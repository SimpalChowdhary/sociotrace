def generate_recommendations(profile_data, risk):

    recommendations = []

    if not profile_data:
        return recommendations

    if profile_data.get("name"):
        recommendations.append("Consider limiting full name exposure if privacy is important.")

    if profile_data.get("location"):
        recommendations.append("Avoid sharing precise location publicly to reduce targeted risks.")

    if profile_data.get("company"):
        recommendations.append("Workplace information can be used for phishing attacks. Be cautious.")

    if profile_data.get("bio") and len(profile_data.get("bio")) > 80:
        recommendations.append("Your bio reveals detailed personal info. Consider shortening it.")

    if profile_data.get("profile_image"):
        recommendations.append("Profile photo can be reverse searched. Use generic images if needed.")

    if profile_data.get("public_repos", 0) > 5:
        recommendations.append("Review repositories for sensitive data like API keys or credentials.")

    if risk and risk.get("score", 0) > 6:
        recommendations.append("High exposure detected. Enable 2FA and review privacy settings.")

    return recommendations