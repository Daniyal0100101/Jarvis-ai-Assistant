import speech_recognition as sr
from .text_to_speech import speak

def listen(timeout=15, phrase_time_limit=60):
    """
    Listen to the user's speech and convert it to text, handling various potential issues robustly.

    Parameters:
    - timeout: Maximum number of seconds that the function will wait for speech input.
    - phrase_time_limit: Maximum number of seconds allowed per phrase of speech.

    Returns:
    - A string containing the recognized text if successful, or None if recognition fails.
    """
    recognizer = sr.Recognizer()
    
    try:
        # Ensure microphone availability and handle exceptions
        with sr.Microphone() as source:
            print("\nListening...")
            
            # Calibrate the recognizer to ambient noise levels
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                # Capture audio from the microphone within specified timeout and phrase time limit
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                print("Recognizing...")
                
                # Attempt to recognize the speech using Google's speech recognition service
                text = recognizer.recognize_google(audio)
                if text:
                    print(f"\nUser: {text}")
                    return text
            
            except sr.UnknownValueError:
                # Speech was not recognized (no transcribable speech found)
                return None
            
            except sr.RequestError as e:
                # Handle errors related to the speech recognition service itself
                error_message = f"Apologies, there was an issue with the speech recognition service: {e}"
                print(error_message)
                speak(error_message)
            
            except sr.WaitTimeoutError:
                # Handle cases where the speech input times out
                error_message = "Listening timed out. No speech was detected."
                print(error_message)
                speak(error_message)
            
            except Exception as e:
                # Handle any other unexpected errors
                error_message = f"An unexpected error occurred during recognition: {e}"
                print(error_message)
                speak(error_message)
    
    except OSError as e:
        # Handle cases where the microphone is not available or inaccessible
        error_message = f"Microphone not found or not accessible: {e}"
        print(error_message)
        speak(error_message)
    
    except Exception as e:
        # Handle any other general exceptions
        error_message = f"An error occurred while trying to access the microphone: {e}"
        print(error_message)
        speak(error_message)
    
    return None
