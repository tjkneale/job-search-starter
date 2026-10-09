#!/usr/bin/env python3
"""Offline starter utilities. No credentials, network access, or external writes."""

import argparse
import csv
from datetime import date
import json
from pathlib import Path
import re
import shutil
import sys

REPO = Path(__file__).resolve().parent.parent
DECISIONS = {"Pursue", "Watch", "Exclude"}
STAGES = {
    "Research", "Networking planning", "Preparing", "Reached out", "Connected",
    "Informational interview", "Applied", "Interviewing", "Offer", "Won't apply",
    "Closed Lost", "Accepted",
}
VERIFICATION = {"Active", "Closed", "Unverified", "Fictional"}
RESEARCH = {
    "untracked", "partial", "researched", "no_paths_found",
    "existing_contacts_only", "deferred",
}
REQUIRED = {"Company", "Role", "Decision", "Pipeline", "Verification status"}


def company_key(value):
    return " ".join(value.split()).casefold()


def read_roles(root):
    records, issues = [], []
    for path in sorted((root / "opportunities/roles").glob("*.md")):
        fields = {"source_file": path.relative_to(root).as_posix()}
        for line in path.read_text().splitlines():
            if line.startswith("## "):
                break
            match = re.fullmatch(r"- ([^:]+):\s*(.*)", line)
            if match:
                key, value = match.groups()
                if key in fields:
                    issues.append(f"{fields['source_file']}: duplicate {key}")
                fields[key] = value
        for field in sorted(REQUIRED):
            if not fields.get(field):
                issues.append(f"{fields['source_file']}: missing {field}")
        for field, allowed in (("Decision", DECISIONS), ("Pipeline", STAGES),
                               ("Verification status", VERIFICATION)):
            if fields.get(field) not in allowed:
                issues.append(f"{fields['source_file']}: invalid {field}")
        lock = fields.get("CRM board lock", "false")
        if lock not in {"true", "false"}:
            issues.append(f"{fields['source_file']}: invalid CRM board lock")
        if fields.get("Verification status") == "Fictional" and root.name != "examples":
            issues.append(f"{fields['source_file']}: fictional role in personal data")
        if fields.get("Verification status") in {"Active", "Closed"}:
            observed = fields.get("Last verified", "").split(" ", 1)[0]
            try:
                date.fromisoformat(observed)
            except ValueError:
                issues.append(f"{fields['source_file']}: verified status needs actual date")
            if not fields.get("Official posting", "").startswith("https://"):
                issues.append(f"{fields['source_file']}: verified status needs official URL")
            if ".example" in fields.get("Official posting", ""):
                issues.append(f"{fields['source_file']}: example URL cannot verify a real role")
        records.append(fields)
    return records, issues


def read_companies(root):
    path = root / "opportunities/company-list.csv"
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream)
        headers = reader.fieldnames or []
        records = list(reader)
    issues = []
    if len(headers) != len(set(headers)):
        issues.append("company-list.csv: duplicate headers")
    if not {"List", "Advocacy", "Motivation", "Posting"}.issubset(headers):
        return records, ["company-list.csv: missing required headers"]
    paths = [h for h in headers if re.fullmatch(r"Networking path \d+", h)]
    expected = [f"Networking path {n}" for n in range(1, len(paths) + 1)]
    if not paths or paths != expected or headers[
        headers.index("Advocacy") + 1:headers.index("Motivation")
    ] != expected:
        issues.append("company-list.csv: path columns must be consecutive between Advocacy and Motivation")
    for number, row in enumerate(records, 2):
        if None in row or any(v is None for v in row.values()):
            issues.append(f"company-list.csv row {number}: mismatched column count")
        if not (row.get("List") or "").strip():
            issues.append(f"company-list.csv row {number}: missing company")
        if row.get("Advocacy") not in {"", "Yes", "No"}:
            issues.append(f"company-list.csv row {number}: invalid Advocacy")
        for field in ("Motivation", "Posting"):
            if row.get(field) not in {"", "1", "2", "3"}:
                issues.append(f"company-list.csv row {number}: invalid {field}")
    return records, issues


def read_checkpoints(root):
    data = json.loads((root / "research/company-status.json").read_text())
    issues = []
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("companies"), dict):
        raise ValueError("company-status.json: unsupported schema")
    for key, company in data["companies"].items():
        if not isinstance(key, str) or key != company_key(key) or not isinstance(company, dict):
            issues.append("company-status.json: invalid company key/entry")
            continue
        for lane in ("networking", "posting"):
            checkpoint = company.get(lane, {"status": "untracked"})
            if not isinstance(checkpoint, dict) or checkpoint.get("status") not in RESEARCH:
                issues.append(f"{key}: invalid {lane} checkpoint")
                continue
            if checkpoint["status"] in {"researched", "no_paths_found", "partial"}:
                try:
                    date.fromisoformat(checkpoint.get("date", ""))
                except (ValueError, TypeError):
                    issues.append(f"{key}: {lane} needs observation date")
                evidence = checkpoint.get("evidence", "")
                if not isinstance(evidence, str) or not evidence:
                    issues.append(f"{key}: {lane} needs evidence")
                    continue
                reference = Path(evidence)
                resolved = (root / reference).resolve()
                if reference.is_absolute() or not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                    issues.append(f"{key}: {lane} evidence missing or outside data root")
    return data["companies"], issues


def inspect(root):
    if not root.is_dir():
        raise ValueError(f"Data folder not found: {root.name}. Run init for personal work.")
    roles, role_issues = read_roles(root)
    companies, company_issues = read_companies(root)
    checkpoints, checkpoint_issues = read_checkpoints(root)
    return roles, companies, checkpoints, role_issues + company_issues + checkpoint_issues


def initialize(destination, source=None):
    source = source or REPO / "templates/workspace"
    if destination.exists() or destination.is_symlink():
        raise ValueError("workspace/ already exists; no files were overwritten")
    # copytree also refuses an existing destination if one appears concurrently.
    shutil.copytree(source, destination)


def crm_preview(roles):
    # No body, contacts, criteria, or evidence copied. This is not a sync plan.
    return [{
        "company": role["Company"], "role": role["Role"],
        "requisition": role.get("Requisition"), "decision": role["Decision"],
        "local_stage": role["Pipeline"],
        "verification_status": role["Verification status"],
        "fictional": role["Verification status"] == "Fictional",
        "source_file": role["source_file"],
        "board_lock": role.get("CRM board lock", "false") == "true",
    } for role in roles]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("demo", "init", "check", "crm-preview"))
    parser.add_argument("--root", type=Path, help="Data folder; default workspace/, demo always examples/")
    args = parser.parse_args(argv)
    if args.command == "init" and args.root:
        parser.error("init creates workspace/ only; --root is for read-only commands")
    if args.command == "demo" and args.root:
        parser.error("demo reads the bundled examples/ only")
    try:
        if args.command == "init":
            initialize(REPO / "workspace")
            print("Created blank workspace/. Fill candidate context, evidence, criteria, and your resume.")
            return 0
        root = REPO / "examples" if args.command == "demo" else (args.root or REPO / "workspace").resolve()
        roles, companies, checkpoints, issues = inspect(root)
        if issues:
            for issue in issues:
                print(f"ERROR: {issue}", file=sys.stderr)
            return 1
        if args.command == "crm-preview":
            print(json.dumps(crm_preview(roles), indent=2))
        elif args.command == "check":
            print(f"Structure valid: {len(roles)} roles, {len(companies)} company rows. Truth/activity eligibility not assessed.")
        else:
            print("FICTIONAL DEMO — frozen April 15, 2025; no live verification or account access.\n")
            for role in roles:
                print(f"{role['Company']} — {role['Role']}: {role['Decision']} / {role['Pipeline']}")
                print(f"  Next: {role.get('Next action', 'Not recorded')}")
            print("\nCompany research is separate from candidate decisions:")
            for row in companies:
                status = checkpoints.get(company_key(row["List"]), {})
                network = status.get("networking", {}).get("status", "untracked")
                print(f"  {row['List']}: Advocacy={row['Advocacy'] or 'blank'}, Motivation={row['Motivation'] or 'blank'}, Posting={row['Posting'] or 'blank'}; networking={network}")
            print("\nFollow examples/README.md through evidence, prep, capture, package, stories, and review.")
            print("No application submitted. Pending personal actions do not count as completed activities.")
        return 0
    except (ValueError, OSError, KeyError, TypeError, csv.Error) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
