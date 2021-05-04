"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # Change ' ' to '_'
    fixed_name_1 = filename.replace(" ", "_").replace(".TXT", ".txt")

    # Change prev char islower() and char isupper(), change to 'sliced word' + ' ' + nextchar.upper()
    fixed_name_2 = ''
    slice_index = 0
    for i, char in enumerate(fixed_name_1):
        if i > 0:
            if fixed_name_1[i-1].islower() and char.isupper():
                name_part = fixed_name_1[slice_index:i] + '_' + char.upper()
                slice_index = i + 1
                fixed_name_2 += name_part
            elif fixed_name_1[i-1].isupper() and char.isupper():    # for OComeAllYeFaithful.txt
                name_part = fixed_name_1[0] + '_' + char.upper()
                slice_index = i + 1
                fixed_name_2 += name_part
    fixed_name_2 = fixed_name_2 + fixed_name_1[slice_index:]

    # prevchar is '_', change nextchar to nextchar.upper()
    fixed_name_3 = ''
    slice_index = 0
    for i, char in enumerate(fixed_name_2):
        if i > 0:
            if fixed_name_2[i-1] == '_':
                name_part = fixed_name_2[slice_index:i] + char.upper()
                slice_index = i + 1
                fixed_name_3 += name_part
    fixed_name_3 = fixed_name_3 + fixed_name_2[slice_index:]

    # prevchar is '(', change nextchar to nextchar.upper()
    fixed_name_4 = ''
    slice_index = 0
    for i, char in enumerate(fixed_name_3):
        if i > 0:
            if fixed_name_3[i - 1] == '(':
                name_part = fixed_name_3[slice_index:i] + char.upper()
                slice_index = i + 1
                fixed_name_4 += name_part
    fixed_name_4 = fixed_name_4 + fixed_name_3[slice_index:]
    return fixed_name_4


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            old_filename = os.path.join(directory_name, filename)
            new_filename = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_filename, new_filename)


main()
