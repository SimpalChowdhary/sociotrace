# linkedin_runner.py

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def run_linkedin(username: str) -> dict:
    """
    Fetch public LinkedIn profile metadata using Playwright.
    Extracts name, headline/bio, and profile image if publicly accessible.
    """

    profile_url = f"https://www.linkedin.com/in/{username}"

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )

            page = context.new_page()

            page.goto(profile_url, timeout=60000)

            # Allow metadata to load
            page.wait_for_timeout(4000)

            html = page.content()

            browser.close()

        soup = BeautifulSoup(html, "html.parser")

        name = ""
        bio = ""
        location = ""
        profile_image = ""

        # OpenGraph metadata extraction
        og_title = soup.find("meta", {"property": "og:title"})
        og_desc = soup.find("meta", {"property": "og:description"})
        og_image = soup.find("meta", {"property": "og:image"})

        if og_title:
            name = og_title.get("content", "").replace("| LinkedIn", "").strip()

        if og_desc:
            bio = og_desc.get("content", "").strip()

        if og_image:
            profile_image = og_image.get("content", "").strip()

        # Detect LinkedIn login wall
        if (
            "Sign Up" in name
            or "Join now" in name
            or "750 million+ members" in bio
            or "LinkedIn" in name and len(name) < 12
        ):
            return {
                "tool": "linkedin_scraper",
                "status": "blocked",
                "data": {
                    "platform": "linkedin",
                    "username": username,
                    "profile_url": profile_url
                }
            }

        data = {
            "platform": "linkedin",

            "username": username,
            "name": name or "",
            "bio": bio or "",
            "location": location or "",

            # LinkedIn follower counts are not publicly accessible
            "followers": None,
            "following": None,
            "public_repos": None,

            # Profile image for OSINT image analysis
            "profile_image": profile_image or "",

            "profile_url": profile_url
        }

        return {
            "tool": "linkedin_scraper",
            "status": "success",
            "data": data
        }

    except Exception as e:

        return {
            "tool": "linkedin_scraper",
            "status": "error",
            "message": str(e)
        }