from colorama import*
from ex_pack import*
from time import sleep
from os import system

init(autoreset=True)
banner = """
  __  __ _       _   ____            _      _     _____ ____ _____ 
 |  \/  (_)_ __ (_) |  _ \ _ __ ___ (_) ___| |_  |_   _|  _ \___  |
 | |\/| | | '_ \| | | |_) | '__/ _ \| |/ _ \ __|   | | | |_) | / / 
 | |  | | | | | | | |  __/| | | (_) | |  __/ |_    | | |  __/ / /  
 |_|  |_|_|_| |_|_| |_|   |_|  \___// |\___|\__|   |_| |_|   /_/   
                                  |__/                             
"""
nom = """
.----------------------------------.
| Preparé par : Rayen Dhmaied      |
| Proposé par : Mr. Kais Ben Salah |
'----------------------------------'
"""
print('\033[92m'+banner)
print('\033[94m'+nom)
for i in range (4):  
    b = "Chargement" + "." * i
    print (b, end="\r")
    sleep(0.5)
while 1:
    print('\033[33m'+"**** MENU GENERAL ****",end='\n\n')
    for i in range(1,10):
        print("\033[91m"+"{0}  -  EXERCICE {0}".format(i))
    print("\033[91m"+"10 -  EXERCICE 10")
    print("\033[91m"+"11 -  QUITTER",end='\n\n')
    while 1:
        choix=int(input("Donner Votre Choix SVP:"))
        if choix in range(1,12):
            break
    system('cls')
    if choix==11:
        quit()
    elif choix==1:
        exercice_1.lancer()
    elif choix==2:
        exercice_2.lancer()
    elif choix==3:
        exercice_3.lancer()
    elif choix==4:
        exercice_4.lancer()
    elif choix==5:
        exercice_5.lancer()
    elif choix==6:
        exercice_6.lancer()
    elif choix==7:
        exercice_7.lancer()
    elif choix==8:
        while 1:
            x=int(input("Vous voulez lancer en mode GUI ou CLI ? (GUI:1 CLI:0) :"))
            if x in [0,1]:
                break
        system('cls')
        if x:
            exercice_8_gui.lancer()
        else:
            exercice_8_cli.lancer()
    elif choix==9:
        while 1:
            x=int(input("Vous voulez lancer en mode GUI ou CLI ? (GUI:1 CLI:0) :"))
            if x in [0,1]:
                break
        system('cls')
        if x:
            exercice_9_gui.lancer()
        else:
            exercice_9_cli.lancer()
    elif choix==10:
        while 1:
            x=int(input("Vous voulez lancer en mode GUI ou CLI ? (GUI:1 CLI:0) :"))
            if x in [0,1]:
                break
        system('cls')
        if x:
            exercice_10_gui.lancer()
        else:
            exercice_10_cli.lancer()
    print("Appuyez sur enter pour revenir au menu général.")
    input()
    system('cls')
