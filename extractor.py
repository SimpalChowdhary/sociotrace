# extractor.py
from bs4 import BeautifulSoup

def extract_visible_info(html):
    soup = BeautifulSoup(html, "html.parser")

    profile_data = {
        "display_name": None,
        "bio": None,
        "links": []
    }

    # Extract display name from title
    title = soup.find("title")
    if title:
        profile_data["display_name"] = title.text.strip()

    # Extract bio from meta description
    meta_desc = soup.find("meta", {"name": "description"})
    if meta_desc:
        profile_data["bio"] = meta_desc.get("content", "").strip()

    # Extract visible external links
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http"):
            profile_data["links"].append(href)

    return profile_data
