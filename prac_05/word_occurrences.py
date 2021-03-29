"""Count the occurrences of words in a string."""


def main():
    words = {}
    string_input = input("Text: ")

    word = ""
    for i, char in enumerate(string_input):
        string_length = len(string_input)
        if char == " ":
            store_word(words, word)
            word = ""
        elif i == string_length - 1:
            word += char
            store_word(words, word)
        else:
            word += char
    sorted_words = sort_words(words)
    display_words(sorted_words)
    print(words.keys())


def store_word(words: dict, word):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


def display_words(words: dict):
    words_list = []
    for word in words:
        words_list.append(word)
    max_word_length = max(words_list)
    print(max_word_length)
    print("{} : {}".format(word, words[word]))


def sort_words(words: dict):
    words_list = []
    sorted_words = {}
    for word in words:
        words_list.append(word)
    words_list.sort()
    for word in words_list:
        sorted_words[word] = words[word]
    return sorted_words


main()
