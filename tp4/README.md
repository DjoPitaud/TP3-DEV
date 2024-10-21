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

> Vous aurez besoin du [**cours sur la gestion d'erreurs**](../../../../cours/dev/error_handling/README.md) pour cette partie.

- retour visuel
  - afficher un message de succès chez le client quand il se co au serveur
  - le message doit être : `Connecté avec succès au serveur <IP_SERVER> sur le port <PORT>`
  - vous utiliserez un `try` `except` pour savoir si la connexion est correctement effectuée
- le programme doit permettre à l'utilisateur d'envoyer la string qu'il veut au serveur
  - on peut récupérer un input utilisateur avec la fonction `input()` en Python
  - au lancement du programme, un prompt doit apparaître pour indiquer à l'utilisateur qu'il peut envoyer une string au serveur :
    - `Que veux-tu envoyer au serveur : `

🌞 **`bs_server_I2.py`**

- retour visuel
  - afficher un message quand un client se co
  - le message doit être : `Un client vient de se co et son IP c'est <CLIENT_IP>.`
- réponse adaptative
  - si le message du client contient "meo" quelque part, répondre : `Meo à toi confrère.`
  - si le message du client contient "waf" quelque part, répondre : `ptdr t ki`
  - si le message du client ne contient PAS "meo", ni "waf", répondre : `Mes respects humble humain.`

## 3. You say client I hear control

On va ajouter un peu de contrôle pour éviter que notre client fasse nawak à l'utilisation du programme.

🌞 **`bs_client_I3.py`**

- vérifier que...
  - le client saisit bien une string
    - utilisez la méthode native `type()` pour vérifier que c'est une string
  - que la string saisie par le client contient obligatoirement soit "waf" soit "meo"
    - utilisez **une expression régulière**
- sinon lever une erreur avec `raise`
  - choisissez avec pertinence l'erreur à lever dans les deux cas (s'il saisit autre chose qu'une string, ou si ça contient aucun des deux mots)
  - y'a un lien vers la liste des exceptions natives (choisissez-en une donc) tout en bas du [cours sur la gestion d'erreur](../../../../cours/dev/error_handling/README.md)

> On poussera le contrôle de saisie plus loin plus tard.