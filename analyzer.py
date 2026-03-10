# analyzer.py
import re

def analyze_exposure(profile_data):
    bio = profile_data.get("bio", "") or ""

    exposure = {
        "email_exposed": False,
        "phone_exposed": False,
        "location_exposed": False,
        "profession_exposed": False,
        "cross_platform_links": []
    }

    # Email detection
    if re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", bio):
        exposure["email_exposed"] = True

    # Phone detection
    if re.search(r"\+?\d[\d\s\-]{7,}\d", bio):
        exposure["phone_exposed"] = True

    # Location detection (basic keywords for demo)
    locations = ["india", "usa", "london", "hyderabad", "new york"]
    for loc in locations:
        if loc.lower() in bio.lower():
            exposure["location_exposed"] = True
            break

    # Profession detection
    professions = ["engineer", "developer", "student", "founder", "designer"]
    for p in professions:
        if p.lower() in bio.lower():
            exposure["profession_exposed"] = True
            break

    # Cross-platform links
    for link in profile_data.get("links", []):
        if "github.com" in link or "linkedin.com" in link:
            exposure["cross_platform_links"].append(link)

    return exposure
