import os
import shutil
import re
from prompt_toolkit import prompt

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

def file_generator(source_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            yield file_path

@log_decorator
def move_and_sort_files(source_folder, destination_folder):
    # Déplacer tous les fichiers en utilisant un générateur
    for file_path in file_generator(source_folder):
        shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

    # Trier les fichiers en utilisant filter et map
    for filename in map(lambda f: os.path.join(destination_folder, f), 
                        filter(lambda f: not re.match(r'^\.', f), os.listdir(destination_folder))):
        if os.path.isfile(filename):
            file_extension = os.path.splitext(filename)[1][1:].lower()
            extension_folder = os.path.join(destination_folder, file_extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
            
            try:
                shutil.move(filename, os.path.join(extension_folder, os.path.basename(filename)))
            except Exception as e:
                print(f"Error sorting file {os.path.basename(filename)}: {e}")

def main():
    print("File Sorter CLI")
    source_folder = prompt("Enter the path to the source folder: ").strip()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    destination_folder = os.path.join(script_directory, "sorted")
    move_and_sort_files(source_folder, destination_folder)
    print("Files have been moved and sorted.")

if __name__ == "__main__":
    main()
