# x_api_runner.py

import requests

# 🔐 IMPORTANT:
# Replace this with your actual Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALTh7wEAAAAATvCpdHxlIRLDOE55BU2vu9ChQAo%3DdXS3cXCM9SJ6TZ4WMgcdv3AdjArW8MY3oSD7HSTYE039gALW2Q"


def run_x_api(username: str) -> dict:
    """
    Fetch basic X (Twitter) profile info using Official X API v2.
    Compatible with Free Tier.
    """

    url = (
        f"https://api.twitter.com/2/users/by/username/{username}"
        "?user.fields=description,public_metrics,verified"
    )

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)

        # ✅ Success
        if response.status_code == 200:
            user = response.json().get("data", {})

            data = {
                "username": user.get("username"),
                "display_name": user.get("name"),
                "bio": user.get("description", ""),
                "followers": user.get("public_metrics", {}).get("followers_count", 0),
                "following": user.get("public_metrics", {}).get("following_count", 0),
                "tweets": user.get("public_metrics", {}).get("tweet_count", 0),
                "verified": user.get("verified", False),
            }

            return {
                "tool": "official_x_api",
                "status": "success",
                "data": data
            }

        # ⚠ Rate limit
        elif response.status_code == 429:
            return {
                "tool": "official_x_api",
                "status": "error",
                "message": "Rate limit exceeded (Free Tier monthly limit reached)"
            }

        # ❌ User not found
        elif response.status_code == 404:
            return {
                "tool": "official_x_api",
                "status": "error",
                "message": "User not found"
            }

        # ❌ Unauthorized (wrong token)
        elif response.status_code == 401:
            return {
                "tool": "official_x_api",
                "status": "error",
                "message": "Unauthorized (Check your Bearer Token)"
            }

        # ❌ Other errors
        else:
            return {
                "tool": "official_x_api",
                "status": "error",
                "message": f"Error {response.status_code}: {response.text}"
            }

    except Exception as e:
        return {
            "tool": "official_x_api",
            "status": "error",
            "message": str(e)
        }