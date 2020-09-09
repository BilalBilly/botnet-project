import socket

def start_scan():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    host = str(input("\033[94m \n Entrez l'ip que vous voulez scanner: \033[0m"))
    #Les ports les plus importants
    port = [9,20,22,23,25,53,67,68,69,80,110,123,143,386,443,465,500,554,636,1352,1433,1521,1723,3306,3389,5432,6667,25565]

    for i in port:
        if s.connect_ex((host, i)):
            print(f"\033[31mLe port {i} est fermé\033[0m")
        else:
            print(f"\033[32mLe port {i} est ouvert\033[0m")



