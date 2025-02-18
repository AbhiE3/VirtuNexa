import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []  # Any uncategorized files
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    move_file(file_path, directory, category)
                    moved = True
                    break
            
            if not moved:  # Move to 'Others' if no category matched
                move_file(file_path, directory, "Others")
    
    print("File organization complete!")

def move_file(file_path, base_directory, category):
    category_path = os.path.join(base_directory, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)
    shutil.move(file_path, os.path.join(category_path, os.path.basename(file_path)))
    print(f"Moved: {file_path} -> {category_path}")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ").strip()
    organize_files(target_directory)
