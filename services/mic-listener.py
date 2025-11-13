#!/usr/bin/env python3
"""
Microphone listener service - captures audio and transcribes locally
"""
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel
import torch

# Initialize GPU-accelerated Whisper
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"🚀 Loading Whisper model on {device.upper()}...")
model = WhisperModel("base.en", device=device, compute_type="float16" if device == "cuda" else "int8")

def transcribe_audio_file(audio_path):
    """
    Transcribe an audio file to text.
    
    Args:
        audio_path: Path to audio file
    
    Returns:
        str: Transcribed text
    """
    segments, _ = model.transcribe(audio_path, language="en")
    return " ".join([seg.text for seg in segments]).strip()

def main():
    """Simple test - transcribe command line audio file"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python mic-listener.py <audio_file>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    print(f"📝 Transcribing: {audio_file}")
    
    result = transcribe_audio_file(audio_file)
    print(f"\n[TRANSCRIPT]\n{result}")

if __name__ == "__main__":
    main()
