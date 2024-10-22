def repondre(message):
    if 'meo' in message.lower():
        return "Meo à toi confrère.".encode("UTF-8")
    elif 'waf' in message.lower():
        return 'ptdr t ki'.encode("UTF-8")
    else:
        return "Mes respects humble humain.".encode("UTF-8")