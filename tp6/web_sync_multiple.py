"""Module providing a function printing python version."""

from os.path import exists
from sys import exit as sysexit, argv

from wrtite.write_content import write_content_in_file
from get.get_content import get_content
from read.read_file import read_file


def main():
    """Function printing python version."""

    if not argv[1]:
        print("You must input a path (path/os/liste/urls)")
        sysexit(1)

    input_file = argv[1]

    if not exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sysexit(1)
    urls = read_file(input_file)

    for url in urls:
        try:
            content = get_content(url)
            output_file = f"/tmp/web_{url.replace('https://', '')}"
            write_content_in_file(content, output_file)
            print(f"Content saved to: {output_file}")
        except Exception as e:
            print(f"Failed to process URL {url}: {e}")


if __name__ == "__main__":
    main()
