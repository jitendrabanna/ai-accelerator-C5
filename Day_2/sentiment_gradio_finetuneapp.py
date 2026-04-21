import gradio as gr
from gradio.themes import Soft
from transformers import pipeline
from typing import Any, cast
sentiment_pipeline = pipeline(
    cast(Any, "sentiment-analysis"),
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment_advanced(text: str):
    """Returns both sentiment and confidence for richer UI."""
    if not text or text.strip() == "":
        return "Neutral", 0.0, "⚠️ Enter text to analyze"
    
    result = sentiment_pipeline(text)
    label = result[0]['label']
    confidence = result[0]['score']
    
    # Map to readable labels
    sentiment = "Positive" if label == "POSITIVE" else "Negative"
    
    return sentiment, confidence, f"✅ Analysis complete"

# Create interface with multiple outputs
with gr.Blocks(title="Sentiment Analysis Studio", theme=Soft()) as demo:
    gr.Markdown("# 🎭 Sentiment Analysis Studio")
    gr.Markdown("Enter any text and get real-time sentiment analysis using a Hugging Face model.")
    
    with gr.Row():
        with gr.Column(scale=2):
            input_text = gr.Textbox(
                label="Your Text",
                placeholder="Type something here...",
                lines=6
            )
            submit_btn = gr.Button("🔍 Analyze Sentiment", variant="primary")
            
        with gr.Column(scale=1):
            sentiment_output = gr.Label(label="Predicted Sentiment")
            confidence_output = gr.Slider(
                label="Confidence Score",
                minimum=0,
                maximum=1,
                interactive=False,
                visible=True
            )
            status_output = gr.Textbox(label="Status", interactive=False)
    
    # Examples section
    gr.Markdown("### 📝 Try these examples:")
    examples = gr.Examples(
        examples=[
            "I absolutely love this product!",
            "This is the worst experience ever.",
            "The weather is nice today.",
            "I'm feeling very frustrated with this service."
        ],
        inputs=input_text
    )
    
    # Connect the button to the function
    submit_btn.click(
        fn=analyze_sentiment_advanced,
        inputs=input_text,
        outputs=[sentiment_output, confidence_output, status_output]
    )
    
    # Real-time analysis (optional - uncomment to enable)
    # input_text.change(
    #     fn=analyze_sentiment_advanced,
    #     inputs=input_text,
    #     outputs=[sentiment_output, confidence_output, status_output]
    # )

if __name__ == "__main__":
    demo.launch(share=False)  # Set share=True for a public link