"""Module providing a function printing python version."""

from sys import exit as sysexit


def write_content_in_file(content, file):
    """Function printing python version."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Contenu écrit dans {file}")
    except OSError as e:
        print(f"Erreur lors de l'écriture dans le fichier : {e}")
        sysexit(1)
