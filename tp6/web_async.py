"""Module providing a function printing python version."""

from sys import exit as sysexit, argv

import asyncio

from wrtite.async_write_content import async_write_content_in_file
from get.async_get_content import async_get_content


async def main():
    """Function printing python version."""

    if not argv[1]:
        print("You must input a url(https://www.example.com)")
        sysexit(1)

    url = argv[1]
    output_file = "/tmp/web_page"

    content = await async_get_content(url)
    await async_write_content_in_file(content, output_file)


if __name__ == "__main__":
    asyncio.run(main())
