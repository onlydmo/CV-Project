import json
import os
import sys

# Configure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def get_proof_point(title):
    t = title.lower()
    if any(k in t for k in ['marketing', 'growth', 'seo', 'content', 'copywriter']):
        return "I revamped a client's SEO and content architecture, lifting organic search visibility by 35% and saving their content lead about 10 hours a week by automating social publishing."
    elif any(k in t for k in ['finance', 'billing', 'reconciliation', 'accountant', 'admin', 'assistant', 'ops', 'operations', 'coordinator']):
        return "I designed a custom automated booking and dispatch flow using n8n and Google Sheets that cut manual operations overhead by 70% within the first month."
    elif any(k in t for k in ['success', 'support', 'cx', 'experience', 'client']):
        return "I optimized a client's HubSpot CRM pipeline and customer feedback loops, saving their customer success manager over 15 hours a week and leading to a 15% increase in lead conversions."
    else:
        return "I managed beta tester feedback loops for over 100+ users on a platform launch and processed 50+ detailed security and data audits, translating complex technical logs into clean automated alerts."

def main():
    print("Generating Dynamic Outreach Drafts for Top 10 Target Startups...")
    
    intel_path = 'company_intel.json'
    if not os.path.exists(intel_path):
        print(f"Error: {intel_path} not found. Run research_companies.py first.")
        sys.exit(1)
        
    with open(intel_path, 'r', encoding='utf-8') as f:
        companies = json.load(f)
        
    os.makedirs('outreach_drafts', exist_ok=True)
    
    for c in companies:
        name = c['company_name']
        slug = name.lower().replace(' ', '_').replace('.', '')
        title = c['job_title']
        email_addr = c['contact_email']
        domain = c['domain_primary']
        pitch = c['n8n_pitch']
        reasoning = c['reasoning']
        
        web_intel = c.get('web_intel', {})
        hero = web_intel.get('hero_text', '')
        desc = web_intel.get('meta_description', '')
        
        # Determine warm hook
        hook_phrase = f"your work at {name}"
        if hero and len(hero) > 10 and not any(x in hero.lower() for x in ['cookie', 'error', 'page', 'about']):
            hook_phrase = f"your focus on: \"{hero}\""
        elif desc and len(desc) > 15:
            hook_phrase = desc[:80] + "..."
            
        proof = get_proof_point(title)
        
        # Build Blueprint name
        blueprint_name = "workflow automation blueprint"
        if any(k in title.lower() for k in ['marketing', 'growth', 'seo', 'content']):
            blueprint_name = "AI content distribution pipeline blueprint"
        elif any(k in title.lower() for k in ['finance', 'billing', 'reconciliation', 'accountant']):
            blueprint_name = "automated Stripe-to-accounting integration blueprint"
        elif any(k in title.lower() for k in ['success', 'support', 'cx']):
            blueprint_name = "automated ticket routing and LLM triage blueprint"
        elif any(k in title.lower() for k in ['recruiting', 'talent', 'hr']):
            blueprint_name = "automated candidate screening pipeline blueprint"
            
        # ── 1. Write premium decontaminated email sequence ───────────────────
        email_content = f"""Subject: Quick observation regarding {name}'s operations and data pipelines

Hi {name} team,

I was looking at {hook_phrase} and saw you're expanding the team with a {title}.

At a scaling startup (currently {c['team_size_min'] or 1}-{c['team_size_max'] or 50} employees), a major hidden bottleneck is often the manual coordination overhead in your daily workflows. As team sizes grow, copying data between fragmented tools (like your CRM, spreadsheets, and database) eats up hours of your team's bandwidth.

I specialize in building custom, reliable automation layers using n8n and Python. {proof}

I have put together a simple, 2-page {blueprint_name} showing how early-stage teams can securely automate these syncs, saving hours of manual admin. 

Would it be useful if I sent that blueprint over?

Best regards,

[Your Name]
AI Automation & Systems specialist
[Your Portfolio URL]

---
### Follow-up 1 (Day 3): Value Drop
Subject: Re: Quick observation regarding {name}'s operations and data pipelines

Hi {name} team,

Wanted to drop that {blueprint_name} I mentioned. You can view the structure here: [Link to blueprint details].

The core benefit is that it intercepts new triggers (like incoming webhooks) and automatically syncs records across your stack in under 3 minutes, routing failures directly to Slack so your ops are fully self-healing.

Is internal workflow automation currently a focus for your {title} roadmap, or are you prioritizing other scaling bottlenecks right now?

Best,
[Your Name]

---
### Follow-up 2 (Day 7): Case Study
Subject: Re: Quick observation regarding {name}'s operations and data pipelines

Hi {name} team,

By using modular n8n pipelines, I recently RevOps-optimized a client's HubSpot database, which saved their operations team over 15 hours a week and drove a 15% increase in lead conversions.

If your team is feeling the operational squeeze as you scale, I'd love to help.

Would you be open to a quick, 10-minute intro call next Tuesday at 2:00 PM CET?

Best,
[Your Name]

---
### Follow-up 3 (Day 14): Clean Break
Subject: Re: {name} workflow automation

Hi {name} team,

I'm assuming you're currently heads-down on core product features and workflow automation is fully handled.

I'll stop checking in. If you ever need a data pipeline specialist skilled in n8n, API integrations, and LLM-driven agents to automate repetitive tasks in the future, don't hesitate to reach out.

Wishing {name} massive success!

Best,
[Your Name]
"""

        # ── 2. Write 80-word LinkedIn DM ──────────────────────────────────────
        dm_content = f"Hi {name} team, saw you're hiring a {title} to help with your operations. Typically, scaling startups lose hours to manual data syncs between fragmented tools. I build custom n8n data pipelines to automate internal ops, recently saving a client 15+ hours/week. Put together a quick {blueprint_name} showing how to automate this role's manual tasks. Would it be useful if I sent it over? Let me know!"
        
        # Save both files
        with open(f'outreach_drafts/{slug}_email.md', 'w', encoding='utf-8') as f:
            f.write(email_content)
        with open(f'outreach_drafts/{slug}_dm.md', 'w', encoding='utf-8') as f:
            f.write(dm_content)
            
    print(f"\n✓ Successfully generated all dynamic drafts inside CV-Project/outreach_drafts/ for all {len(companies)} startups!")

if __name__ == "__main__":
    main()
