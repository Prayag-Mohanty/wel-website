# WEL Inventory — Complete Windows Setup Guide
### Step-by-step from zero to running website

---

## What you need to download (all free)

| Software | Where to get it | You already have it? |
|---|---|---|
| Python 3.12 | https://python.org/downloads | ❓ Check below |
| VS Code | Already installed | ✅ Yes |
| Git | https://git-scm.com/download/win | Optional |

---

## PART 1 — Install Python

### Step 1 — Download Python
1. Go to: **https://python.org/downloads**
2. Click the big yellow button **"Download Python 3.12.x"**
3. Run the downloaded `.exe` file

### Step 2 — VERY IMPORTANT during install
When the installer opens, you will see a screen with checkboxes at the bottom.

**✅ CHECK THIS BOX: "Add python.exe to PATH"**

This is critical. Without it, nothing will work.

Then click **"Install Now"**.

### Step 3 — Verify Python is installed
After install, open **Command Prompt** (press `Win + R`, type `cmd`, press Enter) and run:
```
python --version
```
You should see something like: `Python 3.12.4`

If you see an error, you missed the "Add to PATH" checkbox. Re-run the installer and check it.

---

## PART 2 — Set Up VS Code for Python

### Step 4 — Open VS Code and install the Python extension
1. Open VS Code
2. Press `Ctrl + Shift + X` to open Extensions
3. Search for **"Python"**
4. Install the one by **Microsoft** (it's the first result)

### Step 5 — Open the VS Code terminal
In VS Code, press **Ctrl + `** (that's the backtick key, top-left of keyboard, below Escape)

This opens a terminal at the bottom of VS Code. All commands from here on go in this terminal.

---

## PART 3 — Create the Project

### Step 6 — Create your project folder
In the VS Code terminal, type these commands one by one (press Enter after each):

```
cd Desktop
mkdir iitb-wel-inventory
cd iitb-wel-inventory
```

You're now inside your project folder on your Desktop.

### Step 7 — Open the folder in VS Code
```
code .
```

This reopens VS Code with your new folder as the workspace. Open the terminal again (`Ctrl + `).

### Step 8 — Create a virtual environment

A virtual environment keeps your project's packages separate from the rest of your computer.

```
python -m venv venv
```

Wait a few seconds. You'll see a new `venv` folder appear.

### Step 9 — Activate the virtual environment

**On Windows (Command Prompt / VS Code terminal):**
```
venv\Scripts\activate
```

After running this, your terminal prompt should show `(venv)` at the start, like:
```
(venv) C:\Users\YourName\Desktop\iitb-wel-inventory>
```

**You must do this every time you open a new terminal window.**

---

## PART 4 — Add All the Project Files

### Step 10 — Create the folder structure

In the VS Code terminal:
```
mkdir templates
mkdir templates\admin
```

### Step 11 — Create all the files

You need to create these files. In VS Code, use **File → New File**, or right-click in the Explorer panel (left sidebar) to create each one.

Files to create:
```
iitb-wel-inventory/
├── app.py                          ← Main application
├── requirements.txt                ← Package list
├── .env                            ← Your settings
└── templates/
    ├── base.html
    ├── landing.html
    ├── login.html
    ├── register.html
    ├── inventory.html
    ├── make_request.html
    ├── my_requests.html
    └── admin/
        ├── dashboard.html
        ├── requests.html
        ├── inventory.html
        ├── teams.html
        └── upload.html
```

**Copy the code for each file from the provided code files.**

---

## PART 5 — Configure Your Settings

### Step 12 — Edit the .env file

Open the `.env` file in VS Code. It should look like this:
```
SECRET_KEY=iitb-wel-super-secret-key-change-this-2024
ADMIN_EMAIL=your_roll_number@iitb.ac.in
```

**Change `your_roll_number@iitb.ac.in` to YOUR actual IITB email address.**
This email will automatically get admin access when you register.

Example:
```
SECRET_KEY=iitb-wel-super-secret-key-2024
ADMIN_EMAIL=22b12345@iitb.ac.in
```

---

## PART 6 — Install Python Packages

### Step 13 — Install all required packages

Make sure your virtual environment is active (you see `(venv)` in the terminal), then run:
```
pip install -r requirements.txt
```

This will download and install: Flask, SQLAlchemy, Flask-Login, pandas, openpyxl, and other packages.

It will take 1-2 minutes. You'll see a lot of text scrolling — that's normal.

When done, you'll see something like:
```
Successfully installed Flask-3.0.3 ...
```

---

## PART 7 — Run the Website

### Step 14 — Start the server

In the terminal (with `(venv)` active):
```
python app.py
```

You should see:
```
Database ready.
Open your browser at: http://localhost:5000
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 15 — Open the website

Open your web browser (Chrome/Firefox/Edge) and go to:
```
http://localhost:5000
```

You will see the **WEL Inventory** landing page!

**To stop the server:** Press `Ctrl + C` in the terminal.

---

## PART 8 — First Time Setup (Do This Once)

### Step 16 — Register as admin

1. Click **"Register Team"** on the landing page
2. Fill in:
   - **Team Name:** anything (e.g. "Lab Admin")
   - **Member Name:** your name
   - **Roll No.:** your roll number
   - **IITB Email:** the SAME email you put in `.env` as `ADMIN_EMAIL`
   - **Password:** something you'll remember
3. Click **"Create Team Account"**

Since your email matches `ADMIN_EMAIL`, you automatically become admin.

### Step 17 — Upload your Excel inventory

1. Click **Admin** in the top navbar → **Upload Excel**
2. Click "Choose File" and select your Excel file
3. Click **"Import Components"**

Your components will appear in the inventory!

### Step 18 — Add Quantity column to your Excel (if not already there)

Before uploading, open your Excel file and add a column called **`Quantity`** with how many of each component you have. If you skip this, everything defaults to 1.

---

## PART 9 — How Students Use the Website

### For each team (one-time registration):
1. Go to `http://localhost:5000`
2. Click **Register Team**
3. Enter:
   - Team name (e.g. "Team Omega")
   - All member names + roll numbers
   - **One IITB email** for the team (any member's)
   - Password (team decides this together)
4. Done — they're logged in

### Making a request:
1. Log in with their team email + password
2. Browse inventory, search components
3. Enter quantity and click **Add to Cart**
4. Go to **Cart** → add notes → **Submit Request**
5. A pending request appears in admin panel

### You (admin) handling requests:
1. Go to Admin → Requests
2. See team name + all member names + roll numbers
3. Click **Approve & Issue** → inventory automatically decrements
4. Or click **Reject**

---

## PART 10 — Daily Usage

Every time you want to run the website:

1. Open VS Code
2. Open terminal (`Ctrl + ``)
3. Navigate to your folder: `cd Desktop\iitb-wel-inventory`
4. Activate venv: `venv\Scripts\activate`
5. Run: `python app.py`
6. Open `http://localhost:5000` in browser

---

## Common Problems and Fixes

| Problem | What to do |
|---|---|
| `'python' is not recognized` | Python not added to PATH. Re-install Python and check "Add to PATH" |
| `venv\Scripts\activate` gives an error about scripts | Run this once: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` then try again |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` with venv active |
| Port 5000 in use | Try `python app.py --port 5001`, then open `http://localhost:5001` |
| Can't login | Make sure email ends with `@iitb.ac.in` |
| Admin menu not showing | Make sure your .env ADMIN_EMAIL matches exactly the email you registered with |
| Excel not uploading | Check file is .xlsx not .csv. Add Quantity column. |

---

## Making the Website Accessible to All Students

Right now the website only works on your laptop (`localhost`). To let all students access it:

### Option A — Share on college WiFi (temporary)
1. Find your laptop's IP address: open cmd and type `ipconfig`
2. Look for `IPv4 Address` — something like `192.168.1.105`
3. Run Flask on all interfaces: change last line in `app.py` to:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5000)
   ```
4. Students on the same WiFi can now open `http://192.168.1.105:5000`

### Option B — Deploy to the internet for free (permanent)
Use **Railway.app**:
1. Create free account at https://railway.app
2. Upload your project to GitHub
3. Connect Railway to your GitHub repo
4. Set your environment variables (SECRET_KEY, ADMIN_EMAIL) in Railway settings
5. You get a public URL like `https://iitb-wel.up.railway.app`

---

## Suggested Improvements (Future)

1. **Return tracking** — teams submit return date; admin restores stock on return
2. **Export to Excel** — download the full request log as a spreadsheet
3. **Low stock email alerts** — auto-email you when a component hits 0
4. **Search by roll number** — find which team has which components issued
5. **Component images** — upload photos of components for easy identification
