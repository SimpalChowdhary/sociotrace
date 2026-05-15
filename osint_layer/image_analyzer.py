# image_analyzer.py

def analyze_profile_images(github_data=None, linkedin_data=None, instagram_data=None):
    """
    Detect publicly accessible profile images across platforms.
    No face detection or image comparison — only OSINT exposure detection.
    """

    images = []

    # GitHub
    if github_data and github_data.get("profile_image"):
        images.append({
            "platform": "GitHub",
            "url": github_data.get("profile_image")
        })

    # LinkedIn
    if linkedin_data and linkedin_data.get("profile_image"):
        images.append({
            "platform": "LinkedIn",
            "url": linkedin_data.get("profile_image")
        })

    # Instagram
    if instagram_data and instagram_data.get("profile_image"):
        images.append({
            "platform": "Instagram",
            "url": instagram_data.get("profile_image")
        })

    # No images found
    if len(images) == 0:
        return {
            "status": "none",
            "message": "No publicly accessible profile images detected."
        }

    # Images found
    return {
        "status": "public",
        "message": "Profile photo publicly accessible.",
        "images": images
    }