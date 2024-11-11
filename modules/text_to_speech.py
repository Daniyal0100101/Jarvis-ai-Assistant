import pyttsx3
import requests
from playsound import playsound
import os
from typing import Union, Optional
from .system_control import is_connected

def init_tts_engine() -> Optional[pyttsx3.Engine]:
    """
    Initialize the text-to-speech engine with appropriate settings.

    Returns:
    - An initialized pyttsx3.Engine instance or None if initialization fails.
    """
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            # Select the second voice if available, otherwise default to the first one
            engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
        else:
            print("No voices available in the TTS engine. Using default settings.")
        
        engine.setProperty('rate', 172)
        engine.setProperty('volume', 0.9)
        return engine
    except Exception as e:
        print(f"Error initializing TTS engine: {e}")
        return None

# Initialize the TTS engine globally
engine = init_tts_engine()

def speak_tts(text: str) -> None:
    """
    Speak the given text using the locally initialized TTS engine.

    :param text: Text to be spoken.
    """
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error during TTS speech synthesis: {e}")
    else:
        print(text)

def generate_audio(message: str, voice: str = "Matthew") -> Union[None, bytes]:
    """
    Generate audio from text using the StreamElements API.

    :param message: Text message to convert to speech.
    :param voice: Voice to use for speech synthesis.
    :return: Audio content as bytes or None if the request fails.
    """
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching audio from StreamElements API: {e}")
        return None

def speak_audio(message: str, voice: str = "Matthew", folder: Optional[str] = None, extension: str = ".mp3") -> Union[None, str]:
    """
    Save generated audio to a file, play it, and delete the file afterward.

    :param message: Text message to convert to speech.
    :param voice: Voice to use for speech synthesis.
    :param folder: Directory to save the audio file. Defaults to the current directory.
    :param extension: Extension for the audio file. Defaults to '.mp3'.
    :return: Path of the saved audio file or None if an error occurs.
    """
    folder = folder or ""
    try:
        audio_content = generate_audio(message, voice)
        if audio_content is None:
            return None
        
        file_path = os.path.join(folder, f"{voice}{extension}")
        with open(file_path, "wb") as file:
            file.write(audio_content)
        
        try:
            playsound(file_path)
        except Exception as e:
            print(f"Error playing sound file '{file_path}': {e}")
        
        os.remove(file_path)
        return file_path
    except Exception as e:
        print(f"Error in speak_audio function: {e}")
        return None

def speak(text: str) -> None:
    """
    Speak the given text using the appropriate method based on the system's connection status.

    :param text: Text to be spoken.
    """
    clean_text = text.strip()
    if is_connected():
        if not speak_audio(clean_text):
            # Fallback to local TTS if online synthesis fails
            print("Falling back to local TTS engine.")
            speak_tts(clean_text)
    else:
        speak_tts(clean_text)
