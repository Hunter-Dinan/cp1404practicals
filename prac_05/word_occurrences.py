"""Count the occurrences of words in a string."""


def main():
    word_to_occurrence = {}
    string_input = input("Text: ")
    string_length = len(string_input)

    word = ""
    for i, char in enumerate(string_input):
        if char == " ":
            store_word_occurrences(word_to_occurrence, word)
            word = ""
        elif i == string_length - 1:
            word += char
            store_word_occurrences(word_to_occurrence, word)
        else:
            word += char
    sorted_word_to_occurrence = get_sorted_dict(word_to_occurrence)
    max_word_length = get_max_word_length(word_to_occurrence)
    display_words(sorted_word_to_occurrence, max_word_length)


def store_word_occurrences(word_to_occurrence: dict, word):
    if word in word_to_occurrence:
        word_to_occurrence[word] += 1
    else:
        word_to_occurrence[word] = 1


def display_words(word_to_occurrence: dict, max_word_length):
    words = []
    word_display_length = max_word_length + 2
    for word in word_to_occurrence:
        words.append(word)
        print("{:{}} {}".format(word + " :", word_display_length, word_to_occurrence[word]))


def get_sorted_dict(word_to_occurrence: dict):
    words = []
    sorted_word_to_occurrence = {}
    for word in word_to_occurrence:
        words.append(word)
    words.sort()
    for word in words:
        sorted_word_to_occurrence[word] = word_to_occurrence[word]
    return sorted_word_to_occurrence


def get_max_word_length(word_to_occurrence: dict):
    words = []
    word_lengths = []
    for word in word_to_occurrence:
        words.append(word)
        word_lengths.append(len(word))
    max_word_length = max(word_lengths)
    return max_word_length


main()
