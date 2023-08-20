from random import randint
from colorama import*

def saisir_allumettes():
    while 1:
        allum_choisi=int(input("Donnez votre jeu (3 max) :"))
        if allum_choisi in [1,2,3] and (num_allum-allum_choisi>=0):
            break
    return allum_choisi
def jeu_allumettes():
    global num_allum
    num_allum=randint(20,70)
    print("\033[91m"+"Jeu avec %d allumettes\n"%num_allum)
    while  1:
        while 1:
            allum_choisi_cpu=randint(1,3)
            if num_allum-allum_choisi_cpu>=0:
                break
        num_allum-=allum_choisi_cpu
        print('\033[92m'+"\nJe prends %d allumette(s)."%allum_choisi_cpu,'\033[92m'+"Il en reste %d"%num_allum)
        if num_allum==0:
            print('\033[32m'+"\nBravo vous avez gagnée ! :)")
            break
        num_allum-=saisir_allumettes()
        if num_allum==0:
            print('\033[31m'+"\nTu as perdu ! :( Bonne chance la prochaine fois.")
            break
def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** Jeu d'allumettes ****\n")
    jeu_allumettes()
    print("\n")
