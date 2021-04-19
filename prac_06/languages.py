"""Stores Programming Language information in a list"""
from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    programming_languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()
