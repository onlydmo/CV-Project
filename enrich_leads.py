"""
Verified Lead Extractor
=======================
Extracts job matches with VERIFIED contact emails only.
No guessing, no OSINT, no bounces.
"""

import sys
import csv
from rich import print
from rich.console import Console
from rich.table import Table

from search_jobs import search_matching_roles

console = Console()

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def main():
    console.print("[bold cyan]🚀 Extracting Verified Leads...[/bold cyan]")

    # Get all matches from our keyword scorer
    matches = search_matching_roles()

    # Filter to ONLY verified emails
    verified = [m for m in matches if m.get("company_email")]

    console.print(
        f"Found [bold green]{len(verified)}[/bold green] matches with verified contact emails "
        f"(out of {len(matches)} total matches).\n"
    )

    # Display top 15 in a table
    table = Table(title="Top Verified Leads (Companies ≤ 50 Employees)", show_lines=True)
    table.add_column("Company", style="cyan", width=15)
    table.add_column("Job Title", style="magenta", width=25)
    table.add_column("Size", style="yellow", width=8)
    table.add_column("Contact Email", style="green", width=30)
    table.add_column("Category", style="white", width=25)

    for m in verified[:15]:
        table.add_row(
            m["company"],
            m["title"],
            m["team"],
            m["company_email"],
            m["category"],
        )

    print(table)

    # Export to CSV
    csv_file = "verified_leads.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Company", "Job Title", "Location", "Category",
            "Contact Email", "Apply URL", "Team Size"
        ])
        for r in verified:
            writer.writerow([
                r["company"], r["title"], r["location"], r["category"],
                r["company_email"], r["url"], r["team"]
            ])

    console.print(f"\n[bold green]✓ Exported {len(verified)} verified leads to {csv_file}[/bold green]")
    return verified


if __name__ == "__main__":
    main()
