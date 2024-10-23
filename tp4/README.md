# I. Simple bs program

- [I. Simple bs program](#i-simple-bs-program)
  - [1. First steps](#1-first-steps)
  - [2. User friendly](#2-user-friendly)
  - [3. You say client I hear control](#3-you-say-client-i-hear-control)

## 1. First steps

🌞 **`bs_server_I1.py`**

🌞 **`bs_client_I1.py`**

🌞 **Commandes...**
 
 - Commande ss -lpt | grep 13337 pour afficher l'écoute.
```
[djo@serveur ~]$ ss -lnpt | grep 13337
LISTEN 0      1            0.0.0.0:13337      0.0.0.0:*    users:(("python",pid=1459,fd=3))
```

- Exec programme côté `serveur`.
```
[djo@serveur tp4]$ python bs_server_I1.py
Connected by ('192.168.56.2', 58374)
Données reçues du client : b'Meooooo !'
```
- Exec programme côté client
```
[djo@client tp4]$ python bs_client_I1.py
Le serveur a répondu b'Hi mate!'
```

## 2. User friendly

🌞 **`bs_client_I2.py`**

```
[djo@client tp4]$ python bs_client_I1.py
Connecté avec succès au serveur 192.168.56.102 sur le port 13337
Que veux-tu envoyer au serveur ? meo
Le serveur a répondu 'Meo à toi confrère.'
[djo@client tp4]$ python bs_client_I1.py
Connecté avec succès au serveur 192.168.56.102 sur le port 13337
Que veux-tu envoyer au serveur ? waf
Le serveur a répondu 'ptdr t ki'
[djo@client tp4]$ python bs_client_I1.py
Connecté avec succès au serveur 192.168.56.102 sur le port 13337
Que veux-tu envoyer au serveur ? bonjour
Le serveur a répondu 'Mes respects humble humain.'
```

🌞 **`bs_server_I2.py`**

```
[djo@serveur tp4]$ python bs_server_I1.py
Un client vient de se co et son IP c'est ('192.168.56.2', 35284).
Données reçues du client : meo
[djo@serveur tp4]$ python bs_server_I1.py
Un client vient de se co et son IP c'est ('192.168.56.2', 52464).
Données reçues du client : waf
[djo@serveur tp4]$ python bs_server_I1.py
Un client vient de se co et son IP c'est ('192.168.56.2', 34336).
Données reçues du client : bonjour
```

## 3. You say client I hear control

On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.

🌞 **`bs_client_I3.py`**
- Pour le `type()`
```
if type(msg) is not str:
            raise TypeError("Ici on veut que des strings !")
```
- Pour l'expression régulière:
  - Création d'un fichier `re_verif.py`

```
import re

def verifier_msg(msg):
    
    pattern = r"(waf|meo)"
    
    return bool(re.search(pattern, msg))
```
```
import re_verif

elif re_verif.verifier_msg(msg) is False:
            raise ValueError("Ici on veut que meo et waf !")
```

