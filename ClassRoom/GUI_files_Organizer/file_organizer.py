import os
import shutil

def organize_files(directory):

    # Define file categories and corresponding extensions
    file_categories = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audio': ['.mp3', '.wav'],
        'Misc': []  # Any file that doesn't match the above categories
    }

    # Create subdirectories for each category
    for category in file_categories.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Move files into the appropriate category folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Move file to the correct category
        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                moved = True
                break

        # If file does not fit into any category, move to 'Others'
        if not moved:
            others_folder = os.path.join(directory, 'Misc')
            shutil.move(file_path, os.path.join(others_folder, filename))

    print(f"Files in {directory} have been organized into categories.")