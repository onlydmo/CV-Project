import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import sys
import os
import re

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

PUBLIC_EMAIL_DOMAINS = {
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com',
    'icloud.com', 'zoho.com', 'protonmail.com', 'yandex.com', 'mail.com'
}

def get_domain_from_email(email):
    if not email or '@' not in email:
        return None
    domain = email.split('@')[-1].strip().lower()
    if domain in PUBLIC_EMAIL_DOMAINS:
        return None
    return domain

def scrape_website(domain):
    print(f"Scraping website: {domain}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    
    try:
        url = f"https://{domain}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as response:
            html = response.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        
        # Get meta description
        meta_desc = ""
        meta = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
        if meta:
            meta_desc = meta.get('content', '').strip()
            
        # Get hero/header text
        h1s = [h.get_text().strip() for h in soup.find_all('h1') if h.get_text().strip()]
        hero_text = h1s[0] if h1s else ""
        
        # Get first few paragraphs
        paragraphs = []
        for p in soup.find_all('p'):
            text = p.get_text().strip()
            if len(text) > 40 and not any(x in text.lower() for x in ['cookie', 'privacy', 'terms', 'subscribe']):
                paragraphs.append(text)
                if len(paragraphs) >= 2:
                    break
                    
        return {
            "hero_text": hero_text,
            "meta_description": meta_desc,
            "snippet": " | ".join(paragraphs)
        }
    except Exception as e:
        print(f"Error scraping {domain}: {e}")
        return {
            "hero_text": "",
            "meta_description": "",
            "snippet": "Could not retrieve website content automatically."
        }

def get_recent_news(company_name):
    print(f"Searching recent news for: {company_name}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    query = urllib.parse.quote(f"{company_name} startup news")
    url = f"https://html.duckduckgo.com/html/?q={query}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as response:
            html = response.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        # Parse DDG html results
        for a in soup.find_all('a', class_='result__snippet'):
            text = a.get_text().strip()
            title_node = a.find_parent('div', class_='result__body')
            title = ""
            if title_node:
                title_a = title_node.find('a', class_='result__url')
                if title_a:
                    title = title_a.get_text().strip()
            
            if title and text:
                results.append(f"\"{title}\" - {text[:150]}...")
                if len(results) >= 2:
                    break
                    
        return results
    except Exception as e:
        print(f"Error fetching news for {company_name}: {e}")
        return ["No recent news articles retrieved automatically."]

def main():
    print("🚀 Initializing Email-Prioritized Company Intel Research...")
    
    if not os.path.exists('semantic_matches.json'):
        print("Error: semantic_matches.json not found. Run heuristic_scorer.py first.")
        sys.exit(1)
        
    with open('semantic_matches.json', 'r', encoding='utf-8') as f:
        matches = json.load(f)
        
    hot = matches.get('hot_matches', [])
    if not hot:
        print("No hot matches found.")
        sys.exit(1)
        
    selected_companies = hot[:10]
    print(f"Gathering intel for top {len(selected_companies)} companies...")
    
    intel_reports = []
    for c in selected_companies:
        name = c['company_name']
        title = c['job_title']
        email = c['contact_email']
        
        print(f"\n--- Researching {name} ---")
        
        # Prioritize email domain over DDG search fallback
        email_domain = get_domain_from_email(email)
        if email_domain:
            domain = email_domain
            print(f"Using domain extracted from contact email: {domain}")
        else:
            domain = name.lower().replace(' ', '') + '.com'
            print(f"No valid email domain found. Using fallback: {domain}")
            
        c['domain_primary'] = domain
        
        web_data = scrape_website(domain)
        news = get_recent_news(name)
        
        c['web_intel'] = web_data
        c['news_intel'] = news
        intel_reports.append(c)
        
    # Save the intel reports
    with open('company_intel.json', 'w', encoding='utf-8') as f:
        json.dump(intel_reports, f, indent=2)
        
    # Generate human-friendly markdown report
    md = "# Company Research & Intel Reports\n\n"
    for r in intel_reports:
        team = f"{r['team_size_min'] or 1}-{r['team_size_max'] or 50}"
        md += f"## 🏢 {r['company_name']}\n"
        md += f"- **Target Role**: {r['job_title']}\n"
        md += f"- **Contact Email**: {r['contact_email']}\n"
        md += f"- **Website**: [{r['domain_primary']}](https://{r['domain_primary']})\n"
        md += f"- **Team Size**: {team} employees | **Stage**: {r['stage'] or 'Unknown'} | **Location**: {r['job_location'] or r['office_city']}\n\n"
        
        md += "### 🌐 Website Intel\n"
        if r['web_intel']['hero_text']:
            md += f"- **Hero Headline**: *\"{r['web_intel']['hero_text']}\"*\n"
        if r['web_intel']['meta_description']:
            md += f"- **Description**: {r['web_intel']['meta_description']}\n"
        if r['web_intel']['snippet']:
            md += f"- **Content Extract**: {r['web_intel']['snippet']}\n"
        md += "\n"
        
        md += "### 📰 Recent News & Activity\n"
        for item in r['news_intel']:
            md += f"- {item}\n"
        md += "\n"
        
        md += "### 💡 Suggested Warm Opener & n8n Use Case\n"
        md += f"- **Reasoning**: {r['reasoning']}\n"
        md += f"- **Suggested Approach**: {r['n8n_pitch']}\n"
        md += f"- **Personalized Opener**: \"Hi {r['company_name']} team, saw you're hiring a {r['job_title']} to help with {r['web_intel']['hero_text'] or 'your operations'}. As an AI Automation specialist, I help teams like yours save 20+ hours a week by connecting tools like your CRM/Notion via n8n workflows...\"\n\n"
        md += "---\n\n"
        
    with open('company_intel.md', 'w', encoding='utf-8') as f:
        f.write(md)
        
    print("\n✓ Research completed successfully. Wrote company_intel.md and company_intel.json.")

if __name__ == "__main__":
    main()
