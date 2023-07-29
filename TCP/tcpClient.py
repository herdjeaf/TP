import ssl
import socket
# Configuration du client
host = 'localhost'
port = 8000

# Définir le contexte de SSL
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations("D:/Cours/M2/IoT/TP/OpenSSL/certificate/server.pem")

# Créer un socket TCP
client_socket = ssl_context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=host)
# Se connecter au serveur
client_socket.connect((host, port))
print("Connecté au serveur TCP")
# Envoyer des données au serveur
message = "Hello, server!"
client_socket.send(message.encode())
# Recevoir la réponse du serveur
data = client_socket.recv(1024)
received_data = data.decode()
print("Réponse du serveur :", received_data)
# Fermer la connexion avec le serveur
client_socket.close()
