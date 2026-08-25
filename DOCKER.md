# Running the whole thing with Docker

## What Docker actually is

A container is your application packaged together with everything it needs to
run — the right Python version, the right libraries, the right configuration —
in one sealed box. Anyone with Docker installed runs that box with one command
and gets exactly the same result, on Windows, on Linux, on the lab server, on a
laptop. Nobody has to install Python, pick a version, or fight with `pip`.

That is the whole idea: **"it works on my machine" becomes "it works
everywhere", because the machine travels with the code.**

## Is it worth it here? Honestly:

| | Docker helps? |
|---|---|
| **The website** | Only if you self-host. GitHub Pages already serves it free, and a container adds nothing there. It becomes useful if the lab wants the site on its own server with no dependency on GitHub. |
| **WEL Inventory** | **Yes, a lot.** It is a Python app with dependencies and a database, and getting that running on a shared server is exactly the awkward job containers were invented for. |
| **"Editing anywhere"** | That part is git, not Docker. What Docker adds is that you can *build and preview* your edits without installing Python — see the `dev` profile below. |

So: your senior is right, and mostly right about the inventory app.

---

## Quick start

Install Docker Desktop (Windows/Mac) or Docker Engine (Linux), then:

```bash
copy inventory-app\.env.example inventory-app\.env
```

Edit that file and set a real `SECRET_KEY`, `ADMIN_EMAIL` and `ADMIN_PASSWORD`.
Generate a key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Then start everything:

```bash
docker compose up -d
```

- website → <http://localhost:8080>
- WEL Inventory → <http://localhost:5000>

`docker compose down` stops both. The inventory database is kept.

> If you see `env file ... .env not found`, you skipped the first step. That is
> deliberate: the app would otherwise start with the sample secret key from the
> repository, which anyone can read.

## The three services

**`site`** builds the HTML from `_src/` *inside the image* and serves it with
nginx. Because it rebuilds during the build, the container can never be out of
step with the source — and the build fails if any internal link is broken, so a
broken site cannot be packaged. The finished image contains no Python, just
nginx and the generated files.

**`inventory`** runs the Flask app under gunicorn as a non-root user. It reads
`inventory-app/.env` for its settings.

**`dev`** is for editing. It mounts the repository into a container and runs
`_src/dev.py`, so saving a file rebuilds the site and refreshes the browser —
the normal live-editing loop, without installing Python:

```bash
docker compose --profile dev up
```

Then edit on <http://localhost:8000>. Your files are on your own disk, so your
editor, git and everything else work exactly as usual.

## Where the data lives

The inventory database is on a named volume called `inventory-db`, mounted at
`/app/instance`. It survives `docker compose down`, rebuilds and restarts.

**It does not survive `docker compose down -v`.** That flag deletes volumes.
Back the database up first:

```bash
docker compose cp inventory:/app/instance/inventory.db ./inventory-backup.db
```

Restore it with:

```bash
docker compose cp ./inventory-backup.db inventory:/app/instance/inventory.db
```

Worth putting that backup on a schedule once real stock data is in it.

## On the lab server

```bash
git clone https://github.com/Prayag-Mohanty/wel-website.git
cd wel-website
cp inventory-app/.env.example inventory-app/.env   # then edit it
docker compose up -d
```

Both services carry `restart: unless-stopped`, so they come back by themselves
after a reboot. To update after pushing changes:

```bash
git pull && docker compose up -d --build
```

Two things to sort out with whoever runs the server:

- **Ports.** The containers publish 8080 and 5000. For real use, put nginx or
  Apache in front on ports 80/443 and proxy to them, so people do not have to
  type a port number, and so you get HTTPS.
- **Reachability.** If the server is only visible inside the institute network,
  the site and the inventory app are too. That is fine for the inventory app —
  arguably right, since it holds student details — but the public site should
  stay on GitHub Pages.

## What I would actually do

**Keep the website on GitHub Pages** and use Docker for the inventory app on the
lab server. That gives you a public site that costs nothing and needs no
babysitting, and a stock system that lives inside the institute network where
its data belongs.

The `site` container is there for the day you want to move off GitHub, or to
demonstrate the whole thing on a laptop with no internet.

## Caveat

These files are written but **not yet built** — the Docker daemon was not
running on the machine where they were added, so the compose file is validated
but the images have never been assembled. Expect to fix a small thing or two on
the first `docker compose up --build`. If it complains, paste the error and it
can be sorted quickly.
