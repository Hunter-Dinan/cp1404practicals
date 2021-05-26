"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(input_string, number_of_times_repeated):
    """Repeat input_string a given amount of times with spaces in between."""
    repeated_strings = []
    for i in range(number_of_times_repeated):
        repeated_strings.append(input_string)
    output_string = " ".join(repeated_strings)
    return output_string


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase: str):
    """
    Format phrase as a sentence with capital letter and period.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('Nice to meet you')
    'Nice to meet you.'
    """
    sentence = ""
    if phrase[0].islower():
        sentence += phrase[0].upper()
        sentence += phrase[1:]
    else:
        sentence += phrase
    if phrase[-1] != ".":
        sentence += "."
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    new_car = Car()
    assert new_car.fuel == 0

    assert format_phrase_as_sentence("hello") == "Hello."
    assert format_phrase_as_sentence("It is an ex parrot.") == "It is an ex parrot."
    assert format_phrase_as_sentence("Nice to meet you") == "Nice to meet you."


run_tests()

# (PyCharm may see >>> doctest comments and run doctests anyway.)
doctest.testmod()

# 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass
