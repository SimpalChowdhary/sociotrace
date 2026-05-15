import requests

def run_github_api(username):

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, verify=False)  # 🔥 FIX: disable SSL verify

        print("GitHub Status:", response.status_code)

        if response.status_code != 200:
            print("GitHub API ERROR:", response.text)
            return None

        data = response.json()

        return {
            "platform": "github",
            "username": data.get("login"),
            "name": data.get("name"),
            "bio": data.get("bio"),
            "followers": data.get("followers"),
            "following": data.get("following"),
            "public_repos": data.get("public_repos"),
            "location": data.get("location"),
            "company": data.get("company"),
            "profile_image": data.get("avatar_url"),
            "profile_url": data.get("html_url")
        }

    except Exception as e:
        print("GitHub Exception:", e)
        return None