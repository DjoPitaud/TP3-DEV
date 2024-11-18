"""Module providing a function printing python version."""

from sys import exit as sysexit
import aiohttp


async def async_get_content(argv_url):
    """Function printing python version."""

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(argv_url) as response:

                html = await response.text()
                return html
    except aiohttp.ClientError as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        sysexit(1)
