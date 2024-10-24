def port_valid(port):

    if port < 0 or port > 65535:
        raise IndexError(
            f"ERROR -p argument invalide. Le port spécifié {port} n'est pas un port valide (de 0 à 65535)."
        )

    elif 0 <= port <= 1024:
        raise PermissionError(
            f"ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au-dessus de 1024."
        )
