"""Program that sorts files into directories based on their file type."""

import os
import os.path
import shutil

FILE_TYPE_INDEX = 1


def main():
    """Program that creates directories for each file type and stores the corresponding files within it."""
    os.chdir('FilesToSort')
    file_names = os.listdir('.')
    file_types = get_file_types(file_names)
    create_directory_per_file_type(file_types)
    move_files_to_dir_by_type(file_names)


def get_file_types(file_names: list):
    """Return a list of file_types."""
    file_types = []
    for file_name in file_names:
        if not os.path.isdir(file_name):
            file_name_parts = file_name.split('.')
            file_type = file_name_parts[FILE_TYPE_INDEX]
            if file_type not in file_types:
                file_types.append(file_type)
    return file_types


def create_directory_per_file_type(file_types: list):
    """Create directories for each file type in the list."""
    for file_type in file_types:
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass


def move_files_to_dir_by_type(file_names: list):
    """Move files to directories based on their type."""
    for file_name in file_names:
        if not os.path.isdir(file_name):
            file_name_parts = file_name.split('.')
            shutil.move(file_name, file_name_parts[FILE_TYPE_INDEX] + '/' + file_name)


main()
