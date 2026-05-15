import instaloader
import requests
import os

def run_instaloader(username: str):

    try:

        L = instaloader.Instaloader()

        profile = instaloader.Profile.from_username(L.context, username)

        profile_pic_url = str(profile.profile_pic_url)

        # Save image locally
        image_path = f"static/profile_images/{username}_instagram.jpg"

        try:
            img_data = requests.get(profile_pic_url).content

            with open(image_path, "wb") as handler:
                handler.write(img_data)

            local_image = "/" + image_path

        except:
            local_image = None

        data = {
            "username": profile.username,
            "name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "profile_image": local_image
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