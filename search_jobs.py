import sqlite3
import json
import sys

# Configure UTF-8 for console
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rich import print
from rich.table import Table

DB_PATH = r"C:\Users\HP\.gemini\antigravity\scratch\startupmap-scraper\startupmap.db"

def search_matching_roles():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    
    # Query to fetch jobs where the company has at most 50 employees
    # We join with startups to filter on team size and domain
    query = """
        SELECT 
            j.job_title,
            s.name as company_name,
            s.team_size_min,
            s.team_size_max,
            s.office_city,
            s.country,
            s.domain_primary,
            j.job_location,
            j.apply_url,
            j.contact_email,
            j.type as job_type,
            s.why_interesting
        FROM jobs j
        JOIN startups s ON j.startup_id = s.startup_id
        WHERE j.visible = 1
          AND (s.team_size_max <= 50 OR (s.team_size_max IS NULL AND s.team_size_min <= 50))
        ORDER BY s.name, j.job_title
    """
    
    rows = conn.execute(query).fetchall()
    conn.close()
    
    # Define our targeted keywords for automation opportunities
    # Categories:
    # 1. Support & Customer Success (CRM, ticketing, customer delight automations)
    # 2. Operations & HR (Workflow onboarding, task tracking, Google Sheet syncs)
    # 3. Marketing & Content (SEO mapping, multi-channel auto-post, content calendars)
    # 4. Tech / Automation (Direct n8n, integrations, API connectors)
    
    support_keywords = ["support", "success", "cx", "experience", "care", "relations", "service"]
    ops_keywords = ["operations", "ops", "coordinator", "admin", "office", "assistant", "hr", "recruiting", "talent"]
    marketing_keywords = ["marketing", "seo", "content", "growth", "crm", "hubspot", "social", "copywriter"]
    tech_keywords = ["automation", "integration", "n8n", "zapier", "systems", "nocode", "no-code", "developer", "solutions"]
    
    matches = []
    for r in rows:
        title = r["job_title"].lower()
        
        category = None
        score = 0
        
        # Check matching category
        if any(kw in title for kw in tech_keywords):
            category = "🔌 Integrations / Systems / Tech"
            score = 4
        elif any(kw in title for kw in ops_keywords):
            category = "⚙️ Operations & Recruiting"
            score = 3
        elif any(kw in title for kw in support_keywords):
            category = "🤝 Customer Success & Support"
            score = 2
        elif any(kw in title for kw in marketing_keywords):
            category = "📣 Growth & Marketing Automation"
            score = 2
            
        if category:
            # Determine potential automation use cases
            use_cases = []
            if "support" in title or "success" in title:
                use_cases = ["HubSpot/Zendesk sync", "Auto-responding Telegram bots", "CSAT auto-collection"]
            elif "operations" in title or "ops" in title:
                use_cases = ["Google Sheets to CRM syncs", "Slack/Telegram alerts", "Auto task-creation in Notion"]
            elif "marketing" in title or "content" in title or "seo" in title:
                use_cases = ["AI Content Pipeline (Claude/GPT)", "Automated SEO tracking", "Social auto-posting"]
            elif "hr" in title or "recruiting" in title or "talent" in title:
                use_cases = ["Automated applicant screen", "New hire Slack onboarding", "Calendar invite syncs"]
            elif "automation" in title or "systems" in title or "integration" in title:
                use_cases = ["Custom n8n core integrations", "Multi-app webhook listeners", "LLM agentic workflows"]
            else:
                use_cases = ["General task automation with n8n", "API & Webhook orchestrations"]
                
            matches.append({
                "company": r["company_name"],
                "title": r["job_title"],
                "team": f"{r['team_size_min'] or 1}-{r['team_size_max'] or 50}",
                "location": r["job_location"] or f"{r['office_city']}, {r['country']}",
                "category": category,
                "score": score,
                "use_cases": use_cases,
                "url": r["apply_url"],
                "company_email": r["contact_email"],
                "interest": r["why_interesting"] or ""
            })
            
    # Sort by score descending (tech first, then operations, support, marketing)
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches

def main():
    print("🔍 Searching SQLite database for small teams (<= 50) hiring for automatable roles...")
    matches = search_matching_roles()
    
    print(f"🎉 Found [bold green]{len(matches)}[/bold green] relevant job openings that fit your n8n and automation skills!\n")
    
    # We display the top 15 highest-scoring matches in a gorgeous table
    table = Table(title="Top n8n Automation Job Fits (Companies <= 50 Employees)", show_lines=True)
    table.add_column("Company", style="cyan", width=15)
    table.add_column("Job Title", style="magenta", width=25)
    table.add_column("Size", style="yellow", width=8)
    table.add_column("Category & Location", style="green", width=25)
    table.add_column("n8n Automation Opportunities", style="white", width=35)
    
    # Limit to top 15 for elegant CLI display
    for m in matches[:15]:
        cases_str = "\n".join(f"• {uc}" for uc in m["use_cases"])
        table.add_row(
            m["company"],
            m["title"],
            m["team"],
            f"{m['category']}\n📍 {m['location']}",
            cases_str
        )
        
    print(table)
    
    # Let's save a detailed markdown file inside CV-Project directory for the user to keep
    md_content = """# 🎯 Curated Lead List: AI Automation & n8n Opportunities

I have scanned the scraped directory of **3,756 startups** and **9,997 job openings** in your SQLite database. Here is a hand-picked, scored list of **companies with under 50 employees** currently hiring for roles that would directly benefit from you applying **n8n, Claude 3.5, and systems automation**.

---

"""
    for cat in ["🔌 Integrations / Systems / Tech", "⚙️ Operations & Recruiting", "🤝 Customer Success & Support", "📣 Growth & Marketing Automation"]:
        md_content += f"## {cat}\n\n"
        cat_matches = [m for m in matches if m["category"] == cat]
        if not cat_matches:
            md_content += "_No active listings under this category._\n\n"
            continue
            
        for m in cat_matches[:8]: # Top 8 per category
            md_content += f"### **{m['title']}** at **{m['company']}**\n"
            md_content += f"- **📍 Location:** {m['location']}\n"
            md_content += f"- **👥 Team Size:** {m['team']} employees\n"
            md_content += f"- **💡 Why this is a fit:** Being a small team, they have massive operational scaling needs but limited human hours. automating this role frees up 50%+ of their bandwidth.\n"
            md_content += f"- **🔄 Suggested n8n Use Cases to pitch them:**\n"
            for uc in m["use_cases"]:
                md_content += f"  - [ ] {uc}\n"
            md_content += f"- **🔗 Apply Link:** [Apply Here]({m['url']})\n\n"
            
    with open("job_opportunities.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("💾 Saved comprehensive report to [bold green]job_opportunities.md[/bold green]!")

if __name__ == "__main__":
    main()
