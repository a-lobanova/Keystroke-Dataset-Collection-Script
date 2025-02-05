# Keystroke Dataset Collection Script

This script records audio of keystrokes while verifying password inputs against a predefined dataset. It is designed for research purposes, particularly in acoustic side-channel attacks and keystroke recognition.

## Features
-	Reads a list of passwords from a text file.
-	Records keystroke sounds while the user types a password.
-	Verifies if the input matches the expected password.
-	Saves the recorded keystrokes only when the correct password is entered.

## Setup Instructions
### 1. Install Dependencies
Ensure you have Python 3 installed, then install the required dependencies:

pip install sounddevice numpy soundfile

### 2. Prepare the Dataset
Create a text file (passwords.txt) containing passwords, each on a new line:

password1
password2
password3

### 3. Run the Script

Provide the path to your passwords.txt file in the script, then execute:

python collect_keystrokes.py

When prompted, enter a password. If correct, the keystroke audio will be saved.
