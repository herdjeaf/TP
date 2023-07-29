import socket
# Créer un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Adresse et port du serveur
server_address = ('localhost', 8888) # Remplacez localhost par l'adresse IP du serveur et utilisez le port correspondant
# Envoyer des données au serveur
message = "Bonjour, serveur!"
client_socket.sendto(message.encode(), server_address)
# Recevoir la réponse du serveur
data = client_socket.recv(1024) # 1024 est la taille maximale des données à recevoir
response = data.decode()
# Afficher la réponse du serveur
print(f"Réponse du serveur: {response}")
# Fermer le socket client
client_socket.close()
