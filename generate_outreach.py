import os
import json

def generate_flexion_drafts():
    email = """Subject: Quick observation regarding Flexion's robot ops pipeline

Hi Flexion team,

I was looking at your work building complex intelligence for simple human tasks and saw you're expanding the team with a Product Manager for Developer Tools. 

With a small, highly technical team of scientists and roboticists, a major bottleneck is often the manual overhead in your developer feedback loops and internal release pipelines. 

In my previous roles, I managed feedback loops for over 100+ beta testers and processed 50+ security audits by automating pipeline notifications and syncing testing states across internal tools. This cut manual coordination overhead by roughly 70%.

I've put together a simple, 3-step automation blueprint showing how early-stage robotics teams can use lightweight n8n workflows to connect testing simulators, Jira, and Slack alert chains automatically. 

Would it be useful if I sent that blueprint over?

Best regards,

[Your Name]
AI Automation & Systems specialist
[Your Portfolio URL]

---
### Follow-up 1 (Day 3): Value Drop
Subject: Re: Flexion developer feedback loop blueprint

Hi Flexion team,

Wanted to drop that 3-step automation blueprint I mentioned. You can view the workflow structure here: [Link to n8n workflow image/mockup].

The core benefit is that it intercepts testing failures via webhooks and automatically routes detailed error logs to the specific developer who pushed the commit, bypassing manual triage entirely.

Is developer workflow automation currently a priority for your dev tools roadmap, or are you focused on other scaling bottlenecks right now?

Best,
[Your Name]

---
### Follow-up 2 (Day 7): Case Study / Proof Point
Subject: Re: Flexion developer feedback loop blueprint

Hi Flexion team,

To give you a quick example of this in action: I recently helped an ops-heavy team optimize their CRM and developer pipelines, leading to a 15% improvement in their lead conversion rate and saving their engineering lead about 12 hours a week of manual coordination.

If you're facing similar coordination friction as you scale to 50 employees in Zurich, I'd love to chat.

Would you be open to a brief, 10-minute intro call next Thursday at 2:00 PM CET?

Best,
[Your Name]

---
### Follow-up 3 (Day 14): Clean Break
Subject: Re: Flexion developer feedback loops

Hi Flexion team,

I'm assuming you're currently heads-down scaling the robotics intelligence platform and dev tools are fully covered. 

I'll stop checking in. If you ever need to connect your internal tool stack or automate repetitive operational tasks to save your team's bandwidth down the line, feel free to reach out.

Wishing Flexion the best in Zurich!

Best,
[Your Name]
"""

    dm = """Hi Flexion team, saw you're building complex intelligence for simple human tasks and hiring a PM for Developer Tools. Typically, early-stage robotics teams lose hours in manual dev pipeline coordination. I previously managed feedback loops for 100+ testers by automating internal syncs. Put together a 3-step automation blueprint for robotics dev workflows — would it be useful if I sent it over? Let me know!"""
    
    return email, dm

def generate_dreamdata_drafts():
    email = """Subject: Dreamdata intent signals + internal tool syncs

Hi Dreamdata team,

I was reading about Dreamdata's platform empowering B2B marketers to activate precise audiences and leverage AI intent signals, and saw you're hiring an Automation Engineer for Commercial Systems.

As a platform that thrives on connecting intent data to downstream marketing actions, you know how crucial integration speed is. But internally, syncing GTM systems (like Salesforce, HubSpot, and Slack) can quickly become a manual, brittle bottleneck for your sales teams.

I specialize in building custom n8n automation layers that connect CRM pipelines and GTM stacks. For example, I optimized HubSpot CRM pipelines at a scaling systems company, saving their ops lead 15+ hours a week and leading to a 15% lift in lead conversion.

I put together a quick, 2-page operations guide on how B2B SaaS teams use n8n and LLM agents to automatically trigger high-value Slack alerts and routing rules when a high-intent prospect matches specific web intent signals.

Would it be useful if I sent that guide over?

Best regards,

[Your Name]
AI Automation & Systems specialist
[Your Portfolio URL]

---
### Follow-up 1 (Day 3): Value Drop
Subject: Re: Dreamdata intent signals + internal tool syncs

Hi Dreamdata team,

Here is the GTM routing and alert guide I mentioned: [Link to Operations Guide]. 

The guide highlights how to use conditional n8n webhooks to enrich incoming lead domains in real-time, routing hot opportunities directly to AEs within 3 minutes of an intent trigger.

Are internal systems syncs currently a primary focus for your commercial ops, or are you prioritizing other bottlenecks?

Best,
[Your Name]

---
### Follow-up 2 (Day 7): Case Study
Subject: Re: Dreamdata intent signals + internal tool syncs

Hi Dreamdata team,

Just to share some quick results: I recently designed an automated booking and dispatch flow that achieved a 70% reduction in booking ops overhead, proving that smart systems automation scales productivity without premature hiring.

If your team in Copenhagen is feeling the operational squeeze of syncing attribution data to GTM tools, I'd love to help.

Are you open to a quick, 10-minute chat next Wednesday at 10:00 AM CET?

Best,
[Your Name]

---
### Follow-up 3 (Day 14): Clean Break
Subject: Re: Dreamdata systems syncs

Hi Dreamdata team,

I'm assuming commercial systems automation is fully handled internally at the moment. 

I'll stop checking in. If you ever need to connect complex APIs or build custom, error-resilient n8n pipelines for your GTM tools in the future, feel free to reach out.

Best of luck driving B2B revenue!

Best,
[Your Name]
"""

    dm = """Hi Dreamdata team, love how you're helping marketers activate precise audiences with AI intent signals. Saw you're hiring an Automation Engineer for Commercial Systems. I build custom n8n automation layers for CRM pipelines, recently saving an ops lead 15 hours/week. Put together a 2-page guide on automating high-value sales alerts from GTM intent triggers. Would it be useful to send over? Let me know!"""
    
    return email, dm

def generate_borndigital_drafts():
    email = """Subject: Birth of Born Digital's integration pipelines

Hi Born Digital team,

I was looking at your Enterprise AI Workforce platform and saw you're hiring an Integration Engineer. Congratulations on being recognized by Gartner in the 2025 Market Guide for Digital Humans!

When you're deploying AI employees and digital humans across voice, chat, and support channels, the custom API integration pipelines connecting to your clients' legacy CRMs are often the slowest part of the delivery process.

I specialize in building reliable integration layers using n8n and custom webhook routers to connect LLMs and conversational agents to legacy systems like HubSpot, Zendesk, and SQL databases. I recently managed platform launches and feedback loops for over 100+ beta testers, ensuring zero-latency communication sync.

I put together a quick, 1-page system architecture diagram showing how to build an error-resilient webhook listener in n8n that automatically retries and handles API failures when syncing AI-generated customer transcripts to downstream client databases.

Would it be useful if I sent that diagram over?

Best regards,

[Your Name]
AI Automation & Systems specialist
[Your Portfolio URL]

---
### Follow-up 1 (Day 3): Value Drop
Subject: Re: Birth of Born Digital's integration pipelines

Hi Born Digital team,

Here is the system architecture diagram I mentioned: [Link to Integration Diagram].

It demonstrates a modular approach to handling API timeouts by queuing requests in a secondary cache and automatically alert-routing exceptions to Slack, ensuring your client integration remains highly reliable.

Are custom API integrations for AI deployment currently a bottleneck for your onboarding, or are you fully automated there?

Best,
[Your Name]

---
### Follow-up 2 (Day 7): Case Study
Subject: Re: Birth of Born Digital's integration pipelines

Hi Born Digital team,

To give you an idea of the speed of these deployments: I recently automated a client's booking workflow, resulting in a 70% reduction in operational dispatch time. I also scale organic growth by setting up automated SEO architectures, recently lifting organic visibility by 35%.

If you need a reliable hand in Prague to build out client integration pipelines fast, I'd love to help.

Would you be open to a 10-minute intro call next Tuesday at 3:00 PM CET?

Best,
[Your Name]

---
### Follow-up 3 (Day 14): Clean Break
Subject: Re: Born Digital integration pipelines

Hi Born Digital team,

I'm assuming your client integration queues are fully sorted for now.

I'll stop checking in. If you ever need an integration engineer skilled in n8n, webhooks, and conversational AI pipelines to accelerate your AI employee deployments, feel free to drop me a line.

Keep up the great work scaling the conversational AI workforce!

Best,
[Your Name]
"""

    dm = """Hi Born Digital team, congrats on the Gartner 2025 recognition for Digital Humans! Saw you're hiring an Integration Engineer. I specialize in building custom API integration layers and webhook routers to connect LLMs to CRMs using n8n. Put together a 1-page error-resilient system diagram showing how to queue and retry failed customer transcript syncs. Would it be useful if I sent it over? Let me know!"""
    
    return email, dm

def generate_wobby_drafts():
    email = """Subject: n8n connectivity & custom API integrations for Wobby

Hi Wobby team,

I was looking at your context-aware AI data analyst and saw you're hiring a Senior Engineering Manager for Connectivity and Integrations. 

For a platform enabling trusted conversational data analytics, building and maintaining robust connectivity pipelines to external data sources (Notion, HubSpot, SQL, files) is the core product driver. But standard connectors are often brittle and slow down the engineering queue.

I specialize in building flexible, modular integration architectures using n8n and Python to connect AI models to disparate database APIs. I previously managed over 50+ data audits and security reviews, translating complex technical inputs into clean, structured datasets and automated reporting loops.

I drafted a simple, 2-page integration blueprint showing how SaaS platforms can expose a secure, user-managed webhook gateway via n8n to fetch external database context dynamically for LLMs.

Would it be useful if I sent that blueprint over?

Best regards,

[Your Name]
AI Automation & Systems specialist
[Your Portfolio URL]

---
### Follow-up 1 (Day 3): Value Drop
Subject: Re: n8n connectivity & custom API integrations for Wobby

Hi Wobby team,

Here is the integration blueprint I mentioned: [Link to Webhook Gateway Blueprint].

The architecture maps out a zero-trust model where incoming client data queries are securely sanitized, run through n8n connectivity nodes, and converted to vector-compatible JSON for your AI analyst.

Is expanding source connectors currently a primary scaling bottleneck for your engineering team, or are you focused elsewhere?

Best,
[Your Name]

---
### Follow-up 2 (Day 7): Case Study
Subject: Re: n8n connectivity & custom API integrations for Wobby

Hi Wobby team,

By using modular automation pipelines, I recently cut booking operational overhead by 70% for a client. I also RevOps-optimized their HubSpot CRM database, resulting in a 15% increase in lead conversions by automating manual data syncs.

If your team in Antwerp needs an expert in connectivity, n8n workflows, and data orchestration to speed up your integration roadmap, I'd love to contribute.

Would you be open to a 10-minute intro call next Thursday at 11:00 AM CET?

Best,
[Your Name]

---
### Follow-up 3 (Day 14): Clean Break
Subject: Re: Wobby source connectors

Hi Wobby team,

I'm assuming the connectivity engineering team is fully staffed and on track.

I'll stop checking in. If you ever need an integration systems specialist to build secure, context-aware source connectors or automate internal dev pipelines in the future, don't hesitate to reach out.

Wishing Wobby massive success democratizing data analytics!

Best,
[Your Name]
"""

    dm = """Hi Wobby team, saw you're building a context-aware AI data analyst and hiring a Senior Engineering Manager for Connectivity. I specialize in building modular API integration pipelines to connect database sources to LLMs using n8n. Put together a 2-page blueprint mapping a secure, user-managed webhook gateway for external sources. Would it be useful to send that blueprint over? Let me know!"""
    
    return email, dm

def generate_airmo_drafts():
    email = """Subject: Satellite data pipelines & alert automation for AIRMO

Hi AIRMO team,

I was reading about AIRMO's satellite and drone-mounted optical sensors making methane compliance easy, and saw you're hiring a LiDAR/Calibration/Validation Engineer.

When handling high-frequency satellite imaging and leak detection down to 1 g/h, building real-time alert pipelines that instantly notify oil/gas operators of leaks is critical. If your sensor data is siloed or manual verification is needed, the speed-to-resolution degrades.

I specialize in building real-time data pipelines using n8n, custom webhooks, and Python. I previously designed system-wide automated syncs for high-reliability applications, managing over 50+ detailed audits and processing complex technical datasets into clear, actionable alerting workflows.

I put together a simple system architecture map showing how to build an automated methane leak alert pipeline using n8n. It automatically triggers when satellite sensor thresholds are breached, generates a localized leak report, and routes it directly to field operators via SMS and Slack.

Would it be useful if I sent that map over?

Best regards,

[Your Name]
AI Automation & Systems specialist
[Your Portfolio URL]

---
### Follow-up 1 (Day 3): Value Drop
Subject: Re: Satellite data pipelines & alert automation for AIRMO

Hi AIRMO team,

Here is the methane leak alerting architecture map I mentioned: [Link to Alert Pipeline Map].

It illustrates how to ingest streaming sensor data, run anomaly detection, and use n8n conditional routers to escalate critical leaks in under 3 minutes while suppressing duplicate warnings.

Are real-time data orchestration pipelines a priority for your optical sensor deployments right now, or are you fully automated there?

Best,
[Your Name]

---
### Follow-up 2 (Day 7): Case Study
Subject: Re: Satellite data pipelines & alert automation for AIRMO

Hi AIRMO team,

To give you an idea of the efficiency: I previously designed an automated ops workflow that cut manual coordination overhead by 70%, and revamped a HubSpot CRM database that lifted conversions by 15% by syncing stale lead accounts automatically.

If you need a systems automation specialist in Berlin to help orchestrate your satellite and drone telemetry pipelines, I'd love to connect.

Would you be open to a 10-minute intro call next Wednesday at 4:00 PM CET?

Best,
[Your Name]

---
### Follow-up 3 (Day 14): Clean Break
Subject: Re: AIRMO sensor alerting pipelines

Hi AIRMO team,

I'm assuming your telemetry and leak alerting pipelines are running smoothly.

I'll stop checking in. If you ever need a data pipeline specialist skilled in n8n, webhook alerting, and system-wide database integrations, feel free to reach out.

Keep up the outstanding work protecting the climate with satellite sensor tech!

Best,
[Your Name]
"""

    dm = """Hi AIRMO team, love how you're using drone and satellite sensors to track methane leaks. Saw you're hiring a LiDAR Calibration Engineer. I build custom real-time data pipelines using n8n and Python. Put together a system architecture map showing how to automate a 3-minute leak alerting flow from sensor triggers to field operator Slack/SMS notifications. Would it be useful to send that map over? Let me know!"""
    
    return email, dm

def main():
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
            
    print("Generating Cold Outreach Drafts (5-Skill Chain)...")
    
    os.makedirs('outreach_drafts', exist_ok=True)
    
    # Define generation map
    generators = {
        'flexion': generate_flexion_drafts,
        'dreamdata': generate_dreamdata_drafts,
        'borndigital': generate_borndigital_drafts,
        'wobby': generate_wobby_drafts,
        'airmo': generate_airmo_drafts
    }
    
    csv_data = []
    
    for slug, gen in generators.items():
        print(f"Generating drafts for {slug}...")
        email, dm = gen()
        
        # Write separate files
        with open(f'outreach_drafts/{slug}_email.md', 'w', encoding='utf-8') as f:
            f.write(email)
        with open(f'outreach_drafts/{slug}_dm.md', 'w', encoding='utf-8') as f:
            f.write(dm)
            
        csv_data.append({
            "Company": slug.capitalize(),
            "Email": email.split('\n')[0].replace('Subject: ', ''),
            "LinkedIn DM": dm
        })
        
    # Write LinkedIn Boolean search strings
    boolean_content = """# LinkedIn Boolean Search Strings (Manual Paste)

Copy and paste these search strings into the LinkedIn search bar, click the **Posts** tab, and filter by **Date Posted: Past Week** or **Past 24 Hours** to find hidden job postings!

## Integrations & AI Automation
```
"hiring" AND ("n8n" OR "automation" OR "zapier" OR "workflows") AND ("contract" OR "freelance" OR "consultant")
```

## Operations & Systems
```
"seeking" AND "operations" AND "automation" AND ("startup" OR "early-stage")
```

## Customer Success & CRM
```
"looking for" AND ("customer success" OR "support") AND "automation" AND "HubSpot"
```

## Growth & Content pipelines
```
"hiring" AND ("seo" OR "content" OR "marketing") AND ("automation" OR "ai" OR "workflow")
```

---

# The 3-Message Outreach Flow (Reddit / Communities)

Use this flow to convert leads in communities (like r/startups or Indie Hackers) without sounding transactional.

### Message 1: The Value Drop (Day 1)
> "Hi [Name], saw your post about struggling with [Specific Problem]. I actually just solved this for a scaling platform by building a lightweight n8n workflow that connects [Tool A] to [Tool B] automatically. Put together a quick 1-page PDF showing the exact blueprint if it helps — want me to send it over?"
*   **Goal:** Get a "Yes, please send it." Builds high reciprocity.

### Message 2: Delivery & Soft Probe (Day 2)
> "Here is the blueprint link: [Link]. The trickiest part is usually setting up the webhook error-handling loops so it doesn't drop requests. Are you guys building this internally or looking for a hand to set it up?"
*   **Goal:** Qualify hiring intent.

### Message 3: The Pitch (Day 5)
> "Hey [Name], assuming you're swamped. If you need someone to just take this off your plate entirely and ship it within the week, this is exactly what I do. Open to a quick, 10-minute chat next week?"
*   **Goal:** Book the call.
"""
    
    with open('outreach_drafts/linkedin_boolean_searches.md', 'w', encoding='utf-8') as f:
        f.write(boolean_content)
        
    print("\n✓ Generated all drafts and LinkedIn strings inside CV-Project/outreach_drafts/.")

if __name__ == "__main__":
    main()
