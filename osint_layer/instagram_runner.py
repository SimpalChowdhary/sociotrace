# instagram_runner.py

import instaloader


def run_instaloader(username: str) -> dict:
    """
    Fetch basic public Instagram profile data.
    """

    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)

        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified
        }

        return {
            "tool": "instaloader",
            "status": "success",
            "data": data
        }

    except Exception as e:
        return {
            "tool": "instaloader",
            "status": "error",
            "message": str(e)
        }