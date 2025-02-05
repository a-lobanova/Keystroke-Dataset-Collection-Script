import threading
import sounddevice as sd
import numpy as np
import os
import soundfile as sf
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    filename="py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

SAMPLE_RATE = 16000
DURATION = 9  # Time for input password (6 symbols)
dir_path = os.path.dirname(os.path.realpath(__file__))
passwords_path = os.path.join(dir_path, "passwords.txt")
audio_path = os.path.join(dir_path, "keystrokes/wav")

if not os.path.exists(audio_path):
    os.makedirs(audio_path)

with open(passwords_path, "r") as f:
    passwords = f.read().splitlines()

# Global variables
recorded_audio = []
password_correct = threading.Event()  # Thread-safe flag


def record_audio():
    """Record audio."""
    global recorded_audio
    recorded_audio = []  # Reset buffer
    start_time = time.time()

    def callback(indata, frames, time_info, status):
        if status:
            logging.warning(f"Audio callback status: {status}")
        recorded_audio.append(indata.copy())

    try:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback):
            sd.sleep(int(DURATION * 1000))
    except Exception as e:
        logging.error(f"Error during audio recording: {e}")

    logging.info(f"Audio recording duration: {time.time() - start_time:.2f} seconds")


def save_audio(filename):
    """Save recorded audio."""
    audio_data = np.concatenate(recorded_audio, axis=0)
    filepath = os.path.join(audio_path, f"{filename}.wav")

    try:
        sf.write(filepath, audio_data, samplerate=SAMPLE_RATE)
        logging.info(f"Audio saved: {filepath}")
    except Exception as e:
        logging.error(f"Error saving audio: {e}")


def check_password(input_password, expected_password):
    """Check if input password matches the expected password."""
    if input_password == expected_password:
        password_correct.set()
        logging.info("Password is correct.")
    else:
        password_correct.clear()
        logging.warning(
            f"Wrong password: {input_password} (expected: {expected_password})"
        )


def main(expected_password):
    while True:
        recording_thread = threading.Thread(target=record_audio)
        logging.debug("Starting recording thread.")
        recording_thread.start()

        input_password = input(f"Input password: {expected_password}\n")

        check_thread = threading.Thread(
            target=check_password, args=(input_password, expected_password)
        )
        logging.debug("Starting password check thread.")
        check_thread.start()

        check_thread.join()
        recording_thread.join()

        if password_correct.is_set():
            save_audio(expected_password)
            break
        else:
            print("Incorrect password. Try again.")


for expected_password in passwords:
    main(expected_password)
