# risk_analyzer.py

def analyze_exposure_risk(profile_data: dict, sherlock_data=None):
    """
    Context-aware privacy exposure risk analyzer.

    Risk depends on:
    - What data is exposed
    - Which platform exposes it
    - Cross-platform identity correlation
    """

    score = 0
    exposed = []
    contributions = {}

    if not profile_data:
        return {
            "score": 0,
            "level": "LOW",
            "exposed": [],
            "contributions": {}
        }

    platform = profile_data.get("platform", "unknown")

    # ------------------------------------
    # Platform Weights
    # ------------------------------------

    weights = {
        "linkedin": {
            "name": 0.5,
            "bio": 1,
            "location": 1,
            "company": 0.5,
            "profile_image": 0.5
        },
        "github": {
            "name": 1,
            "bio": 1,
            "location": 1,
            "company": 1,
            "profile_image": 1
        },
        "instagram": {
            "name": 1,
            "bio": 1,
            "location": 2,
            "profile_image": 1
        },
        "default": {
            "name": 1,
            "bio": 1,
            "location": 1,
            "company": 1,
            "profile_image": 1
        }
    }

    platform_weights = weights.get(platform, weights["default"])

    # ------------------------------------
    # Name
    # ------------------------------------

    if profile_data.get("name") or profile_data.get("full_name"):
        value = platform_weights.get("name", 1)
        score += value
        exposed.append("Name")
        contributions["Name"] = value

    # ------------------------------------
    # Bio
    # ------------------------------------

    if profile_data.get("bio"):
        value = platform_weights.get("bio", 1)
        score += value
        exposed.append("Bio")
        contributions["Bio"] = value

    # ------------------------------------
    # Location
    # ------------------------------------

    if profile_data.get("location"):
        value = platform_weights.get("location", 1)
        score += value
        exposed.append("Location")
        contributions["Location"] = value

    # ------------------------------------
    # Company
    # ------------------------------------

    if profile_data.get("company"):
        value = platform_weights.get("company", 1)
        score += value
        exposed.append("Company")
        contributions["Company"] = value

    # ------------------------------------
    # Profile Image Exposure
    # ------------------------------------

    if profile_data.get("profile_image"):
        value = platform_weights.get("profile_image", 1)
        score += value
        exposed.append("Profile Photo")
        contributions["Profile Photo"] = value

    # ------------------------------------
    # Email Exposure
    # ------------------------------------

    if profile_data.get("email"):
        score += 2
        exposed.append("Email")
        contributions["Email"] = 2

    # ------------------------------------
    # Phone Exposure
    # ------------------------------------

    if profile_data.get("phone"):
        score += 3
        exposed.append("Phone")
        contributions["Phone"] = 3

    # ------------------------------------
    # Cross-Platform Correlation Risk
    # ------------------------------------

    if sherlock_data and sherlock_data.get("accounts"):

        total_accounts = len(sherlock_data["accounts"])

        if total_accounts >= 5:
            correlation_score = 2
        elif total_accounts >= 3:
            correlation_score = 1
        else:
            correlation_score = 0

        if correlation_score > 0:
            score += correlation_score
            exposed.append("Cross-Platform Identity Correlation")
            contributions["Cross-Platform Correlation"] = correlation_score

    # ------------------------------------
    # Determine Risk Level
    # ------------------------------------

    if score >= 7:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": round(score, 2),
        "level": level,
        "exposed": exposed,
        "contributions": contributions
    }

