# AI Assistant README

## Overview
This project is an AI Assistant application that uses various Python libraries and machine learning models to provide multiple functionalities, such as speech recognition, text-to-speech synthesis, gesture control, system automation, image generation, object detection, and more. The assistant can interact with the user through either text or voice commands, automate tasks, perform actions based on gestures, and facilitate daily routines.

## Features

1. **Hand Gesture Detection**: Uses a camera to track hand movements and perform actions like clicking, double-clicking, and taking screenshots, controlled by specific hand gestures (file: `hand_gesture_detector.py`).

2. **Image Generation**: Generates images based on a given text prompt, using an API to create and save the generated image (file: `Image_generator.py`).

3. **Object Detection**: Uses a YOLOv5 model for object detection, silently loading a model and identifying objects captured by a camera feed (file: `object_detection.py`).

4. **Speech Recognition**: Uses the microphone to listen to user commands and convert them into text. Integrates error handling to manage microphone availability issues (file: `speech_recognition.py`).

5. **System Control**: Automates various system-level controls, such as adjusting volume, locking the screen, shutting down, restarting, or logging off the system (file: `system_control.py`).

6. **Text to Speech (TTS)**: Converts text into speech using either local or online text-to-speech services to provide audio responses to the user (file: `text_to_speech.py`).

7. **Apps Automation**: Sends WhatsApp messages instantly using `pywhatkit`, supporting quick communication (file: `apps_automation.py`).

8. **Voice and Text Interaction**: Supports both voice and text mode for user interaction, allowing switching between them based on the user's environment (file: `main.py`).

## Requirements

- Python 3.7+
- Required Python Libraries: Install all necessary dependencies by running:

  ```sh
  pip install -r requirements.txt
  ```

- Hardware Requirements:
  - Microphone for voice interaction.
  - Camera for hand gesture detection and object detection.

- API Keys:
  - Ensure to set paths for API keys for weather and email services in the `__init__.py` file.

## File Structure

- **`main.py`**: Entry point for running the assistant. Handles user authentication, greeting, interaction mode switching, and general query handling.
- **`hand_gesture_detector.py`**: Handles hand gesture detection and executes system actions based on recognized gestures.
- **`Image_generator.py`**: Generates images using an external API based on a given prompt.
- **`object_detection.py`**: Loads a YOLOv5 model to identify objects using the system camera.
- **`speech_recognition.py`**: Converts spoken user commands into text.
- **`system_control.py`**: Provides various system control functions like volume adjustment, shutdown, restart, etc.
- **`text_to_speech.py`**: Provides text-to-speech functionalities to vocalize responses.
- **`utils.py`**: Contains utility functions for greeting, scheduling tasks, managing reminders, etc.
- **`apps_automation.py`**: Sends WhatsApp messages using `pywhatkit`.
- **`__init__.py`**: Contains initialization configurations, constants, and sensitive paths.

## How to Run
1. Clone the repository to your local machine.
2. Install all the required libraries using `pip install -r requirements.txt`.
3. Set up the necessary paths and credentials in the `__init__.py` file.
4. Run the `main.py` file:

   ```sh
   python main.py
   ```

5. Authenticate using the defined password to access the assistant.

## Usage
- You can use the assistant to:
  - Control your system's volume, brightness, and power settings.
  - Generate images based on text descriptions.
  - Detect objects or use hand gestures to interact with your computer.
  - Perform web searches, send WhatsApp messages, set reminders, and more.
  - Switch between voice and text mode seamlessly.

## Customization
- **Credentials and Paths**: Update sensitive details such as passwords, API keys, and file paths in the `__init__.py`.
- **Gesture Settings**: Modify gesture thresholds and actions in `hand_gesture_detector.py` to customize the assistant's behavior.
- **Interaction Mode**: The default interaction mode is text if no internet connection is available. You can modify the default settings in `main.py`.

## Error Handling
- **Network Connectivity**: `system_control.py` includes a function to verify internet connectivity, and actions dependent on connectivity adapt accordingly.
- **Exceptions**: All modules include exception handling to manage unexpected errors gracefully.

## Limitations
- The assistant requires API keys for some functionalities (e.g., weather updates).
- Gesture detection may vary in accuracy based on camera quality and environmental conditions.
- The project is primarily Windows-compatible due to certain dependencies (`winsound`, `pyautogui` shortcuts).

## Future Improvements
- Implement a graphical user interface (GUI) for easier interactions.
- Add support for Linux/macOS commands.
- Improve gesture detection accuracy with better models or training.

## Credits
- Uses **YOLOv5** for object detection.
- Integrates **Google Speech Recognition** for speech-to-text conversion.
- Uses **pyttsx3** for local TTS and **StreamElements API** for online TTS.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code with proper attribution.
