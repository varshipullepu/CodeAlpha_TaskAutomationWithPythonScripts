import os
import shutil

# Define the directory to organize
DIRECTORY_TO_ORGANIZE = "/path/to/your/directory"

# Dictionary that maps file extensions to folder names
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.doc', '.pptx', '.ppt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.html', '.css', '.js', '.java', '.cpp', '.c'],
    'Others': []
}

# Function to create directories if they don't exist
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Function to organize files by moving them into folders based on file types
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Determine the folder name based on the file extension
        folder_name = 'Others'  # Default folder for unknown file types
        for category, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                folder_name = category
                break

        # Create the destination folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        create_directory(folder_path)

        # Move the file to the correct folder
        shutil.move(file_path, folder_path)
        print(f'Moved: {filename} -> {folder_name}')

# Run the file organizer
if __name__ == "__main__":
    organize_files(DIRECTORY_TO_ORGANIZE)
    print("File organization completed.")
