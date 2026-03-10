# github_runner.py

import requests


def run_github_api(username: str) -> dict:
    """
    Fetch public GitHub profile data via API.
    """

    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code != 200:
            return {
                "tool": "github_api",
                "status": "error",
                "message": "User not found"
            }

        user_data = response.json()

        data = {
            "username": user_data.get("login"),
            "name": user_data.get("name"),
            "bio": user_data.get("bio"),
            "followers": user_data.get("followers"),
            "following": user_data.get("following"),
            "public_repos": user_data.get("public_repos"),
            "location": user_data.get("location"),
            "company": user_data.get("company")
        }

        return {
            "tool": "github_api",
            "status": "success",
            "data": data
        }

    except Exception as e:
        return {
            "tool": "github_api",
            "status": "error",
            "message": str(e)
        }