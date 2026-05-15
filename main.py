from urllib.parse import urlparse
from database import save_full_scan

from osint_layer.sherlock_runner import run_sherlock
from osint_layer.instagram_runner import run_instaloader
from osint_layer.github_runner import run_github_api
from osint_layer.linkedin_runner import run_linkedin

from osint_layer.nlp.nlp_analyzer import analyze_text
from osint_layer.nlp.interest_detector import detect_interests
from osint_layer.nlp.risk_analyzer import analyze_exposure_risk
from osint_layer.nlp.intelligence_summary import generate_summary
from osint_layer.nlp.recommendation_engine import generate_recommendations

from osint_layer.graph.account_graph import generate_account_graph
from osint_layer.image_analyzer import analyze_profile_images


def classify_account_type(profile_data):

    text = " ".join([
        str(profile_data.get("bio", "")),
        str(profile_data.get("name", "")),
        str(profile_data.get("company", "")),
        str(profile_data.get("location", "")),
    ]).lower()

    if any(word in text for word in ["ceo", "founder", "company", "inc", "ltd", "microsoft", "foundation"]):
        return "Business / Professional"

    elif any(word in text for word in ["developer", "engineer", "software", "github", "python"]):
        return "Tech / Developer"

    return "General User"


def extract_username_and_platform(url: str):

    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    path_parts = [p for p in parsed.path.split("/") if p]
    username = path_parts[-1] if path_parts else ""

    return domain, username


def detect_platform(domain: str):

    if "instagram.com" in domain:
        return "instagram"
    elif "github.com" in domain:
        return "github"
    elif "linkedin.com" in domain:
        return "linkedin"
    else:
        return "unknown"


def run_osint_pipeline(profile_url):

    domain, username = extract_username_and_platform(profile_url)

    if not username:
        return {"error": "Username extraction failed"}

    platform = detect_platform(domain)

    sherlock_data = run_sherlock(username)

    platform_data = None

    if platform == "instagram":
        platform_data = run_instaloader(username)
    elif platform == "github":
        platform_data = run_github_api(username)
    elif platform == "linkedin":
        platform_data = run_linkedin(username)

    interests = []
    nlp_result = None
    risk = None
    recommendations = []
    summary = ""
    account_type = "Unknown"

    if platform_data:

        if isinstance(platform_data, dict) and platform_data.get("data"):
            profile_data = platform_data["data"]
        else:
            profile_data = platform_data

        # ✅ FIX NUMERIC CRASH
        profile_data["public_repos"] = profile_data.get("public_repos") or 0
        profile_data["followers"] = profile_data.get("followers") or 0
        profile_data["following"] = profile_data.get("following") or 0

        account_type = classify_account_type(profile_data)

        text = profile_data.get("bio") or ""

        if text:
            nlp_result = analyze_text(text)
            interests = detect_interests(text)

        risk = analyze_exposure_risk(profile_data)
        recommendations = generate_recommendations(profile_data, risk)

        summary = generate_summary(
            username,
            platform,
            profile_data,
            interests,
            risk,
            sherlock_data
        )

    graph_path = None
    if sherlock_data and sherlock_data.get("accounts"):
        graph_path = generate_account_graph(username, sherlock_data)

    image_analysis = analyze_profile_images(
        platform_data if platform == "github" else None,
        platform_data if platform == "linkedin" else None,
        platform_data if platform == "instagram" else None
    )

    save_full_scan(profile_url, username, platform, platform_data, sherlock_data)

    # 🔥 ONLY FIXED PART (ATTACKER VIEW)
    attacker_view = []
    if platform_data and risk:
        attacker_view = generate_attacker_view(profile_data, risk)

    return {
        "username": username,
        "platform": platform,
        "platform_data": platform_data,
        "sherlock": sherlock_data,
        "nlp": nlp_result,
        "interests": interests,
        "risk": risk,
        "summary": summary,
        "image_analysis": image_analysis,
        "recommendations": recommendations,
        "account_type": account_type,
        "attacker_view": attacker_view,
        "graph": graph_path
    }


# 🔥 ONLY UPDATED FUNCTION
def generate_attacker_view(profile_data, risk):

    attacks = []

    if not profile_data or not risk:
        return ["No immediate attack vectors detected"]

    exposed = risk.get("exposed", [])

    if "Name" in exposed:
        attacks.append("Real name can be used for identity correlation across platforms.")

    if "Location" in exposed:
        attacks.append("Location can enable targeted phishing or physical tracking.")

    if "Company" in exposed:
        attacks.append("Company info can be used for spear phishing or impersonation attacks.")

    if "Profile Photo" in exposed:
        attacks.append("Profile image can be reverse searched to uncover more accounts.")

    if "Public Repos" in exposed or profile_data.get("public_repos", 0) > 0:
        attacks.append("Public repositories may expose sensitive code or credentials.")

    if not attacks:
        attacks.append("Low exposure reduces immediate attack surface.")

    return attacks


if __name__ == "__main__":
    print("\n========= SOCIOTRACE OSINT ENGINE =========\n")
    url = input("Enter profile URL to analyze: ").strip()
    result = run_osint_pipeline(url)
    print(result)