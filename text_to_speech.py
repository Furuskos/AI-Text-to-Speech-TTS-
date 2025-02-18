from gtts import gTTS
import os

def text_to_speech(text, lang="en"):
    """Converts text to speech and saves as an audio file."""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("speech.mp3")
    os.system("start speech.mp3")

if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    text_to_speech(text)
