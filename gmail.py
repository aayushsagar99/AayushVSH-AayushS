import imaplib
import time
import os
import sys

# Pygame is used here for reliable macOS audio playback
try:
    from pygame import mixer
except ImportError:
    print("Error: pygame not found. Please run: pip install pygame")
    sys.exit(1)

# --- CONFIGURATION ---
EMAIL = "your_email@gmail.com"
PASSWORD = "your_16_char_app_password" # Use the 16-char Google App Password
SENDER_TO_WATCH = "userresearch@withgoogle.com"
SOUND_FILE = "alert.mp3" # Ensure this file is in the same folder
CHECK_INTERVAL = 60 # Seconds between checks

def check_gmail():
    try:
        # Initialize sound mixer
        mixer.init()
        
        # Connect to Gmail via IMAP
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        # Search for UNREAD (UNSEEN) emails from the specific sender
        search_criteria = f'(UNSEEN FROM "{SENDER_TO_WATCH}")'
        result, data = mail.search(None, search_criteria)
        
        # Get list of email IDs
        mail_ids = data[0].split()
        
        if mail_ids:
            print(f"Found {len(mail_ids)} new email(s) from {SENDER_TO_WATCH}!")
            
            # Play the alert sound
            if os.path.exists(SOUND_FILE):
                mixer.music.load(SOUND_FILE)
                mixer.music.play()
                # Keep script alive while sound plays
                while mixer.music.get_busy():
                    time.sleep(0.1)
            else:
                print(f"Alert: Email received, but '{SOUND_FILE}' was not found in this folder.")
            
            # CRITICAL: Mark as read so it doesn't alert again next minute
            for mail_id in mail_ids:
                mail.store(mail_id, "+FLAGS", "\\Seen")
        else:
            print("No new emails from userresearch yet...")

        mail.logout()
    except imaplib.IMAP4.error:
        print("Auth Error: Check your App Password and ensure 2-Step Verification is on.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(f"Monitoring started for {SENDER_TO_WATCH}...")
    print("Keep this window open. Press Ctrl+C to stop.")
    while True:
        check_gmail()
        time.sleep(CHECK_INTERVAL)
