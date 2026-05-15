# osint_layer/nlp/nlp_analyzer.py

import spacy
from transformers import pipeline
import re

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Load sentiment model explicitly
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_text(text: str):
    """
    Perform NLP analysis on profile text.
    Extracts:
    - Named entities
    - Sentiment
    - Potential sensitive indicators
    """

    if not text or text.strip() == "":
        return {
            "entities": [],
            "sentiment": {
                "label": "NEUTRAL",
                "score": 0
            },
            "sensitive_indicators": []
        }

    doc = nlp(text)

    entities = []
    sensitive = []

    for ent in doc.ents:

        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

        # Detect potentially sensitive entity types
        if ent.label_ in ["GPE", "LOC"]:
            sensitive.append(f"Location reference detected: {ent.text}")

        if ent.label_ in ["ORG"]:
            sensitive.append(f"Organization reference detected: {ent.text}")

        if ent.label_ in ["PERSON"]:
            sensitive.append(f"Person reference detected: {ent.text}")

    # Detect email addresses in bio
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)

    for email in emails:
        sensitive.append(f"Email address detected: {email}")

    # Run sentiment analysis
    sentiment = sentiment_pipeline(text)[0]

    return {
        "entities": entities,
        "sentiment": {
            "label": sentiment.get("label"),
            "score": sentiment.get("score")
        },
        "sensitive_indicators": sensitive
    }