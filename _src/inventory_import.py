#!/usr/bin/env python3
"""Turn the WEL component spreadsheet into the data the website reads.

    python _src/inventory_import.py path/to/components.xlsx
    python _src/inventory_import.py path/to/components.csv

Writes assets/data/inventory.json, which the WEL Inventory page on the site
loads. Run it again whenever the spreadsheet changes, then rebuild and push.

The column names it accepts are exactly the ones inventory-app/app.py accepts
in its "Upload Excel" screen, so the same file works for both: upload it to the
app for the request workflow, run it through here for the public listing.

  Sr No / SNo / S No          -> sr_no
  Type of Component / Type    -> component_type
  Model No / Model            -> model_no
  Description                 -> description
  Link / URL                  -> link
  Location                    -> location
  Quantity / Qty              -> quantity      (missing means 1)

Reading .xlsx needs pandas and openpyxl; .csv needs nothing.
"""
import csv
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "data", "inventory.json")


def norm(name):
    """Column name normalisation, matching app.py."""
    return (str(name).strip().lower()
            .replace(" ", "_").replace(".", "")
            .replace("(", "").replace(")", ""))


def pick(row, *names):
    for n in names:
        v = row.get(n)
        if v is not None and str(v).strip() and str(v).strip().lower() != "nan":
            return str(v).strip()
    return ""


def to_int(v, default=None):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return default


def read_rows(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in (".xlsx", ".xls"):
        try:
            import pandas as pd
        except ImportError:
            sys.exit("Reading %s needs pandas: pip install pandas openpyxl" % ext)
        df = pd.read_excel(path)
        df.columns = [norm(c) for c in df.columns]
        return df.to_dict("records")
    if ext == ".csv":
        with open(path, newline="", encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh)
            reader.fieldnames = [norm(c) for c in (reader.fieldnames or [])]
            return list(reader)
    sys.exit("Unsupported file type %r - give me an .xlsx, .xls or .csv" % ext)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    if not os.path.exists(src):
        sys.exit("No such file: %s" % src)

    components = []
    for row in read_rows(src):
        model = pick(row, "model_no", "model")
        desc = pick(row, "description")
        if not model and not desc:
            continue                      # skip blank rows
        components.append({
            "sr": to_int(pick(row, "sr_no", "sno", "s_no"), len(components) + 1),
            "type": pick(row, "type_of_component", "type"),
            "model": model,
            "description": desc,
            "link": pick(row, "link", "url"),
            "location": pick(row, "location", "location_where_its_keep"),
            "qty": to_int(pick(row, "quantity", "qty"), 1) or 1,
        })

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({
            "updated": date.today().isoformat(),
            "sample": False,
            "components": components,
        }, fh, indent=1, ensure_ascii=False)

    types = sorted({c["type"] for c in components if c["type"]})
    print("Wrote %s" % os.path.relpath(OUT, ROOT))
    print("  %d components, %d types" % (len(components), len(types)))
    print("  total units in stock: %d" % sum(c["qty"] for c in components))
    if types:
        print("  types: %s" % ", ".join(types[:12]) + (" ..." if len(types) > 12 else ""))
    print("\nNow run:  python _src/build.py")


if __name__ == "__main__":
    main()
