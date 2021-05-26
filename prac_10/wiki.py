"""Display summaries of Wikipedia pages from user input."""

import wikipedia

FIRST_RESULT_INDEX = 0


def main():
    """Display summaries of Wikipedia pages from user input."""
    wiki_input = input("Enter page title or search phrase:")
    while wiki_input != "":
        wiki_pages = get_wiki_pages_from_input(wiki_input)
        display_information_of_wiki_page(wiki_pages)
        wiki_input = input("Enter page title or search phrase:")


def get_wiki_pages_from_input(wiki_input):
    """Search Wikipedia for page title or phrase and return Wikipedia pages list."""
    wiki_pages = wikipedia.search(wiki_input, results=10)
    return wiki_pages


def display_information_of_wiki_page(wiki_pages: list):
    """
    Display title, summary, and URL of first Wikipedia page in the given list of pages,
    that is not a Disambiguation page.
    """
    wiki_page_title = wiki_pages[FIRST_RESULT_INDEX]
    try:
        wiki_page = wikipedia.page(wiki_page_title, auto_suggest=False)
        print("Title: {}\n"
              "Summary:\n{}\n"
              "URL:{}".format(wiki_page.title, wiki_page.summary.strip(), wiki_page.url))
    except wikipedia.exceptions.DisambiguationError as e:
        print("DisambiguationError, input may refer to:")
        print(e.options)


main()
