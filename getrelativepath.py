import os

def list_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            print(relative_path)


folder_path = 'imgs/EPW'
list_files_in_directory(folder_path)