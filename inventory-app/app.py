import os, json
from datetime import datetime
from functools import wraps

import pandas as pd
from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template,
                   request, session, url_for)
from flask_login import (LoginManager, UserMixin, current_user,
                         login_required, login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'iitb-wel-change-me-2024')
# Defaults to instance/inventory.db. Set DATABASE_URL to put the database
# somewhere else - a mounted volume, or a Postgres server later on.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# A session cookie is what proves you are an admin, so it should not travel
# with requests that some other site made on your behalf. SameSite=Lax is what
# stops a form on another page from POSTing to /admin/... as you.
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_HTTPONLY'] = True
# Set COOKIE_SECURE=1 in the environment once the site is served over HTTPS.
app.config['SESSION_COOKIE_SECURE'] = os.environ.get('COOKIE_SECURE', '') == '1'

db = SQLAlchemy(app)
lm = LoginManager(app)
lm.login_view = 'login'
lm.login_message = 'Please log in to access this page.'

ADMIN_EMAIL    = os.environ.get('ADMIN_EMAIL', '').lower().strip()
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

class Team(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(120), unique=True, nullable=False)
    members_json = db.Column(db.Text, default='[]')

    @property
    def members(self):
        return json.loads(self.members_json or '[]')

    @members.setter
    def members(self, val):
        self.members_json = json.dumps(val)


class User(UserMixin, db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    team_id       = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    is_admin      = db.Column(db.Boolean, default=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)

    @property
    def team(self):
        return db.session.get(Team, self.team_id) if self.team_id else None


class Component(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    sr_no          = db.Column(db.Integer)
    component_type = db.Column(db.String(100))
    model_no       = db.Column(db.String(100))
    description    = db.Column(db.Text)
    link           = db.Column(db.String(500))
    location       = db.Column(db.String(200))
    quantity       = db.Column(db.Integer, default=1)
    # Archived parts stay in the database so that past requests still resolve,
    # but they disappear from the list students order from.
    archived       = db.Column(db.Boolean, default=False, nullable=False)


class ComponentRequest(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    team_id    = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    status     = db.Column(db.String(20), default='pending')
    notes      = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def team(self):
        return db.session.get(Team, self.team_id)

    @property
    def items(self):
        return RequestItem.query.filter_by(request_id=self.id).all()


class RequestItem(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    request_id   = db.Column(db.Integer, db.ForeignKey('component_request.id'), nullable=False)
    component_id = db.Column(db.Integer, db.ForeignKey('component.id'), nullable=False)
    quantity     = db.Column(db.Integer, nullable=False)

    @property
    def component(self):
        return db.session.get(Component, self.component_id)


class Revision(db.Model):
    """A single row holding a counter that every change to stock or to a
    request bumps.

    The browser polls this number. When it moves, the page knows something
    changed and pulls fresh markup; when it has not moved, the answer is a few
    bytes and the page does nothing. That is the whole live-update mechanism -
    no websockets, no background worker, and nothing that breaks when the app
    runs behind an ordinary gunicorn worker.
    """
    id = db.Column(db.Integer, primary_key=True)
    n  = db.Column(db.Integer, default=0, nullable=False)


def bump():
    """Record that something changed. Call before commit()."""
    row = db.session.get(Revision, 1)
    if row is None:
        row = Revision(id=1, n=0)
        db.session.add(row)
    row.n = (row.n or 0) + 1


def current_revision():
    row = db.session.get(Revision, 1)
    return row.n if row else 0


@lm.user_loader
def load_user(uid):
    return db.session.get(User, int(uid))

def admin_required(f):
    @wraps(f)
    def wrap(*a, **kw):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Please log in as admin to access this page.', 'danger')
            return redirect(url_for('admin_login'))
        return f(*a, **kw)
    return wrap

def _safe_str(v):
    if v is None or (isinstance(v, float) and str(v) == 'nan'):
        return ''
    return str(v).strip()

def _safe_int(v):
    try:
        return int(float(v))
    except Exception:
        return None


@app.route('/')
def landing():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('inventory'))
    return render_template('landing.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('inventory'))

    if request.method == 'POST':
        email     = request.form.get('email', '').strip().lower()
        team_name = request.form.get('team_name', '').strip()
        password  = request.form.get('password', '')
        confirm   = request.form.get('confirm', '')
        m_names   = request.form.getlist('member_name')
        m_regs    = request.form.getlist('member_reg')

        if not email.endswith('@iitb.ac.in'):
            flash('Only @iitb.ac.in email addresses are allowed.', 'danger')
            return render_template('register.html')
        if email == ADMIN_EMAIL:
            flash('This email is reserved. Please use a different email.', 'danger')
            return render_template('register.html')
        if User.query.filter_by(email=email).first():
            flash('An account with this email already exists. Please log in.', 'warning')
            return redirect(url_for('login'))
        if Team.query.filter_by(name=team_name).first():
            flash('A team with that name already exists. Choose a different name.', 'danger')
            return render_template('register.html')
        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return render_template('register.html')
        if password != confirm:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')
        if not team_name:
            flash('Team name is required.', 'danger')
            return render_template('register.html')

        members = []
        for name, reg in zip(m_names, m_regs):
            name = name.strip(); reg = reg.strip()
            if name and reg:
                members.append({'name': name, 'reg_no': reg})
        if not members:
            flash('Add at least one team member with name and registration number.', 'danger')
            return render_template('register.html')

        team         = Team(name=team_name)
        team.members = members
        db.session.add(team)
        db.session.flush()

        user = User(email=email, team_id=team.id, is_admin=False)
        user.set_password(password)
        db.session.add(user)
        bump()
        db.session.commit()

        login_user(user)
        flash(f'Account created for team "{team_name}"! Welcome.', 'success')
        return redirect(url_for('inventory'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('inventory'))

    if request.method == 'POST':
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not email.endswith('@iitb.ac.in'):
            flash('Only @iitb.ac.in email addresses are allowed.', 'danger')
            return render_template('login.html')

        user = User.query.filter_by(email=email).first()

        if user and user.is_admin:
            flash('Admin accounts must use the Admin Login page.', 'warning')
            return redirect(url_for('admin_login'))

        if not user or not user.check_password(password):
            flash('Invalid email or password.', 'danger')
            return render_template('login.html')

        login_user(user)
        nxt = request.args.get('next')
        return redirect(nxt or url_for('inventory'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    was_admin = current_user.is_admin
    logout_user()
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('admin_login') if was_admin else url_for('landing'))


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    if current_user.is_authenticated:
        logout_user()
        session.clear()

    if request.method == 'POST':
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = User.query.filter_by(email=email, is_admin=True).first()
        if not user or not user.check_password(password):
            flash('Invalid admin credentials.', 'danger')
            return render_template('admin/login.html')

        login_user(user)
        flash('Welcome back, Admin!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/login.html')


@app.route('/inventory')
@login_required
def inventory():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    q           = request.args.get('q', '').strip()
    type_filter = request.args.get('type', '')
    qry = Component.query.filter(Component.archived.is_(False))
    if q:
        qry = qry.filter(db.or_(
            Component.model_no.ilike(f'%{q}%'),
            Component.description.ilike(f'%{q}%'),
            Component.component_type.ilike(f'%{q}%'),
            Component.location.ilike(f'%{q}%'),
        ))
    if type_filter:
        qry = qry.filter(Component.component_type == type_filter)
    components = qry.order_by(Component.sr_no).all()
    types = [r[0] for r in db.session.query(Component.component_type)
             .filter(Component.archived.is_(False)).distinct().all() if r[0]]
    cart  = session.get('cart', {})
    return render_template('inventory.html', components=components,
                           q=q, types=types, type_filter=type_filter, cart=cart)


@app.route('/cart/add/<int:cid>', methods=['POST'])
@login_required
def add_to_cart(cid):
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    qty  = max(1, int(request.form.get('quantity', 1)))
    cart = session.get('cart', {})
    cart[str(cid)] = cart.get(str(cid), 0) + qty
    session['cart'] = cart
    flash('Added to request cart.', 'success')
    return redirect(url_for('inventory'))


@app.route('/cart/remove/<int:cid>')
@login_required
def remove_from_cart(cid):
    cart = session.get('cart', {})
    cart.pop(str(cid), None)
    session['cart'] = cart
    return redirect(url_for('make_request'))


@app.route('/cart/clear')
@login_required
def clear_cart():
    session['cart'] = {}
    return redirect(url_for('inventory'))


@app.route('/request', methods=['GET', 'POST'])
@login_required
def make_request():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    if not current_user.team_id:
        flash('No team linked to your account.', 'warning')
        return redirect(url_for('inventory'))

    pending = ComponentRequest.query.filter_by(
        team_id=current_user.team_id, status='pending').first()
    if pending:
        flash('Your team already has a pending request. Wait for it to be processed.', 'warning')
        return redirect(url_for('my_requests'))

    cart       = session.get('cart', {})
    cart_items = []
    for cid, qty in cart.items():
        comp = db.session.get(Component, int(cid))
        if comp:
            cart_items.append((comp, qty))

    if request.method == 'POST':
        if not cart_items:
            flash('Your cart is empty. Add components first.', 'danger')
            return redirect(url_for('inventory'))
        notes   = request.form.get('notes', '')
        new_req = ComponentRequest(team_id=current_user.team_id, notes=notes)
        db.session.add(new_req)
        db.session.flush()
        for comp, qty in cart_items:
            ri = RequestItem(request_id=new_req.id,
                             component_id=comp.id, quantity=int(qty))
            db.session.add(ri)
        bump()
        db.session.commit()
        session['cart'] = {}
        flash('Request submitted! The lab team will review it shortly.', 'success')
        return redirect(url_for('my_requests'))

    return render_template('make_request.html', cart_items=cart_items)


@app.route('/my-requests')
@login_required
def my_requests():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    reqs = ComponentRequest.query.filter_by(
        team_id=current_user.team_id
    ).order_by(ComponentRequest.created_at.desc()).all()
    return render_template('my_requests.html', requests=reqs)


@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin/dashboard.html', **_dashboard_stats())


def _dashboard_stats():
    return dict(
        pending=ComponentRequest.query.filter_by(status='pending').count(),
        total_comp=Component.query.filter(Component.archived.is_(False)).count(),
        total_teams=Team.query.count(),
        low_stock=Component.query.filter(Component.archived.is_(False),
                                         Component.quantity <= 2)
                           .order_by(Component.quantity).all(),
    )


@app.route('/admin/requests')
@login_required
@admin_required
def admin_requests():
    status = request.args.get('status', 'pending')
    reqs   = ComponentRequest.query.filter_by(status=status) \
                             .order_by(ComponentRequest.created_at.desc()).all()
    return render_template('admin/requests.html', requests=reqs, status=status)


@app.route('/admin/request/<int:rid>/approve', methods=['POST'])
@login_required
@admin_required
def approve_request(rid):
    req = ComponentRequest.query.get_or_404(rid)
    if req.status != 'pending':
        flash('Request is not pending.', 'warning')
        return redirect(url_for('admin_requests'))
    for item in req.items:
        if item.component.quantity < item.quantity:
            flash(f'Not enough stock for {item.component.model_no} '
                  f'(have {item.component.quantity}, need {item.quantity}).', 'danger')
            return redirect(url_for('admin_requests'))
    for item in req.items:
        item.component.quantity -= item.quantity
    req.status     = 'approved'
    req.updated_at = datetime.utcnow()
    bump()
    db.session.commit()
    flash(f'Request #{rid} approved! Inventory updated automatically.', 'success')
    return redirect(url_for('admin_requests'))


@app.route('/admin/request/<int:rid>/reject', methods=['POST'])
@login_required
@admin_required
def reject_request(rid):
    req            = ComponentRequest.query.get_or_404(rid)
    req.status     = 'rejected'
    req.updated_at = datetime.utcnow()
    bump()
    db.session.commit()
    flash(f'Request #{rid} rejected.', 'info')
    return redirect(url_for('admin_requests'))


@app.route('/admin/inventory')
@login_required
@admin_required
def admin_inventory():
    show = request.args.get('show', 'active')
    return render_template('admin/inventory.html', show=show,
                           components=_admin_components(show),
                           rev=current_revision())


def _admin_components(show):
    qry = Component.query
    if show != 'archived':
        qry = qry.filter(Component.archived.is_(False))
    else:
        qry = qry.filter(Component.archived.is_(True))
    return qry.order_by(Component.sr_no, Component.id).all()


@app.route('/admin/component/update/<int:cid>', methods=['POST'])
@login_required
@admin_required
def update_quantity(cid):
    comp          = Component.query.get_or_404(cid)
    comp.quantity = max(0, _safe_int(request.form.get('quantity')) or 0)
    bump()
    db.session.commit()
    flash(f'Quantity for {comp.model_no} updated.', 'success')
    return redirect(url_for('admin_inventory'))


@app.route('/admin/upload', methods=['GET', 'POST'])
@login_required
@admin_required
def upload_excel():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f or not f.filename.endswith(('.xlsx', '.xls')):
            flash('Please upload a valid .xlsx / .xls file.', 'danger')
            return redirect(url_for('upload_excel'))
        try:
            df = pd.read_excel(f)
            df.columns = [str(c).strip().lower()
                          .replace(' ', '_').replace('.', '')
                          .replace('(', '').replace(')', '')
                          for c in df.columns]
            count = 0
            for _, row in df.iterrows():
                comp = Component(
                    sr_no=_safe_int(row.get('sr_no') or row.get('sno') or row.get('s_no')),
                    component_type=_safe_str(row.get('type_of_component') or row.get('type')),
                    model_no=_safe_str(row.get('model_no') or row.get('model')),
                    description=_safe_str(row.get('description')),
                    link=_safe_str(row.get('link') or row.get('url')),
                    location=_safe_str(row.get('location') or row.get('location_where_its_keep')),
                    quantity=_safe_int(row.get('quantity') or row.get('qty')) or 1,
                )
                db.session.add(comp)
                count += 1
            bump()
            db.session.commit()
            flash(f'Successfully imported {count} components!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error reading file: {e}', 'danger')
        return redirect(url_for('admin_inventory'))
    return render_template('admin/upload.html')


# ---------------------------------------------------------------------------
# Editing the component list
#
# Before this, an admin could change a quantity and nothing else: adding a part
# or fixing a wrong model number meant re-importing the whole spreadsheet.
# ---------------------------------------------------------------------------

COMPONENT_FIELDS = ('component_type', 'model_no', 'description',
                    'link', 'location')


def _read_component_form(comp):
    """Copy the posted fields onto a Component. Returns an error string or None."""
    for f in COMPONENT_FIELDS:
        setattr(comp, f, _safe_str(request.form.get(f)))
    comp.sr_no    = _safe_int(request.form.get('sr_no'))
    comp.quantity = max(0, _safe_int(request.form.get('quantity')) or 0)
    if not comp.model_no and not comp.description:
        return 'A component needs at least a model number or a description.'
    return None


@app.route('/admin/component/new', methods=['POST'])
@login_required
@admin_required
def create_component():
    comp = Component()
    err  = _read_component_form(comp)
    if err:
        flash(err, 'danger')
        return redirect(url_for('admin_inventory'))
    if comp.sr_no is None:
        # Continue the existing numbering rather than leaving a blank column.
        highest    = db.session.query(db.func.max(Component.sr_no)).scalar()
        comp.sr_no = (highest or 0) + 1
    db.session.add(comp)
    bump()
    db.session.commit()
    flash('Added %s to the inventory.' % (comp.model_no or comp.description[:40]), 'success')
    return redirect(url_for('admin_inventory'))


@app.route('/admin/component/<int:cid>/edit', methods=['POST'])
@login_required
@admin_required
def edit_component(cid):
    comp = Component.query.get_or_404(cid)
    err  = _read_component_form(comp)
    if err:
        db.session.rollback()
        flash(err, 'danger')
        return redirect(url_for('admin_inventory'))
    bump()
    db.session.commit()
    flash('Updated %s.' % (comp.model_no or ('component #%d' % cid)), 'success')
    return redirect(url_for('admin_inventory'))


@app.route('/admin/component/<int:cid>/archive', methods=['POST'])
@login_required
@admin_required
def archive_component(cid):
    comp          = Component.query.get_or_404(cid)
    comp.archived = not comp.archived
    bump()
    db.session.commit()
    flash('%s %s.' % (comp.model_no or ('Component #%d' % cid),
                      'archived and hidden from students' if comp.archived
                      else 'restored to the inventory'), 'success')
    return redirect(url_for('admin_inventory',
                            show='archived' if comp.archived else 'active'))


@app.route('/admin/component/<int:cid>/delete', methods=['POST'])
@login_required
@admin_required
def delete_component(cid):
    """Permanent delete, allowed only when nothing points at the component.

    A component named on a past request cannot be deleted: the request would
    then refer to a row that no longer exists, and every page that lists it
    would break. Archive those instead.
    """
    comp = Component.query.get_or_404(cid)
    used = RequestItem.query.filter_by(component_id=cid).count()
    if used:
        flash('%s appears on %d request%s, so it cannot be deleted without '
              'breaking them. Archive it instead - it disappears from the '
              'student list but the history stays intact.'
              % (comp.model_no or ('Component #%d' % cid), used,
                 '' if used == 1 else 's'), 'warning')
        return redirect(url_for('admin_inventory', show='archived'))
    name = comp.model_no or ('Component #%d' % cid)
    db.session.delete(comp)
    bump()
    db.session.commit()
    flash('Deleted %s permanently.' % name, 'success')
    return redirect(url_for('admin_inventory', show='archived'))


# ---------------------------------------------------------------------------
# Live updates
#
# Pages poll /api/version. It is two cheap queries and a handful of bytes, so
# it can be called every few seconds without mattering. When the number moves,
# the page asks for the fragment it is showing and swaps it in - the markup
# comes from the same Jinja partial the full page uses, so there is no second
# copy of it to keep in step.
# ---------------------------------------------------------------------------

@app.route('/api/version')
@login_required
def api_version():
    return {
        'rev':     current_revision(),
        'pending': ComponentRequest.query.filter_by(status='pending').count(),
    }


@app.route('/admin/dashboard/fragment')
@login_required
@admin_required
def admin_dashboard_fragment():
    return render_template('admin/_dashboard_stats.html', **_dashboard_stats())


@app.route('/admin/requests/fragment')
@login_required
@admin_required
def admin_requests_fragment():
    status = request.args.get('status', 'pending')
    reqs   = ComponentRequest.query.filter_by(status=status)                              .order_by(ComponentRequest.created_at.desc()).all()
    return render_template('admin/_requests_list.html',
                           requests=reqs, status=status)


@app.route('/admin/inventory/fragment')
@login_required
@admin_required
def admin_inventory_fragment():
    show = request.args.get('show', 'active')
    return render_template('admin/_inventory_rows.html',
                           components=_admin_components(show), show=show)


@app.route('/my-requests/fragment')
@login_required
def my_requests_fragment():
    if current_user.is_admin:
        return ('', 204)
    reqs = ComponentRequest.query.filter_by(
        team_id=current_user.team_id
    ).order_by(ComponentRequest.created_at.desc()).all()
    return render_template('_my_requests_list.html', requests=reqs)


@app.route('/admin/teams')
@login_required
@admin_required
def admin_teams():
    teams = Team.query.order_by(Team.name).all()
    return render_template('admin/teams.html', teams=teams)


@app.route('/admin/make-admin', methods=['POST'])
@login_required
@admin_required
def make_admin():
    email = request.form.get('email', '').strip().lower()
    user  = User.query.filter_by(email=email).first()
    if not user:
        flash(f'No account found for {email}. They must register first.', 'danger')
    else:
        user.is_admin = True
        db.session.commit()
        flash(f'{email} is now an admin.', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/import-sheet', methods=['POST'])
@login_required
@admin_required
def import_google_sheet():
    """Import inventory directly from a Google Sheets link."""
    sheet_url = request.form.get('sheet_url', '').strip()
    if not sheet_url:
        flash('Please provide a Google Sheets URL.', 'danger')
        return redirect(url_for('upload_excel'))

    try:
        # Convert any Google Sheets URL to a CSV export URL
        import re
        # Extract the spreadsheet ID
        match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', sheet_url)
        if not match:
            flash('Invalid Google Sheets URL. Please copy the link from your browser address bar.', 'danger')
            return redirect(url_for('upload_excel'))

        sheet_id = match.group(1)
        # Extract gid (sheet tab) if present
        gid_match = re.search(r'gid=(\d+)', sheet_url)
        gid = gid_match.group(1) if gid_match else '0'

        csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}'

        df = pd.read_csv(csv_url)
        df.columns = [str(c).strip().lower()
                      .replace(' ', '_').replace('.', '')
                      .replace('(', '').replace(')', '')
                      for c in df.columns]

        count = 0
        for _, row in df.iterrows():
            comp = Component(
                sr_no=_safe_int(row.get('sr_no') or row.get('sno') or row.get('s_no')),
                component_type=_safe_str(row.get('type_of_component') or row.get('type')),
                model_no=_safe_str(row.get('model_no') or row.get('model')),
                description=_safe_str(row.get('description')),
                link=_safe_str(row.get('link') or row.get('url')),
                location=_safe_str(row.get('location') or row.get('location_where_its_keep')),
                quantity=_safe_int(row.get('quantity') or row.get('qty')) or 1,
            )
            db.session.add(comp)
            count += 1

        bump()
        db.session.commit()
        flash(f'Successfully imported {count} components from Google Sheets!', 'success')

    except Exception as e:
        db.session.rollback()
        flash(f'Error importing Google Sheet: {e}. Make sure the sheet is set to "Anyone with the link can view".', 'danger')

    return redirect(url_for('admin_inventory'))


# ---------------------------------------------------------------------------
# Start-up
# ---------------------------------------------------------------------------

def ensure_schema():
    """Add columns that a database created by an older version is missing.

    `db.create_all()` creates missing *tables* but never alters existing ones,
    so a database that predates the `archived` column would still be missing
    it and every query touching it would fail. This adds it in place, keeping
    the stock already recorded.
    """
    from sqlalchemy import inspect, text
    insp = inspect(db.engine)
    if 'component' not in insp.get_table_names():
        return
    cols = {c['name'] for c in insp.get_columns('component')}
    if 'archived' not in cols:
        db.session.execute(text(
            'ALTER TABLE component ADD COLUMN archived BOOLEAN NOT NULL DEFAULT 0'))
        db.session.commit()
        print('Schema: added component.archived')


def init_db():
    """Create the tables, upgrade an older database, seed the admin account."""
    db.create_all()
    ensure_schema()
    if ADMIN_EMAIL and not User.query.filter_by(email=ADMIN_EMAIL).first():
        admin = User(email=ADMIN_EMAIL, is_admin=True)
        admin.set_password(ADMIN_PASSWORD)
        db.session.add(admin)
        db.session.commit()
        print('Admin account created: %s' % ADMIN_EMAIL)
    if db.session.get(Revision, 1) is None:
        db.session.add(Revision(id=1, n=0))
        db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        init_db()
        if ADMIN_EMAIL:
            print(f'Admin account ready: {ADMIN_EMAIL}')
        print('Database ready.')
        print('Student portal : http://localhost:5000')
        print('Admin portal   : http://localhost:5000/admin/login')
    app.run(debug=True)
