from random import randint
from colorama import*

def saisie():
    while 1:
        N=int(input("Donner la taille de tableau :"))
        if 5<=N<=50:
            break
    return N

def remplir_alea(n):
    T=[]
    for i in range(n):
        T.append(randint(10,99))
        print("T[%d] ="%i,T[i])
    return T

def element_tableau(T):
    L=[]
    for x in T:
        ch=str(x)
        for c in ch:
            if int(c) not in L:
                L.append(int(c))
    return L

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 7 ****\n")
    print('\033[94m'+"Donnez la taille du tableau pour qu'il se remplisse aléatoirement\navec des nombres positifs à 2 chiffres puis affichez un tableau\nde nombres qui composent les éléments du tableau sans redondance.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    N=saisie()
    T=remplir_alea(N)
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****\n")
    print("Les chiffres qui composent les elements du tableau T sans redondance : ",element_tableau(T))
    print("\n")
