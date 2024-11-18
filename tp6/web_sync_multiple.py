"""Module providing a function printing python version."""

from sys import exit as sysexit, argv

from wrtite.write_content import write_content_in_file
from get.get_content import get_content


def main():
    """Function printing python version."""

    if not argv[1]:
        print("You must input a url(https://www.example.com)")
        sysexit(1)

    url = argv[1]
    output_file = "/tmp/web_page"

    content = get_content(url)
    write_content_in_file(content, output_file)


if __name__ == "__main__":
    main()
