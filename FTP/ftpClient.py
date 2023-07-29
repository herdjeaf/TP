from ftplib import FTP_TLS
# Informations de connexion au serveur FTP
ftp_server = '127.0.0.1'
username = 'herdjeaf'
password = '1234'
# Établir une connexion avec le serveur FTP
ftp = FTP_TLS(ftp_server)
ftp.login(username, password)
# Liste les fichiers/dossiers dans le répertoire distant
ftp.cwd('')
ftp.prot_p()
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
