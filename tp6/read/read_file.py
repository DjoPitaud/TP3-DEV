"""Module providing a function printing python version."""

from sys import exit as sysexit

path_file = "home/djo/documents/liste_urls"

def read_file(input_file):
    """Function printing python version."""

    with open(input_file, "r") as file:
        urls = [line.strip() for line in file if line.strip()]
        print(f"{urls}")

    if not urls:
        print(f"No URLs found in '{input_file}'. Exiting.")
        sysexit(1)

read_file(path_file)