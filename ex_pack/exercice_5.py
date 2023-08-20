from colorama import*

def saisie():
    while 1:
        N=int(input("Donner la taille de tableau :"))
        if 4<=N<=50:
            break
    return N

def remplir(n):
    L=[]
    for i in range(n):
        while 1:
            ch=input("Nom["+str(i)+"] : ")
            if ch.isalpha() and ch.isupper() and len(ch)<=20:
                break
        L.append(ch)
    return L

def cmpt_voy(ch):
    voy_num=0
    for c in ch:
        if c in ['A','E','I','O','U','Y']:
            voy_num+=1
    return voy_num

def generer_tid(L,n):
    TID=[]
    for i in range(n):
        n=ord(L[i][0])+cmpt_voy(L[i])
        if n>90:
            id=L[i][:2]+str(i)+'a'
        else :
            id=L[i][:2]+str(i)+chr(n)
        TID.append(id)
    print("Le tableau des identificateurs genere est :",TID)

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 5 ****\n")
    print('\033[94m'+"Remplir un tableau par des noms d'utilisateurs pour générer des identifiants d'utilisateurs à partir de ces noms.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    N=saisie()
    T=remplir(N)
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****\n")
    generer_tid(T,N)
    print("\n")
