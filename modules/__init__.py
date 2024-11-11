import spacy

# This file can be empty or can include initialization code if needed
password = "YOUR_PASSWORD_PLACEHOLDER"  # Placeholder for authentication password

# Contacts dictionary
contacts = {
    "user" : "USER_CONTACT_PLACEHOLDER",
    "mother" : "MOTHER_CONTACT_PLACEHOLDER",
    "father" : "FATHER_CONTACT_PLACEHOLDER",
    "sister_1" : "SISTER_1_CONTACT_PLACEHOLDER",
    "sister_2" : "SISTER_2_CONTACT_PLACEHOLDER"
    # Add more contacts as needed with placeholders
}

# API keys path 
WEATHER_API_KEY_PATH = "YOUR_API_KEY_PATH_PLACEHOLDER"
EMAIL_CREDENTIALS_PATH = "YOUR_EMAIL_CREDENTIALS_PATH_PLACEHOLDER"

# Define constants
NOTE_FILE_PATH = "YOUR_NOTE_FILE_PATH_PLACEHOLDER"

WORD_TO_OPERATOR = {
    '+': '+',
    '-': '-',
    'x': '*',
    '÷': '/'
}

# Initialize an empty conversation history
conversation_history = []

# List to store reminders
reminders = []

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
