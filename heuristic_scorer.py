import sqlite3
import json
import os

def score_job(job):
    title = job['job_title'].lower()
    why_int = (job['why_interesting'] or '').lower()
    
    score = 0
    reasoning = []
    n8n_pitch = ""
    
    # 1. Direct Tech & Automation Matches (Highest priority)
    if any(k in title for k in ['automation', 'integration', 'systems', 'tools', 'revops', 'workflow']):
        score += 85
        reasoning.append("Direct match for core systems automation and workflow integration.")
        n8n_pitch = "Pitch robust n8n pipelines as a unified integration layer, saving them the overhead of dedicated custom engineering."
        
    # 2. Operations & Chief of Staff (High task automation potential)
    elif any(k in title for k in ['operations', 'ops', 'chief of staff', 'coordinator']):
        score += 80
        reasoning.append("Ops/CoS roles are heavily burdened by manual tool-syncing and operational bottlenecks.")
        n8n_pitch = "Offer to automate cross-platform syncs (e.g. CRM to project management boards) and Slack alert notifications to streamline internal ops."

    # 3. Sales Development / Lead Gen / Sales Ops (Highly repetitive pipelines)
    elif any(k in title for k in ['sdr', 'bdr', 'sales representative', 'lead generation', 'lead gen', 'sales operations']):
        score += 78
        reasoning.append("Sales & lead generation roles involve repetitive prospecting, data enrichment, and list management.")
        n8n_pitch = "Pitch automated lead scoring and enrichment pipelines connecting Apollo/Clay to HubSpot, cutting out manual lead research."

    # 4. Billing / Finance / Bookkeeping / Administrative (Highly prone to manual transcription)
    elif any(k in title for k in ['finance', 'billing', 'bookkeeper', 'reconciliation', 'accountant', 'admin', 'assistant', 'accounting']):
        score += 75
        reasoning.append("Finance and admin tasks are highly manual and easily automatable (invoicing, expense reconciliation, reporting).")
        n8n_pitch = "Pitch automated Stripe-to-accounting syncs, automated invoice generation, and expense tracking webhooks."

    # 5. Customer Success / Support / Helpdesk (Ticket management, tag triage)
    elif any(k in title for k in ['success', 'support', 'cx', 'experience', 'helpdesk', 'client services']):
        score += 72
        reasoning.append("Customer support roles involve repetitive ticket categorization, FAQs, and customer feedback loops.")
        n8n_pitch = "Propose an automated customer support routing workflow that auto-triage tickets via LLMs and drafts draft replies."

    # 6. Recruiting / Talent Acquisition / HR Coordinator
    elif any(k in title for k in ['recruiting', 'talent', 'recruiter', 'hr', 'human resources', 'onboarding']):
        score += 70
        reasoning.append("HR and recruiting coordinators spend hours coordinating calendars, screening resumes, and sending updates.")
        n8n_pitch = "Pitch automated applicant screening filters that flag matching profiles in Slack and send booking links to top candidates."

    # 7. Content / Marketing / Social Media / Copywriter
    elif any(k in title for k in ['growth', 'marketing', 'content', 'seo', 'copywriter', 'social media', 'newsletter', 'creative']):
        score += 65
        reasoning.append("Marketing/Content roles benefit massively from automated multi-platform distribution and content calendars.")
        n8n_pitch = "Offer to build a multi-channel AI content repurposing pipeline that translates single articles into social posts and posts them."

    # 8. Data / Product Analyst
    elif any(k in title for k in ['data', 'product', 'analyst']):
        score += 55
        reasoning.append("Data and product analysts require automated extraction, processing, and data pipeline scheduling.")
        n8n_pitch = "Pitch automated ETL workflows connecting customer interaction APIs to analytics databases."
        
    else:
        score += 35
        reasoning.append("General professional role that can benefit from customized operational automation.")
        n8n_pitch = "Suggest general workflow efficiency blueprints tailored to the department's manual work."

    # Boosts based on company description & intent signals
    if any(k in why_int for k in ['scale', 'fast-growing', 'automate', 'workflow', 'efficiency', 'ai', 'data', 'agile']):
        score += 15
        reasoning.append("Company description points to scaling operations or integration pain points.")
        
    score = min(score, 100)
    
    return {
        "score": score,
        "reasoning": " ".join(reasoning),
        "n8n_pitch": n8n_pitch
    }

def main():
    print("Running Local Heuristic Scorer...")
    
    db_path = r"C:\Users\HP\.gemini\antigravity\scratch\startupmap-scraper\startupmap.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    
    query = """
        SELECT 
            j.job_title,
            s.name as company_name,
            s.team_size_min,
            s.team_size_max,
            s.office_city,
            s.country,
            s.domain_primary,
            s.why_interesting,
            s.stage,
            s.year_founded,
            s.last_funding_amount,
            j.job_location,
            j.apply_url,
            j.contact_email,
            j.type as job_type
        FROM jobs j
        JOIN startups s ON j.startup_id = s.startup_id
        WHERE j.visible = 1
          AND j.contact_email IS NOT NULL AND j.contact_email != ''
          AND (s.team_size_max <= 50 OR (s.team_size_max IS NULL AND s.team_size_min <= 50))
    """
    
    rows = conn.execute(query).fetchall()
    conn.close()
    
    scored_jobs = []
    for r in rows:
        job_dict = dict(r)
        analysis = score_job(job_dict)
        job_dict['score'] = analysis['score']
        job_dict['reasoning'] = analysis['reasoning']
        job_dict['n8n_pitch'] = analysis['n8n_pitch']
        scored_jobs.append(job_dict)
        
    # Sort by score descending
    scored_jobs.sort(key=lambda x: x['score'], reverse=True)
    
    # Filter to unique companies to avoid spamming one company
    seen_companies = set()
    unique_jobs = []
    for j in scored_jobs:
        if j['company_name'] not in seen_companies:
            unique_jobs.append(j)
            seen_companies.add(j['company_name'])
            
    hot_matches = unique_jobs[:30]
    warm_matches = unique_jobs[30:50]
    
    # Write JSON
    output_data = {
        "hot_matches": hot_matches,
        "warm_matches": warm_matches
    }
    with open('semantic_matches.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
        
    # Write Markdown
    md_content = "# Semantic Job Matches (Heuristic Fallback)\n\n"
    md_content += "## Hot Matches (Top 30)\n\n"
    for m in hot_matches:
        team = f"{m['team_size_min'] or 1}-{m['team_size_max'] or 50}"
        md_content += f"### {m['job_title']} at {m['company_name']} (Score: {m['score']})\n"
        md_content += f"- **Email**: {m['contact_email']}\n"
        md_content += f"- **Team Size**: {team}\n"
        md_content += f"- **Location**: {m['job_location'] or m['office_city']}\n"
        md_content += f"- **Reasoning**: {m['reasoning']}\n"
        md_content += f"- **Pitch Angle**: {m['n8n_pitch']}\n\n"
        
    md_content += "## Warm Leads (Next 20)\n\n"
    for m in warm_matches:
        team = f"{m['team_size_min'] or 1}-{m['team_size_max'] or 50}"
        md_content += f"### {m['job_title']} at {m['company_name']} (Score: {m['score']})\n"
        md_content += f"- **Email**: {m['contact_email']} | **Team**: {team}\n"
        md_content += f"- **Reasoning**: {m['reasoning']}\n\n"
        
    with open('semantic_matches.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Scored {len(scored_jobs)} jobs. Wrote 30 hot and 20 warm matches.")

if __name__ == "__main__":
    main()
