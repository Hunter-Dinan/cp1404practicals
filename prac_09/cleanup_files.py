"""Cleanup filenames in Lyrics/Christmas directory."""
import os


def main():
    """Cleanup filenames in Lyrics/Christmas directory."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        fixed_filename = get_fixed_filename(filename)
        os.rename(filename, fixed_filename)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # Correction 1: Replace ' ' with '_'
    fixed_filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    # Correction 2: Add '_' to lowercase connected to uppercase, e.g. ObedientDog -> Obedient_Dog.
    fixed_filename = get_fixed_filename_correction_2(fixed_filename)

    # Correction 3: Add uppercase after '_', e.g. O_little_town_of_bethlehem -> O_Little_Town_Of_Bethlehem
    fixed_filename = get_fixed_filename_correction_3(fixed_filename)

    # Correction 4: Add uppercase after '(', e.g. Blue_Dog_(jerry) -> Blue_Dog_(Jerry)
    fixed_filename = get_fixed_filename_correction_4(fixed_filename)
    return fixed_filename


def get_fixed_filename_correction_2(filename):
    """Add '_' to lowercase connected to uppercase, e.g. ObedientDog -> Obedient_Dog."""
    fixed_filename = ''
    slice_index = 0
    for i, char in enumerate(filename):
        if i > 0:
            if filename[i - 1].islower() and char.isupper():
                fixed_name_part = filename[slice_index:i] + '_' + char.upper()
                slice_index = i + 1
                fixed_filename += fixed_name_part
            elif filename[i - 1].isupper() and char.isupper():  # for OComeAllYeFaithful.txt
                fixed_name_part = filename[i - 1] + '_' + char.upper()
                slice_index = i + 1
                fixed_filename += fixed_name_part
    fixed_filename = fixed_filename + filename[slice_index:]
    return fixed_filename


def get_fixed_filename_correction_3(filename):
    """Add uppercase after '_', e.g. O_little_town_of_bethlehem -> O_Little_Town_Of_Bethlehem."""
    fixed_filename = ''
    slice_index = 0
    for i, char in enumerate(filename):
        if i > 0:
            if filename[i - 1] == '_':
                fixed_name_part = filename[slice_index:i] + char.upper()
                slice_index = i + 1
                fixed_filename += fixed_name_part
    fixed_filename = fixed_filename + filename[slice_index:]
    return fixed_filename


def get_fixed_filename_correction_4(filename):
    """Add uppercase after '(', e.g. Blue_Dog_(jerry) -> Blue_Dog_(Jerry)."""
    fixed_filename = ''
    slice_index = 0
    for i, char in enumerate(filename):
        if i > 0:
            if filename[i - 1] == '(':
                fixed_name_part = filename[slice_index:i] + char.upper()
                slice_index = i + 1
                fixed_filename += fixed_name_part
    fixed_filename = fixed_filename + filename[slice_index:]
    return fixed_filename


main()
