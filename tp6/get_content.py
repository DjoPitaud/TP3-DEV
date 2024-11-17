from requests import get, exceptions
from sys import exit as sysexit 

url = "https://www.ynov.com"
def get_content(url):

    try:
        response = get(url)
        response.raise_for_status()
        return response.text
    except exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")
        sysexit(1)

get_content(url)
