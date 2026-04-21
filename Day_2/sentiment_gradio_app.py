import gradio as gr
from transformers import pipeline
from typing import Any, cast
# Load the sentiment analysis model once (at startup)
sentiment_pipeline = pipeline(
    cast(Any, "sentiment-analysis"),
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of the input text.
    
    Args:
        text: User input string
        
    Returns:
        Dictionary with sentiment label and confidence score
    """
    if not text or text.strip() == "":
        return {"sentiment": "NEUTRAL", "confidence": 0.0, "message": "Please enter some text."}
    
    # Run sentiment analysis
    result = sentiment_pipeline(text)
    
    # Extract label and score
    label = result[0]['label']
    confidence = result[0]['score']
    
    # Format for display
    return {
        "sentiment": label,
        "confidence": round(confidence * 100, 2),  # Convert to percentage
        "message": f"Sentiment: {label} (Confidence: {confidence*100:.1f}%)"
    }

# Custom function that returns formatted output for Gradio display
def format_sentiment_output(text: str):
    """Returns a formatted string for Gradio to display."""
    if not text or text.strip() == "":
        return "⚠️ Please enter some text to analyze."
    
    result = sentiment_pipeline(text)
    label = result[0]['label']
    confidence = result[0]['score']
    
    # Create emoji and color indicators
    if label == "POSITIVE":
        emoji = "😊"
        indicator = "🟢"
    else:
        emoji = "😞"
        indicator = "🔴"
    
    return f"""{indicator} **{label}** {emoji}
    
Confidence: {confidence*100:.1f}%

---
*Input text:* "{text[:200]}{'...' if len(text) > 200 else ''}"
"""

# Create the Gradio Interface
demo = gr.Interface(
    fn=format_sentiment_output,
    inputs=gr.Textbox(
        label="Enter your text here",
        placeholder="Type a sentence or paragraph... e.g., 'I absolutely love this movie!'",
        lines=5
    ),
    outputs=gr.Markdown(label="Sentiment Analysis Result"),
    title="🎭 Sentiment Analysis App",
    description="""
    Enter any text below, and the AI will analyze its sentiment (positive or negative).
    
    **Examples:**
    - "I had a wonderful day today!"
    - "This is the worst experience ever."
    - "The meeting was productive and efficient."
    """,
    examples=[
        ["I absolutely love this product! Best purchase ever!"],
        ["This is terrible. I'm very disappointed."],
        ["The movie was okay, nothing special."],
        ["I'm feeling great about our team's progress."],
        ["Customer support was unhelpful and rude."]
    ],
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()