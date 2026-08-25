# Running WEL Inventory as an admin

Everything below happens at `/admin`. Log in through **Admin** in the top bar,
or go straight to `/admin/login`.

## The short version

| You want to | Go to | Do this |
|---|---|---|
| Add a part | Inventory | **Add component** |
| Fix a wrong model number, location, link | Inventory | pencil icon on the row |
| Change how many you have | Inventory | type in the **Set qty** box, Save |
| Stop offering a part | Inventory | archive icon |
| Issue components to a team | Requests | **Approve & Issue** |
| Add a whole spreadsheet at once | Upload Excel | file or Google Sheets link |
| Let a colleague administer | Dashboard | **Grant Admin Access** |

---

## Editing the component list

**Add component** opens a dialog with every field: type, model number,
description, datasheet link, location and quantity. Only a model number *or* a
description is required — the rest can be filled in later. Leave the serial
number blank and it continues from the highest one already in use. The **type**
box suggests the types already in the inventory, so you do not end up with
"Sensor", "sensors" and "SENSOR" as three separate things.

The **pencil** on any row edits all of those fields on an existing part. The
**Set qty** box next to it is the shortcut for the thing you do most often —
changing a count without opening anything.

### Removing something: archive, not delete

The archive icon hides a part from students. It stays in the database, so every
past request that mentions it still reads correctly, and you can restore it
from the **Archived** tab. This is what you want in almost every case — a part
you have run out of, a line that is no longer stocked.

Permanent deletion is offered only for archived parts that have **never
appeared on a request**, which in practice means typos and bad spreadsheet
rows. If a part has any history, the app refuses and tells you to archive it
instead. That refusal is deliberate: deleting it would leave old requests
pointing at a component that no longer exists.

---

## Approving a request

**Requests** lists everything waiting, newest first, with the team, its
members, what they asked for, and — in the last column — how many you actually
have right now.

**Approve & Issue** does two things: it marks the request approved, and it
subtracts the quantities from stock. You do not then have to go and adjust the
numbers yourself. If any line asks for more than you have, nothing is approved
and the app tells you which part is short, so you never end up with negative
stock.

**Reject** closes the request and changes no quantities.

> **Returns are not tracked.** Approving reduces stock; nothing puts it back
> when a team brings components in. For now, adjust the quantity by hand when
> things are returned. If issue-and-return becomes the normal pattern, that is
> worth building properly rather than working around.

---

## What "live" means here

Every admin screen keeps itself current. If a student submits a request while
you have the Requests page open, it appears on its own. If a colleague approves
something or changes a count, your screen follows within a few seconds. The
number on the **Requests** tab in the navigation bar is the count of pending
requests, and it is live everywhere in the app.

Students see the same thing from the other side: **My Requests** updates itself
the moment you approve or reject, without them refreshing.

Some deliberate details:

- **It will not interrupt you.** While you are typing in a box or have a dialog
  open, the refresh waits. You cannot lose half-entered work to a background
  update.
- **A background tab slows down** from every 5 seconds to every 30, and speeds
  up again the moment you switch back to it.
- **No refresh button needed** — but reloading never hurts.

Under the bonnet this is polling, not websockets: the page asks a very small
endpoint whether anything has changed, and only fetches new content when the
answer is yes. That was a deliberate choice. It survives restarts, proxies and
flaky Wi-Fi, and it works on an ordinary gunicorn worker with no special
server configuration — which a websocket setup would have needed.

---

## Two admins at once

Both see each other's changes within seconds, so there is no need to coordinate
who is looking at what. The one thing to know: approvals are checked against
stock **at the moment you press the button**, not when the page was drawn. If
two of you approve competing requests at nearly the same time, the second one
is refused for lack of stock rather than pushing the count below zero.

---

## Settings worth knowing

Set these in `inventory-app/.env`:

| Variable | What it does |
|---|---|
| `SECRET_KEY` | Signs login sessions. Must be a long random value. |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | The first admin account, created on first start. |
| `DATABASE_URL` | Where the database lives. Defaults to `instance/inventory.db`. |
| `COOKIE_SECURE` | Set to `1` once the app is served over HTTPS. |

Generate a secret key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Additional admins are added from the dashboard — they must register a normal
account first, then you grant it.

---

## Back up the database

It is one file. Copy it somewhere safe on a schedule:

```bash
cp instance/inventory.db ~/backups/inventory-$(date +%F).db
```

If you are running under Docker, `DOCKER.md` has the equivalent command for
pulling it out of the volume.
