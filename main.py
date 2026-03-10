# main.py

from urllib.parse import urlparse
from database import save_full_scan
from osint_layer.sherlock_runner import run_sherlock
from osint_layer.instagram_runner import run_instaloader
from osint_layer.x_api_runner import run_x_api
from osint_layer.github_runner import run_github_api
from osint_layer.nlp.nlp_analyzer import analyze_text
from osint_layer.nlp.interest_detector import detect_interests
from osint_layer.nlp.risk_analyzer import analyze_exposure_risk
from osint_layer.nlp.intelligence_summary import generate_summary
from osint_layer.graph.account_graph import generate_account_graph   # ✅ NEW IMPORT

def extract_username_and_platform(url: str):
    """
    Extract username and domain from URL.
    """
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # ✅ FIXED USERNAME EXTRACTION
    path_parts = [p for p in parsed.path.split("/") if p]
    username = path_parts[-1] if path_parts else ""

    return domain, username


def detect_platform(domain: str):
    """
    Identify platform based on domain.
    """
    if "instagram.com" in domain:
        return "instagram"
    elif "x.com" in domain or "twitter.com" in domain:
        return "twitter"
    elif "github.com" in domain:
        return "github"
    elif "linkedin.com" in domain:
        return "linkedin"
    else:
        return "unknown"


if __name__ == "__main__":

    print("\n========= SOCIOTRACE OSINT ENGINE =========\n")

    # ---- Step 1: Ask User For URL ----
    target_url = input("Enter profile URL to analyze: ").strip()

    if not target_url:
        print("URL cannot be empty.")
        exit()

    # ---- Step 2: Extract Username + Domain ----
    domain, username = extract_username_and_platform(target_url)

    if not username:
        print("Could not extract username.")
        exit()

    print(f"\nDetected Username: {username}")
    print(f"Detected Domain: {domain}")

    # ---- Step 3: Detect Platform ----
    platform = detect_platform(domain)
    print(f"Detected Platform: {platform}")

    # ---- Step 4: Run Sherlock ----
    print("\nRunning cross-platform OSINT (Sherlock)...\n")
    sherlock_data = run_sherlock(username)

    # ---- Step 5: Run Platform-Specific Tool ----
    print("Running platform-specific analysis...\n")

    platform_data = None

    if platform == "instagram":
        platform_data = run_instaloader(username)

    elif platform == "twitter":
        platform_data = run_x_api(username)

    elif platform == "github":
        platform_data = run_github_api(username)

    else:
        print("No specialized tool for this platform.")

    # ---- Step 6: Print Platform Data ----
    if platform_data:
        print("\n===== PLATFORM SPECIFIC DATA =====\n")

        if platform_data["status"] == "success":
            for key, value in platform_data["data"].items():
                print(f"{key}: {value}")
        else:
            print("Error:", platform_data.get("message"))

    # ---- Step 7: NLP Analysis ----
    if platform_data and platform_data.get("status") == "success":

        text_to_analyze = ""

        if "bio" in platform_data["data"]:
            text_to_analyze = platform_data["data"]["bio"]

        elif "headline" in platform_data["data"]:
            text_to_analyze = platform_data["data"]["headline"]

        elif "description" in platform_data["data"]:
            text_to_analyze = platform_data["data"]["description"]

        if text_to_analyze:
            print("\n===== NLP ANALYSIS =====\n")

            nlp_result = analyze_text(text_to_analyze)

            print("Sentiment:", nlp_result["sentiment"])

            print("\nEntities Detected:")
            for ent in nlp_result["entities"]:
                print(f"{ent['text']} -> {ent['label']}")

            # ---- INTEREST DETECTION ----
            print("\n===== INTEREST DETECTION =====\n")

            interests = detect_interests(text_to_analyze)

            if interests:
                for interest in interests:
                    print("-", interest)
            else:
                print("No major interests detected.")

        # ---- RISK ANALYSIS ----
        print("\n===== RISK ANALYSIS =====\n")

        risk = analyze_exposure_risk(platform_data["data"])

        print("Risk Level:", risk["level"])
        print("Risk Score:", risk["score"])

        if risk["exposed"]:
            print("\nExposed Information:")
            for item in risk["exposed"]:
                print("-", item)
        else:
            print("No sensitive information exposed.")

        # ---- INTELLIGENCE SUMMARY ----
        print("\n===== INTELLIGENCE SUMMARY =====\n")

        summary = generate_summary(
            username,
            platform,
            platform_data["data"],
            interests if 'interests' in locals() else [],
            risk,
            sherlock_data
        )

        print(summary)

    # ---- Step 8: Print Sherlock Results ----
    print("\n===== CROSS‑PLATFORM ACCOUNT DISCOVERY =====\n")

    if sherlock_data.get("status") == "success":

        print("Total Accounts Found:", sherlock_data.get("total_found", 0))

        for account in sherlock_data.get("accounts", []):
            print(f"{account['platform']}: {account['url']}")

        # ✅ GENERATE ACCOUNT RELATIONSHIP GRAPH
        generate_account_graph(username, sherlock_data)

    else:
        print("Sherlock failed:", sherlock_data.get("message"))

    # ---- Step 9: Save To MongoDB ----
    save_full_scan(
        target_url,
        username,
        platform,
        platform_data,
        sherlock_data
    )

    print("\n========= ANALYSIS COMPLETE =========\n")