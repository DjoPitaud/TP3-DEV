"""Module providing a function printing python version."""

from os.path import exists
from sys import exit as sysexit, argv
import time

import asyncio

from process.process_url import process_url
from read.read_file import read_file


async def main():
    """Function printing python version."""

    start_time = time.time()

    if not argv[1]:
        print("You must input a path (path/os/liste/urls)")
        sysexit(1)

    input_file = argv[1]

    if not exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sysexit(1)
    urls = read_file(input_file)

    tasks = [process_url(url) for url in urls]

    await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
