import socket
import ssl

# Créer un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Lier le socket à une adresse et un port
server_address = ('localhost', 8888) # Utilisez l'adresse IP de votre choix et un port disponible
server_socket.bind(server_address)

# Boucle principale du serveur pour l'échange des données 
while True:
    print('Le serveur est en attente de messages...')

    # Recevoir les données et l'adresse du client
    data = server_socket.recvfrom(4096) # 1024 est la taille maximale des données à recevoir

    # Afficher les informations du client
    print(f"Message reçu: {data[0]}")
    print(f"De: {data[1]}")
# Traiter les données reçues (vous pouvez ajouter votre propre logique ici)
# ...
    break
# enveloppe le socket avec SSL pour créer une connexion sécurisée

# Envoyer une réponse au client
response = "Message reçu avec succès!"
server_socket.sendto(response.encode(), data[1])
server_socket.close()