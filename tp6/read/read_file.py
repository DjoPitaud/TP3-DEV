"""Module providing a function printing python version."""

from sys import exit as sysexit


def read_file(input_file):
    """Function printing python version."""

    with open(input_file, "r", encoding="utf-8") as file:
        urls = [line.strip() for line in file if line.strip()]
        cleaned_urls = [url.replace("https://", "") for url in urls]
        return urls, cleaned_urls
    if not urls:
        print(f"No URLs found in '{input_file}'. Exiting.")
        sysexit(1)