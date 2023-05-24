import os
import shutil

def move_documents(source_folder, destination_folder):
    
    files = os.listdir(source_folder)

    for file in files:
        if file.endswith('.pdf') or file.endswith('.txt') or file.endswith ('.doc') or file.endswith ('.docx'):
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {destination_folder}")


source_folder = '/path/to/source/folder'
destination_folder = '/path/to/destination/folder'


move_documents(source_folder, destination_folder)
