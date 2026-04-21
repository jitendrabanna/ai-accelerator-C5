from pathlib import Path
from typing import Any, cast

import soundfile as sf
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Load the automatic speech recognition pipeline
transcriber = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

# This is just for demonstration purposes. In a real scenario, you would load your audio file.
# audio_data = "/content/Durga Nagar Road 3.m4a" # Dummy data for 1 second of audio at 16kHz
# sf.write("/content/Durga Nagar Road 3.m4a", audio_data, 16000)

# Transcribe the audio
audio_candidates = [
	Path(__file__).resolve().parents[1] / "dummy_audio.wav",
	Path(__file__).with_name("Trump_WEF_2018.mp3"),
	Path(__file__).resolve().parents[1] / "Day_6" / "session_2" / "data" / "audio" / "ai_agents.mp3",
]
audio_file = next((path for path in audio_candidates if path.exists()), None)
if audio_file is None:
	raise FileNotFoundError(
		"No demo audio file found. Update audio_candidates with a valid local audio path."
	)

audio_array, sample_rate = sf.read(audio_file)
if getattr(audio_array, "ndim", 1) > 1:
	audio_array = audio_array.mean(axis=1)

audio_input = {"array": audio_array, "sampling_rate": sample_rate}
transcription = cast(dict[str, Any], transcriber(audio_input))

print("Transcription:")
print(transcription['text'])



# Load a summarization model directly because this transformers version
# does not expose the "summarization" pipeline task.
summary_model_name = "sshleifer/distilbart-cnn-12-6"
summary_tokenizer = AutoTokenizer.from_pretrained(summary_model_name)
summary_model = AutoModelForSeq2SeqLM.from_pretrained(summary_model_name)

# Text to summarize
text = """
Hugging Face is a company and open-source platform that provides tools and models for natural language processing (NLP). It has become a central hub for the ML community, offering a wide range of pre-trained models that can be easily used or fine-tuned for specific applications. Key aspects of Hugging Face include the Transformers library, Model Hub, Datasets library, and Tokenizers library. Hugging Face democratizes access to powerful ML models, making it easier for developers and researchers to build and deploy applications.
"""

# Summarize the text
summary_inputs = summary_tokenizer(
	text.strip(),
	return_tensors="pt",
	truncation=True,
	max_length=1024,
)
summary_ids = summary_model.generate(
	**summary_inputs,
	max_new_tokens=60,
	min_length=25,
	num_beams=4,
	do_sample=False,
)
summary_text = summary_tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Original Text:")
print(text)
print("\nSummary:")
print(summary_text)