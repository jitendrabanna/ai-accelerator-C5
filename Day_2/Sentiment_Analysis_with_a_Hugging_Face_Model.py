# test_sentiment.py - Run this first to verify the model works
from typing import Any, cast

from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline(
    cast(Any, "sentiment-analysis"),
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Test with sample texts
test_texts = [
    "I love this product! It's amazing!",
    "This is terrible, I hate it.",
    "The weather is okay today."
]

for text in test_texts:
    result = sentiment_pipeline(text)
    print(f"Text: {text}")
    print(f"Sentiment: {result[0]['label']} (confidence: {result[0]['score']:.4f})")
    print("-" * 50)