import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_text(text: str):
    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    sentiment = sentiment_pipeline(text)[0]

    return {
        "entities": entities,
        "sentiment": sentiment
    }