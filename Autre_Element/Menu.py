from pyfiglet import Figlet
from termcolor import colored, cprint

def menuPortScan():
    figlet = Figlet(font="starwars")
    print(figlet.renderText("Port Scan"))

def menuDDOS():
    figlet = Figlet(font='slant')
    print(figlet.renderText(" D D O S"))

def menuKey():
    print("   \n             -----Menu Keylogger----- "
          "\n\t/---------------------------------------\ \n"
          "\t|                                       |\n"
          "\t| [ START ] pour débuter le Keylogger   |\n"
          "\t| [ STOP ] pour stopper le Keylogger    |\n"
          "\t| [ GET ] pour récupérer le fichier     |\n"
          "\t|                                       |\n"
          "\t\---------------------------------------/\n")


def menu():
    print("\n\t/-------------------------\ \n"
          "\t|                         |\n"
          "\t|   [ 1 ]  Connexion      |\n"
          "\t|   [ 2 ]  Keylogger      |\n"
          "\t|   [ 3 ]  PortScan       |\n"
          "\t|   [ 4 ]  DDOS           |\n"
          "\t|   [ 5 ]  EXIT           |\n"
          "\t|                         |\n"
          "\t\-------------------------/\n")



def bannière():
    banner = """

    88                      88                                   88
    88                      88                                   88   
    88                      88888                                88888
    88,dPPYba,   ,adPPYba,  88          ,,           ,8edPPUba,  88
    88P'    "8a a8"     "8a 88          88,dPPUba,  88       d8' 88
    88       d8 8b       d8 88          88       d8 88e88e88e"'  88   
    88b,   ,a8" "8a,   ,a8" 88b,        88       88 88,          88b,   
    8Y"Ybbd8"'    "YbbdP"'  '8Y"Ybbd8"' 88       88  8Y"Ybbd8"'  '8Y"Ybbd8"'

    """
    print("\033[31m", banner, "\033[0m")
    print("                              by \033[32mBilal\033[0m")

