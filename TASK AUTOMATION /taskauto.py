import os
import shutil

def organize_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Create folders for different file types
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1]
            folder_name = file_extension[1:].upper() + "_Files"  # Create folder name from file extension
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
    
    # Move files to their respective folders
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1]
            folder_name = file_extension[1:].upper() + "_Files"  # Get folder name for file extension
            folder_path = os.path.join(directory, folder_name)
            shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))

if __name__ == "__main__":
    directory = input("Enter the directory path to organize files: ")
    organize_files(directory)
    print("Files organized successfully!")
