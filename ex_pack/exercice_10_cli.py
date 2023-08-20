from random import randint
from colorama import*

def saisie_char():
    while 1:
        c=input("Saisir une lettre :")
        if (c.isupper() or c.islower()) and len(c)==1:
            break
    return c
    
def chercher_char(c):
    for i in range(len(tmp_dev_mot)):
        if c==tmp_dev_mot[i]:
            return i
    return -1

def eliminer_char(i):
    global tmp_dev_mot
    ch=""
    if i==0:
        ch="*"+tmp_dev_mot[1:]
    elif i==len(tmp_dev_mot):
        ch=tmp_dev_mot[:len(tmp_dev_mot)-1]+"*"
    else :
        ch=tmp_dev_mot[:i]+"*"+tmp_dev_mot[i+1:]
    tmp_dev_mot=ch

def ajouter_char(c,i):
    global nou_mot
    for k in range(len(tmp_dev_mot)):
        if i==k:
            L[i]=c
    ch=""
    for k  in range(len(tmp_dev_mot)):
        ch+=L[k]
    nou_mot=ch

def jeu():
    essai=7
    while essai>0:
        print('\033[93m'+"Tu a "+str(essai)+" essais a pour deviner le mot")
        C=saisie_char()
        I=chercher_char(C)
        if I == -1:
            essai-=1
            if not essai:
                print('\033[31m'+"\n\tDesole , Vous avez perdu ! La mot a deviner est ' %s '"%dev_mot)
                break
            else:
                print('\033[91m'+"\n\tLa lettre n'existe pas de le mot !\n")
                continue
        else:
            eliminer_char(I)
            ajouter_char(C,I)
            if nou_mot==dev_mot:
                print ('\033[92m'+"\n\tBravo , Vous avez gagnée ! La mot est ' %s '"%nou_mot)
                break
            else:
                print('\033[36m'+"\n\tBien ! Vous avez trouvez une lettre , Ton progres : %s\n"%nou_mot)

def lancer():
    init(autoreset=True)
    mots=['abundant','peck','mysterious','flower','person','scissors','reach','farm','ceaseless','injure','plain','object','dashing','remember','whip','unsuitable','sack','friendly','aquatic','shaggy','anxious','earsplitting','excited','glass','devilish','garrulous','pointless','various','crazy','two','team','foolish','malicious','replace','previous','cherries','six','direful','huge','dull','protective','uncovered','haunt','examine','alert','gratis','vegetable','reason','worry','brief']
    global dev_mot
    global tmp_dev_mot
    global nou_mot
    global L
    dev_mot=mots[randint(0,len(mots)-1)]
    tmp_dev_mot=dev_mot
    nou_mot=""
    L=[]
    for _ in range(len(dev_mot)):
        L.append("_")
    print('\033[95m'+"\n**** Devinez Le Mot ****\n")
    jeu()
    print("\n")
