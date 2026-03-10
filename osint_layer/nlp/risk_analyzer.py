# risk_analyzer.py

def analyze_exposure_risk(profile_data: dict):
    """
    Calculate risk score based on how much personal information
    is publicly exposed in the profile.
    """

    score = 0
    exposed = []

    if not profile_data:
        return {"score": 0, "level": "LOW", "exposed": []}

    # Name
    if profile_data.get("name") or profile_data.get("full_name"):
        score += 1
        exposed.append("Name")

    # Bio / Description
    if profile_data.get("bio"):
        score += 1
        exposed.append("Bio")

    # Location
    if profile_data.get("location"):
        score += 1
        exposed.append("Location")

    # Company
    if profile_data.get("company"):
        score += 1
        exposed.append("Company")

    # Email
    if profile_data.get("email"):
        score += 2
        exposed.append("Email")

    # Website
    if profile_data.get("website"):
        score += 1
        exposed.append("Website")

    # Phone
    if profile_data.get("phone"):
        score += 3
        exposed.append("Phone")

    # Determine risk level
    if score >= 6:
        level = "HIGH"
    elif score >= 3:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "score": score,
        "level": level,
        "exposed": exposed
    }