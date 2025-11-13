import sounddevice as sd
import numpy as np
import whisper
from datetime import datetime

MODEL_NAME = "base"  # You can use "tiny", "small", "medium", "large" as needed

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def listen_and_transcribe(samplerate=16000, chunk_duration=5):
    log(f"Loading Whisper model '{MODEL_NAME}'...")
    model = whisper.load_model(MODEL_NAME)
    log("Whisper model loaded. Continuous listening...")

    try:
        with sd.InputStream(samplerate=samplerate, channels=1, dtype='float32') as stream:
            while True:
                log("Listening...")
                audio = stream.read(int(chunk_duration * samplerate))[0]
                audio = np.squeeze(audio)
                audio = whisper.pad_or_trim(audio)
                mel = whisper.log_mel_spectrogram(audio)
                if model.device.type == "cuda":
                    mel = mel.to(model.device)
                options = whisper.DecodingOptions(language="en", fp16=False)
                result = whisper.decode(model, mel, options)
                text = result.text.strip()
                if text:
                    log(f"Recognized: {text}")
    except KeyboardInterrupt:
        log("Stopped by user.")

if __name__ == "__main__":
    listen_and_transcribe()
