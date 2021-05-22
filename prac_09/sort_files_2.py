"""Program that sorts files into directories based on their given category."""


import os
import os.path
import shutil

FILE_TYPE_INDEX = 1


def main():
    """Program that creates directories from given categories and stores the corresponding file types within them."""
    os.chdir('FilesToSort')
    file_names = os.listdir('.')
    file_types = get_file_types(file_names)
    file_type_to_category = choose_category_per_file_type(file_types)
    create_directory_per_category(file_type_to_category)
    move_files_to_dir_by_category(file_names, file_type_to_category)


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


def choose_category_per_file_type(file_types: list):
    """Choose categories for file types and return a dictionary."""
    file_type_to_category = {}
    for file_type in file_types:
        category = input("What category would you like to sort {} files into? ".format(file_type))
        file_type_to_category[file_type] = category
    return file_type_to_category


def create_directory_per_category(file_type_to_category: dict):
    """Create directories for each category in the dictionary."""
    for category in file_type_to_category.values():
        try:
            os.mkdir(category)
        except FileExistsError:
            pass


def move_files_to_dir_by_category(file_names, file_type_to_category: dict):
    """Move files to directories based on their category."""
    for file_name in file_names:
        if not os.path.isdir(file_name):
            file_name_parts = file_name.split('.')
            file_type = file_name_parts[FILE_TYPE_INDEX]
            category = file_type_to_category[file_type]
            shutil.move(file_name, category + '/' + file_name)


main()
