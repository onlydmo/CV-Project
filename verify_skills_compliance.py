import os
import sys

# Configure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BANNED_AI_WORDS = {
    'delve', 'synergy', 'robust', 'comprehensive', 'game-changing', 
    'revolutionize', 'landscape', 'cutting-edge', 'streamline', 
    'seamless', 'holistic', 'leverage', 'testament'
}

def audit_draft(email_path, dm_path):
    issues = []
    score = 100
    
    # Audit DM
    with open(dm_path, 'r', encoding='utf-8') as f:
        dm_content = f.read()
    dm_word_count = len(dm_content.split())
    if dm_word_count > 80:
        issues.append(f"DM exceeds 80-word limit ({dm_word_count} words)")
        score -= 20
        
    # Audit Email
    with open(email_path, 'r', encoding='utf-8') as f:
        email_content = f.read()
    
    # Check for AI decontamination signatures
    found_banned = [w for w in BANNED_AI_WORDS if w in email_content.lower() or w in dm_content.lower()]
    if found_banned:
        issues.append(f"AI fingerprints detected: {', '.join(found_banned)}")
        score -= 15 * len(found_banned)
        
    # Check for Soft CTA
    if "?" not in email_content.split("Best regards")[0]:
        issues.append("Email lacks an interest-based soft CTA (question mark)")
        score -= 15
        
    # Check for Hard Numbers (Prove It Sweep)
    has_numbers = any(char.isdigit() for char in email_content)
    if not has_numbers:
        issues.append("Lacks hard proof points (numbers/percentages)")
        score -= 15
        
    return score, issues, dm_word_count

def main():
    print("--------------------------------------------------")
    print("🔍 RUNNING AUTOMATED SKILLS COMPLIANCE AUDIT...")
    print("--------------------------------------------------")
    
    drafts_dir = 'outreach_drafts'
    if not os.path.exists(drafts_dir):
        print("Error: outreach_drafts directory not found.")
        sys.exit(1)
        
    files = os.listdir(drafts_dir)
    companies = set(f.split('_')[0] for f in files if f.endswith('.md') and f != 'linkedin_boolean_searches.md')
    
    total_score = 0
    count = 0
    
    for c in sorted(companies):
        email_file = os.path.join(drafts_dir, f"{c}_email.md")
        dm_file = os.path.join(drafts_dir, f"{c}_dm.md")
        
        # Handle cases where naming convention differs slightly
        if not os.path.exists(email_file) or not os.path.exists(dm_file):
            continue
            
        score, issues, dm_words = audit_draft(email_file, dm_file)
        score = max(score, 0)
        total_score += score
        count += 1
        
        status = "✅ PASSED" if score >= 85 else "⚠️ WARNING"
        print(f"🏢 {c.upper().replace('_', ' ')}")
        print(f"  - Compliance Score: {score}/100 [{status}]")
        print(f"  - LinkedIn DM Word Count: {dm_words} words (Limit: 80)")
        if issues:
            print("  - Issues Found:")
            for issue in issues:
                print(f"    • {issue}")
        else:
            print("  - Decontamination: 100% human voice. Zero AI fingerprints.")
        print("-" * 50)
        
    avg = total_score / count if count > 0 else 0
    print(f"\n🎯 OVERALL PIPELINE COMPLIANCE AVERAGE: {avg:.1f}/100")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()
