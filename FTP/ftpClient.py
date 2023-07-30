import ftplib
import ssl

# Paramètres de connexion FTP
ftp_host = 'localhost'
ftp_port = 21
ftp_username = 'username'
ftp_password = 'password'

# Chemin d'accès à la clé privée et au certificat
keyfile = 'D:/Cours/M2/IoT/TP/OpenSSL/certificate/server.key'
certfile = 'D:/Cours/M2/IoT/TP/OpenSSL/certificate/server.pem'

# Créer un contexte SSL/TLS personnalisé
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)

# Créer une connexion FTP sécurisée
ftp = ftplib.FTP_TLS()
ftp.connect(ftp_host, ftp_port)
ftp.auth()
ftp.prot_p()
ftp.login(user=ftp_username, passwd=ftp_password)

# Effectuer des opérations FTP sécurisées
# Liste les fichiers/dossiers dans le répertoire distant
ftp.cwd('')
ftp.retrlines('LIST')
files = ftp.nlst()
# Affiche la liste des fichiers/dossiers
for file in files:
    print(file)


# Télécharger un fichier du serveur FTP
filename = 'ftp.py'
local_filepath = 'D:/Cours/M2/IoT/TP/TCP/file.py'
ftp.retrbinary('RETR ' + filename, open(local_filepath, 'wb').write)


# Envoyer un fichier vers le serveur FTP
local_filepath = 'D:/Cours/M2/IoT/TP/TCP/tcpClient.py'
filename = 'tcpClient.py'
ftp.storbinary('STOR ' + filename, open(local_filepath, 'rb'))
# Fermer la connexion FTP
ftp.quit()