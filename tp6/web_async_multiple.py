"""Module providing a function printing python version."""

from os.path import exists
from sys import exit as sysexit, argv
import time

import asyncio

from wrtite.async_write_content import async_write_content_in_file
from get.async_get_content import async_get_content
from read.read_file import read_file


async def main():
    """Function printing python version."""

    start_time = time.time()

    if not argv[1]:
        print("You must input a path (path/os/liste/urls)")
        sysexit(1)

    input_file = argv[1]

    if not await exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sysexit(1)
    urls = read_file(input_file)

    for url in urls:
        try:
            content = await async_get_content(url)
            output_file = f"/tmp/web_{url.replace('https://', '')}"
            await async_write_content_in_file(content, output_file)

        except Exception as e:
            print(f"Failed to process URL {url}: {e}")
    
    await asyncio.gather( exists, async_get_content, async_write_content_in_file)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal execution time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
