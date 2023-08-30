# Author: Daniel Beglaryan
# Date: 7/05/23
# Description: This Python script organizes files in the user's Downloads folder into specific subfolders based on their file type.

import os
import glob
import shutil

# Get a list of all files in the user's Downloads folder
files_in_downloads = glob.glob(os.path.expanduser(r"{downloads_folder}"))

# Define file type categories
documents = ['.pdf', '.docx', '.doc', '.txt']
media = ['.jpeg', '.jpg', '.webp', '.svg', '.png', '.PNG', '.mp4', '.mp3']
setup_files = ['.exe', '.msi']
compressed_files = ['.zip']
other_files = ['.psd', '.ai', '.eps']

# Define destination folders for each file type
documents_location = os.path.expanduser("~/Downloads/PDF")
media_location = os.path.expanduser("~/Downloads/JPEG")
setup_files_location = os.path.expanduser("~/Downloads/EXE")
compressed_files_location = os.path.expanduser("~/Downloads/ZIP")
other_files_location = os.path.expanduser("~/Downloads/PSD")

# Organize files into their respective folders
for file_path in files_in_downloads:
    base_filename = os.path.basename(file_path)
    destination = None
    
    # Determine the destination folder based on the file extension
    file_extension = os.path.splitext(file_path)[1]
    if file_extension in documents:
        destination = documents_location
    elif file_extension in media:
        destination = media_location
    elif file_extension in setup_files:
        destination = setup_files_location
    elif file_extension in compressed_files:
        destination = compressed_files_location
    elif file_extension in other_files:
        destination = other_files_location
    
    # Move the file to its destination folder
    if destination:
        if os.path.exists(destination):
            new_path = os.path.join(destination, base_filename)
            
            # Handle duplicate file names by appending a count
            if os.path.exists(new_path):
                root, ext = os.path.splitext(base_filename)
                count = 1
                while os.path.exists(os.path.join(destination, f"{root}_{count}{ext}")):
                    count += 1
                new_path = os.path.join(destination, f"{root}_{count}{ext}")
            shutil.move(file_path, new_path)
        else:
            os.mkdir(destination)
            shutil.move(file_path, os.path.join(destination, base_filename))
