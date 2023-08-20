from colorama import*
from math import pow,trunc

def saisie():
    while 1:
        P=int(input("Donner P:"))
        Q=int(input("Donner Q:"))
        if 10<P<Q<=10000:
            break
    return P,Q

def racine_cubique(x):
    x=pow(x,1/3)
    if x-trunc(x)==0 or x-trunc(x)>=0.99:
        return round(x)
    return x

def nikomakhos(n,rc_n):
    for i in range(1,n//2,2):
        L=[]
        L.append(i)
        somme=i
        x=i
        for _ in range(rc_n-1):
            x+=2
            L.append(x)
            somme+=x
        if somme==n:
            ch=str(rc_n)+"^3 = "+str(n)+" = "+str(L[0])
            for j in range(1,len(L)):
                        ch+=(" + "+str(L[j]))
            print(ch)
    

def parcours(p,q):
    cp=0
    for n in range(p,q+1):
        rc_n=racine_cubique(n)
        if isinstance(rc_n,int):
            cp+=1
            if cp==1:
                print("\nLes nombres sous la (les) decomposition(s) du cube de chaque entier sont :")
            nikomakhos(n,rc_n)
    if cp==0:
        print("\nIl n'y a pas des nombres sous la (les) decomposition(s) du cube de chaque entier.")

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 1 ****\n")
    print('\033[94m'+"D'apres l'introduction arithmétique de Nikomakhos,tout cube d'un\nnombre naturel non nul X est égal à la somme de X nombres impairs\nconsécutifs. Donnez un intervalle [P,Q] pour trouver ces nombres.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    P,Q=saisie()
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****")
    parcours(P,Q)
    print("\n")
