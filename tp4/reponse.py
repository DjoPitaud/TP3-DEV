def repondre(message):
    if b'meo' in message.lower():
        return "Meo \xc3\xa0 toi confr\xc3\xa8re.".encode("UTF-8")
    elif b'waf' in message.lower():
        return 'ptdr t ki'.encode("UTF-8")
    else:
        return "Mes respects humble humain.".encode("UTF-8")