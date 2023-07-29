import ssl
import socket
# from pip._vendor import requests

# response = requests.get('https://localhost', verify=False)

# Définir le contexte de SSL
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="D:/Cours/M2/IoT/TP/OpenSSL/certificate/server.pem", keyfile="D:/Cours/M2/IoT/TP/OpenSSL/certificate/server.key")

# Configuration du serveur
host = 'localhost'
port = 8000
max_connections = 1

# Créer un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à une adresse et un port
server_socket.bind((host, port))

# Mettre le socket en mode écoute
server_socket.listen()

active_connections = 0

print("Serveur TCP démarré. En attente de connexions...")

try:
    while True:

        # Accepter une connexion entrante
        client_socket, client_address = server_socket.accept()
        print("Client connecté :", client_address)

        if active_connections >= max_connections:
            #Rejeter  la demande de connexion si le nombre de connexion est atteint
            client_socket.close()
        else:
            active_connections +=1
            # Enveloppe la socket avec SSLContext, connexion securisee
            secure_socket = ssl_context.wrap_socket(client_socket, server_side=True)
            # Recevoir des données du client
            data = secure_socket.recv(1024)
            received_data = data.decode()
            print("Message reçu du client :", received_data)

            # Envoyer une réponse au client
            response = "Message reçu avec succès!"
            secure_socket.send(response.encode())
            active_connections -=1
except socket.timeout:
    pass
    # Fermer la connexion avec le client
    secure_socket.close()

    # Fermer le socket du serveur
    server_socket.close()