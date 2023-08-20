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

def longue_sequence_nulle(L):
    S=[]
    cp=0
    for i in range(len(L)):
        somme=L[i]
        for j in range(i+1,len(L)):
            somme+=L[j]
            if somme==0:
                cp=1
                if (j-i+1)>len(S):
                    S.clear()
                    for k in range(i,j+1):
                        S.append(L[k])
    if cp:
        print("La premiere longue sequence dont la somme nulle :",S)
    else:
        print("Il n'a pas des sequences nulles dans la liste")

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 4 ****\n")
    print('\033[94m'+"Remplir une liste L par N entiers non nuls pour trouver et afficher la première longue séquence nulle.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    N=saisie()
    L=remplir(N)
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****\n")
    longue_sequence_nulle(L)
    print("\n")
