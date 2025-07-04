# Import necessary modules
import os  # Used for directory scanning and filesystem interaction
from pathlib import Path  # Used for handling filesystem paths in an object-oriented way

# Define a dictionary to categorize files based on their extensions
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "IMAGES": ['.jpeg', '.jpg', '.png'],
    "CODES": ['.py', '.go']
}

# Function to choose the appropriate directory based on file extension
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"  # Return 'MISC' if no matching category is found

# Function to organize files in the current directory
def organizeDirectory():
    for item in os.scandir():  # Iterate through all items in the current directory
        if item.is_dir():  # Skip directories
            continue
        filePath = Path(item)  # Convert item to a Path object
        fileType = filePath.suffix.lower()  # Get the file extension in lowercase
        directory = pickDirectory(fileType)  # Determine the target directory name
        directoryPath = Path(directory)  # Convert it to a Path object
        if not directoryPath.is_dir():  # Create directory if it doesn't already exist
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))  # Move file to the appropriate folder
