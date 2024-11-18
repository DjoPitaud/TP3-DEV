"""Module providing a function printing python version."""

from wrtite.async_write_content import async_write_content_in_file
from get.async_get_content import async_get_content


async def process_url(url):
    """Process a single URL: get content and write it to file."""
    try:
        content = await async_get_content(url)
        output_file = f"/tmp/web_{url.replace('https://', '')}"
        await async_write_content_in_file(content, output_file)
    except Exception as e:
        print(f"Failed to process URL {url}: {e}")

