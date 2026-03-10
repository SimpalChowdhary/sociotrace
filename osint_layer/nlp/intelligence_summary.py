# intelligence_summary.py

def generate_summary(username, platform, profile_data, interests, risk, sherlock_data):

    name = profile_data.get("name") or profile_data.get("full_name") or username
    location = profile_data.get("location", "Unknown")

    summary = []

    summary.append(f"Target username '{username}' was analyzed on {platform}.")
    summary.append(f"The profile appears to belong to {name}.")

    if location != "Unknown":
        summary.append(f"The user is located in {location}.")

    # Interests
    if interests:
        interest_text = ", ".join(interests)
        summary.append(f"Detected interests include {interest_text}.")

    # Risk analysis
    summary.append(
        f"The account exposes {len(risk['exposed'])} types of personal information "
        f"resulting in a {risk['level']} privacy risk score."
    )

    # Cross‑platform presence
    if sherlock_data and sherlock_data.get("status") == "success":

        total_accounts = sherlock_data.get("total_found", 0)

        platforms = [
            account["platform"]
            for account in sherlock_data.get("accounts", [])[:10]
        ]

        if platforms:
            platform_text = ", ".join(platforms)

            summary.append(
                f"The same username was identified across {total_accounts} platforms "
                f"including {platform_text}."
            )

    return " ".join(summary)