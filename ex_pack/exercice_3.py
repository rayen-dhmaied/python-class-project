from colorama import*

def saisie():
    while 1:
        N=int(input("Donner la taille de la liste :"))
        if 2<=N<=50:
            break
    return N

def remplir(n):
    L=[]
    for i in range(n):
        while 1:
            x=int(input("L["+str(i)+"] : "))
            if x !=0:
                break
        L.append(x)
    return L

def sequence_nulle(L):
    S=[]
    cp=0
    for i in range(len(L)):
        somme=L[i]
        for j in range(i+1,len(L)):
            somme+=L[j]
            if somme==0:
                for k in range(i,j+1):
                    S.append(L[k])
                cp+=1
                if cp==1:
                    print("Les sequences nulles sont :")
                print(S)
                S.clear()
    print("Le nombre de sequences nulles est :",cp)

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 3 ****\n")
    print('\033[94m'+"Une séquence nulle est un ensemble d'entiers consécutifs dont la somme des valeurs est égale à zéro.\nRemplir une liste avec des entiers non nuls pour afficher le nombre et les éléments de ces séquences.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    N=saisie()
    L=remplir(N)
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****\n")
    sequence_nulle(L)
    print("\n")
