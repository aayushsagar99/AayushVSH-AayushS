import os
import shutil

# 1. Safely get a secret API key from your system's environment variables
# If 'MY_SECRET_KEY' isn't found, it returns "Not Found" instead of crashing
def main():
    api_key = os.getenv('MY_SECRET_KEY', 'Not Found')

    print(f"Your API Key is: {api_key}")

    # 2. Check which Operating System you are running
    if os.name == 'nt':
        print("You are on Windows.")
    elif os.name == 'posix':
        print("You are on Mac or Linux.")
    else:
        print(f"Unsupported OS: {os.name}")



# 1. Define the folder you want to clean up
folder_to_clean = r"/Users/aayushsagar/Downloads"  # Use your actual path

# 2. Map extensions to their new category folders
file_map = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".go", ".rs", ".java", ".c", ".cpp", ".sh", ".bat"]
}

def organize_folder(path):
    # Loop through every file in the directory
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip if it's a folder, only process files
        if os.path.isfile(file_path):
            # Get the file extension (e.g., '.pdf')
            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            # Find which category this extension belongs to
            for folder_name, extensions in file_map.items():
                if extension in extensions:
                    # Create the category folder if it doesn't exist
                    target_folder = os.path.join(path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    
                    # Move the file!
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} -> {folder_name}/")
                    break

# Run the function
organize_folder(folder_to_clean)

import os
import time

def cleanup_old_files(path, days=30):
    # Calculate how many seconds are in 'X' days
    seconds_in_day = 24 * 60 * 60
    cutoff_time = time.time() - (days * seconds_in_day)

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        
        # Only check files, not folders
        if os.path.isfile(file_path):
            # Get the last modification time of the file
            file_mod_time = os.path.getmtime(file_path)
            
            if file_mod_time < cutoff_time:
                try:
                    os.remove(file_path)
                    print(f"Deleted old file: {filename}")
                except Exception as e:
                    print(f"Error deleting {filename}: {e}")

# Run it on your downloads folder
cleanup_old_files(r"/Users/aayushsagar/Downloads")

