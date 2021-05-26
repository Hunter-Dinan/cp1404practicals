"""Display summaries of Wikipedia pages from user input."""

import wikipedia

FIRST_RESULT_INDEX = 0


def main():
    """Display summaries of Wikipedia pages from user input."""
    wiki_input = input("Enter page title or search phrase:")
    while wiki_input != "":
        wiki_pages = get_wiki_pages_from_input(wiki_input)
        display_summary_of_wiki_page(wiki_pages)
        wiki_input = input("Enter page title or search phrase:")


def get_wiki_pages_from_input(wiki_input):
    """Search Wikipedia for page title or phrase and return Wikipedia pages list."""
    wiki_pages = wikipedia.search(wiki_input, results=10)
    return wiki_pages


def display_summary_of_wiki_page(wiki_pages: list):
    """
    Display summary of first Wikipedia page in the given list of pages,
    that is not a Disambiguation page.
    """
    wiki_page_title = wiki_pages[FIRST_RESULT_INDEX]
    try:
        print("Page: {}\n"
              "Summary:\n{}".format(wiki_page_title, wikipedia.summary(wiki_page_title, auto_suggest=False)))
    except wikipedia.exceptions.DisambiguationError as e:
        print("DisambiguationError, input may refer to:")
        print(e.options)


main()
