# intelligence_summary.py

def generate_summary(username, platform, profile_data, interests, risk, sherlock_data):

    name = profile_data.get("name") or username
    location = profile_data.get("location")

    # Location sentence fix
    if location:
        location_text = f"The user is located in {location}."
    else:
        location_text = "Location information is not publicly available."

    risk_score = risk.get("score", 0)
    risk_level = risk.get("level", "LOW")

    total_accounts = sherlock_data.get("total_found", 0)

    platforms = []

    if sherlock_data.get("accounts"):
        for acc in sherlock_data["accounts"][:10]:
            platforms.append(acc["platform"])

    platform_list = ", ".join(platforms)

    summary = (
        f"Target username '{username}' was analyzed on {platform}. "
        f"The profile appears to belong to {name}. "
        f"{location_text} "
        f"The account exposes {len(risk.get('exposed', []))} types of personal information "
        f"resulting in a {risk_level} privacy risk score. "
        f"The same username was identified across {total_accounts} platforms including {platform_list}."
    )

    return summary