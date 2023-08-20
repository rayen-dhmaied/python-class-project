from random import randint
from colorama import*

def saisie():
    while 1:
        N=int(input("Donner la taille de tableau :"))
        if 4<=N<=50:
            break
    return N

def remplir(n):
    T=[]
    for i in range(n):
        while 1:
            x=int(input("T[%d] ="%i))
            if 111<=x<=999:
                break
        T.append(x)
    return T

def premier(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1

def premier_absolu(x):
    ch=str(x)
    for i in range(len(ch)):
        for j in range(len(ch)):
            for k in range(len(ch)):
                if ( i!=j and i!=k and j!=k):
                    if not premier(int(str(ch[i]+ch[j]+ch[k]))):
                        return 0
    return 1

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 6 ****\n")
    print('\033[94m'+"Un nombre à 3 chiffres x est dit premier absolu s'il est premier et tous les nombres formé\npar les combinaisons de ses 3 chiffres sont également premiers. Remplir un tableau par des\nnombres positifs de 3 chiffres pour rechercher et afficher les nombres premiers absolus.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    N=saisie()
    T=remplir(N)
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****")
    cp=0
    for x in T:
        if premier_absolu(x):
            print(x,"est un nombre premier absolu")
            cp+=1
    if cp==0:
        print("Il n'ya pas des nombres premiers absolus dans le tableau !")
    print("\n")
