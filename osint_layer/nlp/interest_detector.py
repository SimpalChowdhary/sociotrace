# interest_detector.py

def detect_interests(text: str):
    """
    Detect user interests based on keywords found in text.
    """

    if not text:
        return []

    text = text.lower()

    interest_keywords = {

        "Software Development": [
            "developer", "programming", "software", "coding",
            "python", "java", "javascript", "api"
        ],

        "Open Source": [
            "open source", "github", "linux", "pip", "package"
        ],

        "Artificial Intelligence": [
            "ai", "machine learning", "deep learning", "neural"
        ],

        "Cybersecurity": [
            "security", "cyber", "hacking", "malware", "exploit"
        ],

        "Blockchain": [
            "crypto", "bitcoin", "ethereum", "blockchain", "web3"
        ],

        "Finance": [
            "finance", "trading", "investing", "stocks"
        ],

        "Gaming": [
            "gaming", "gamer", "twitch", "esports"
        ],

        "Space": [
            "space", "nasa", "astronomy", "rocket"
        ]
    }

    detected_interests = []

    for interest, keywords in interest_keywords.items():
        for keyword in keywords:
            if keyword in text:
                detected_interests.append(interest)
                break

    return detected_interests