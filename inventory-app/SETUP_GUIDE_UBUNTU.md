# WEL Inventory — Complete Setup Guide (Ubuntu)

---

## What This Website Does

- Teams register with their IITB email, team name, member names and roll numbers
- Teams browse the component inventory, search, and add items to a cart
- Teams submit one request at a time to the lab team
- Admin (lab team) sees all requests with team name and member details
- Admin clicks Approve — inventory count decrements AUTOMATICALLY
- Admin clicks Reject — request is marked rejected, no stock change
- You NEVER need to update the Excel file again after the first upload

---

## Two Separate Portals

| Who | URL | What they can do |
|---|---|---|
| Students / Teams | http://localhost:5000 | Register, login, browse, request |
| Admin / Lab Team | http://localhost:5000/admin/login | Manage inventory, approve/reject requests |

Students cannot see or access anything in the admin portal. They are completely separate.

---

## PART 1 — One Time Setup

### Step 1 — Open Terminal
Press Ctrl + Alt + T

### Step 2 — Install Python tools
```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```
Type your Ubuntu password when asked. You will not see the characters — that is normal.

### Step 3 — Extract the ZIP file
If the ZIP is in your Downloads folder:
```bash
cd ~/Desktop
unzip ~/Downloads/IITB_WEL_Inventory.zip -d iitb-wel-inventory
cd iitb-wel-inventory
```

### Step 4 — Create virtual environment
```bash
python3 -m venv venv
```

### Step 5 — Activate virtual environment
```bash
source venv/bin/activate
```
Your terminal will now show (venv) at the start. You must do this every time you open a new terminal.

### Step 6 — Install required packages
```bash
pip install -r requirements.txt
```
Wait 1-2 minutes until you see: Successfully installed Flask...

If you get a pandas error, run this instead:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 7 — Edit the .env file
```bash
gedit .env
```

Change the file to:
```
SECRET_KEY=iitb-wel-super-secret-key-2024
ADMIN_EMAIL=your_actual_email@iitb.ac.in
ADMIN_PASSWORD=choose_a_strong_password
```

Replace your_actual_email@iitb.ac.in with your real IITB email.
Replace choose_a_strong_password with a password you will remember.

Press Ctrl + S to save. Close gedit.

### Step 8 — Delete old database (if you ran the old version before)
```bash
rm -f instance/inventory.db
```
This is only needed if you ran the old version. Skip if this is a fresh install.

### Step 9 — Run the website
```bash
python3 app.py
```

You will see:
```
Admin account created: your_email@iitb.ac.in
Password: your_password
Database ready.
Student portal : http://localhost:5000
Admin portal   : http://localhost:5000/admin/login
```

### Step 10 — Open in browser
Open Firefox or Chrome and go to:
```
http://localhost:5000
```

You will see the WEL Inventory homepage with two options:
- Student / Team portal
- Admin portal

---

## PART 2 — First Time Admin Setup

### Step 11 — Log in as admin
1. Click Admin Login on the homepage (or go to http://localhost:5000/admin/login)
2. Enter the email and password you put in the .env file
3. You are now in the Admin Dashboard

### Step 12 — Upload your Excel inventory file
1. Click Upload Excel in the top navbar
2. Click Choose File
3. Select your Excel file
4. Click Import Components

Your components now appear in the inventory.

NOTE: Make sure your Excel file has a Quantity column.
If it does not, add one in LibreOffice Calc before uploading.
Without it, everything will default to quantity 1.

---

## PART 3 — How Students Use the Website

### Registering (one time per team):
1. Go to http://localhost:5000
2. Click Register Team
3. Fill in:
   - Team Name (e.g. Team Omega)
   - Member Name and Roll Number for each member (click + Add Another Member for more)
   - One IITB email for the team account
   - Password (team decides this together)
4. Click Create Team Account
5. They are now logged in

### Making a request:
1. Log in at http://localhost:5000 with team email and password
2. Browse inventory, use the search bar to find components
3. Enter quantity and click Add to Cart
4. Click Cart in the top navbar
5. Add notes if needed
6. Click Submit Request
7. The request goes to the admin dashboard as Pending

---

## PART 4 — How Admin Approves Requests

1. Log in at http://localhost:5000/admin/login
2. Click Requests in the navbar
3. You see all pending requests with:
   - Team name
   - All member names and roll numbers
   - What components they want and how many
   - Current stock vs requested quantity
4. Click Approve & Issue — inventory AUTOMATICALLY decrements
   OR click Reject — nothing changes in inventory
5. The team sees their request status updated

### Important about inventory:
- You do NOT need to update the Excel file after the first upload
- The database tracks all quantities automatically
- When you approve a request, the count goes down by itself
- You can manually edit quantities in Admin > Inventory if needed
- The Excel file is only for the initial import

---

## PART 5 — Running the Website Every Day

Open terminal (Ctrl + Alt + T) and run:

```bash
cd ~/Desktop/iitb-wel-inventory
source venv/bin/activate
python3 app.py
```

Then open http://localhost:5000 in browser.

To stop the website: Press Ctrl + C in the terminal.

---

## PART 6 — Making It Accessible to All Students

Right now only your computer can access it (localhost).

### Option A — Campus WiFi (temporary, easy)

Find your IP address:
```bash
hostname -I
```
You will see something like: 10.105.20.45

Change the last line of app.py from:
```python
app.run(debug=True)
```
To:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Now students on the same WiFi can open:
```
http://10.105.20.45:5000
```
Replace 10.105.20.45 with your actual IP.

NOTE: Your laptop must stay on and the server must be running.

### Option B — Internet (permanent, free hosting)
Use Railway.app to host it online so anyone can access it from anywhere.
Ask for help if you want to do this step.

---

## Common Problems

| Problem | Solution |
|---|---|
| sudo apt update gives error | Check your internet connection |
| venv not activating | Make sure you are inside the project folder first: cd ~/Desktop/iitb-wel-inventory |
| pandas install fails | Run: pip install --upgrade pip then try again |
| Website not opening | Make sure python3 app.py is still running in terminal |
| Admin menu visible to students | Delete inventory.db and restart: rm -f instance/inventory.db then python3 app.py |
| Forgot admin password | Edit .env with new password, delete inventory.db, restart |
| Excel not importing | Make sure file is .xlsx not .csv and column names match the guide |
| Port already in use | Run: python3 app.py --port 5001 and open http://localhost:5001 |

---

## Summary of All URLs

| URL | Who uses it |
|---|---|
| http://localhost:5000 | Landing page — everyone |
| http://localhost:5000/login | Student login |
| http://localhost:5000/register | New team registration |
| http://localhost:5000/inventory | Browse components (students) |
| http://localhost:5000/admin/login | Admin login |
| http://localhost:5000/admin | Admin dashboard |
| http://localhost:5000/admin/requests | See and approve requests |
| http://localhost:5000/admin/inventory | Manage stock |
| http://localhost:5000/admin/teams | See all registered teams |
| http://localhost:5000/admin/upload | Upload Excel file |

