from colorama import*

def saisie():
    while 1:
        N=int(input("Donner la taille de la liste :"))
        if 2<=N:
            break
    return N

def saisie_chaine(i):
    while 1:
        ch=input("Joueur[%d] = "%i)
        if (all(c.isalpha() or c.isspace() for c in ch)) and ch[0].isupper() and ch.count(" ")==1 and ch[ch.find(" ")+1:].isupper():
            break
    return ch

def saisie_essai(i):
    while 1:
        x=int(input("Essai %d :"%i))
        if 0<=x<=10:
            break
    return x

def tri_dict_value(d):
    trie_dict={}
    trie_keys=sorted(d,key=d.get)
    for k in reversed(trie_keys):
        trie_dict[k]=d[k]
    return trie_dict

def remplir(n):
    resultats={}
    for i in range(1,n+1):
        ch=saisie_chaine(i)
        score=0
        for j in range(1,4):
            score+=saisie_essai(j)
        resultats[ch]=score
    return tri_dict_value(resultats)

def affiche_resultats(d):
    for k in d:
        print('\033[36m'+k+" avec un score de "+str(d[k]))

def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** Jeu de tir a l’arc ****\n")
    N=saisie()
    D=remplir(N)
    print('\033[94m'+"Classement :\n")
    affiche_resultats(D)
    print("\n")
