import socket
import time

#Configuration du débit de données maximum en octets par seconde
MAX_BYTES_PER_SECOND = 1000


# Créer un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Lier le socket à une adresse et un port
server_address = ('localhost', 8888) # Utilisez l'adresse IP de votre choix et un port disponible
server_socket.bind(server_address)

# Initialiser le temps de départ et le nombre d'octets reçus
start_time = time.time()
bytes_received = 0

# Boucle principale du serveur pour l'échange des données 
while True:

    print('Le serveur est en attente de messages...')
    # Recevoir des données depuis le socket
    data = server_socket.recvfrom(1024)
    bytes_received += len(data)

    # Calculer le temps écoulé depuis le début du transfert
    elapsed_time = time.time() - start_time

    # Vérifier si le débit de données maximum a été atteint
    if bytes_received > MAX_BYTES_PER_SECOND:
        # Attendre suffisamment de temps pour respecter le débit de données maximum
        time_to_wait = bytes_received / MAX_BYTES_PER_SECOND - elapsed_time
        time.sleep(time_to_wait)

    # Traiter les données reçues
    # Afficher les informations du client
    print(f"Message reçu: {data[0]}")
    print(f"De: {data[1]}")
    # Envoyer une réponse au client
    response = "Message reçu avec succès!"
    server_socket.sendto(response.encode(), data[1])
    server_socket.close()