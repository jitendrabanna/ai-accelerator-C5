import os
from io import BytesIO
from importlib import import_module

from transformers import pipeline
from PIL import Image
import requests
import torch
from datasets import load_dataset


try:
    userdata = import_module('google.colab').userdata
except ImportError:
    userdata = None
from huggingface_hub import whoami

# # Read from Colab Secrets when available, otherwise fall back to an env var.
if userdata is not None:
    hf_token = userdata.get('HF_TOKEN')
else:
    hf_token = os.getenv('HF_TOKEN')

# Verify the token by checking your identity
try:
    user_info = whoami(token=hf_token)
    print(f"Logged in as: {user_info['name']}")
except Exception as e:
    print(f"Could not log in: {e}")
    print("Set HF_TOKEN in Colab Secrets or as a local environment variable.")

# Load an image classification pipeline
classifier = pipeline("image-classification")

# Get an image from a URL (replace with your image URL)
url = "https://i.guim.co.uk/img/media/327aa3f0c3b8e40ab03b4ae80319064e401c6fbc/377_133_3542_2834/master/3542.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=34d32522f47e4a67286f9894fc81c863"
response = requests.get(url, timeout=30)
response.raise_for_status()
image = Image.open(BytesIO(response.content))

# Classify the image
predictions = classifier(image)

print("Image Classification Results:")
for prediction in predictions:
    print(f"- {prediction['label']}: {prediction['score']:.2f}")

# Load an audio classification pipeline
# We use a smaller model for demonstration purposes
classifier = pipeline("audio-classification", model="superb/wav2vec2-base-superb-ks")

# This is a simple sine wave, you would load your actual audio data.
dummy_audio = torch.randn(16000)  # 1 second of dummy audio at 16kHz


# Classify the audio
audio_input = {"array": dummy_audio.numpy(), "sampling_rate": 16000}
predictions = classifier(audio_input)

print("Audio Classification Results:")
for prediction in predictions:
    print(f"- {prediction['label']}: {prediction['score']:.2f}")

# Load a dataset (e.g., the SQuAD dataset for question answering)
dataset = load_dataset("squad")

# Print information about the dataset
print(dataset)

# Access an example from the training set
print("\nExample from the training set:")
print(dataset["train"][0])