"""Module providing a function printing python version."""

from sys import exit as sysexit

from requests import get, exceptions



def get_content(argv_url):
    """Function printing python version."""

    try:
        response = get(argv_url, timeout=10)
        response.raise_for_status()
        return response.text
    except exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        sysexit(1)
