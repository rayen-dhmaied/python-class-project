from tkinter import*
from tkinter import simpledialog
from tkinter import messagebox
from random import randint

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

def saisie_char():
    global essai
    c=char_entry.get()
    char_entry.delete(0,END)
    if (c.isupper() or c.islower()) and len(c)==1:
        i=chercher_char(c)
        if i != -1:
            eliminer_char(i)
            ajouter_char(c,i)
            if nou_mot==dev_mot:
                info_label.forget()
                char_entry.forget()
                verif_button.forget()
                statut.set("Bravo , Vous avez gagnée ! La mot est %s"%nou_mot)
                quit_button.forget()
                statut_label.pack()
                quit_button.pack(pady=10)
            else:
                statut.set("Bien ! Vous avez trouvez une lettre. Ton progres : %s"%nou_mot)
                quit_button.forget()
                statut_label.pack()
                quit_button.pack(pady=10)
                
        else:
            essai-=1
            if essai==0:
                info_label.forget()
                char_entry.forget()
                verif_button.forget()
                statut.set("Desole , Vous avez perdu ! La mot a deviner est '%s'"%dev_mot)
            else:
                if nou_mot == "":
                    statut.set("La lettre n'existe pas de le mot !")
                else:
                    statut.set("La lettre n'existe pas de le mot ! Ton progres : %s"%nou_mot)
                info.set("Devinez un caractère: Vous avez %d essais"%essai)
                quit_button.forget()
                statut_label.pack()
                quit_button.pack(pady=10)
    else:
        messagebox.showinfo("Erreur","Tapez un seul caractère alphabétique s'il vous plaît.")

def lancer():
    mots=['abundant','peck','mysterious','flower','person','scissors','reach','farm','ceaseless','injure','plain','object','dashing','remember','whip','unsuitable','sack','friendly','aquatic','shaggy','anxious','earsplitting','excited','glass','devilish','garrulous','pointless','various','crazy','two','team','foolish','malicious','replace','previous','cherries','six','direful','huge','dull','protective','uncovered','haunt','examine','alert','gratis','vegetable','reason','worry','brief']
    global dev_mot
    global tmp_dev_mot
    global nou_mot
    global L
    global essai
    global r
    global titre
    global info
    global info_label
    global char_entry
    global verif_button
    global statut
    global statut_label
    global quit_button
    dev_mot=mots[randint(0,len(mots)-1)]
    tmp_dev_mot=dev_mot
    nou_mot=""
    L=[]
    essai=7
    for _ in range(len(dev_mot)):
        L.append("_")
    r=Tk()
    r.title("Devinez Le Mot")
    r.geometry("500x235")
    r.config(background="#33FFE0")
    titre=Label(r,text="Devinez Le Mot",font=("Cambria",20),fg="blue",bg="#33FFE0")
    titre.pack()
    info=StringVar()
    info.set("Devinez un caractère: Vous avez %d essais"%essai)
    info_label=Label(r,textvariable=info,font=("Calibri",15),bg="#33FFE0",fg="#260E82")
    info_label.pack(pady=2)
    char_entry=Entry(r,font="Arial 12")
    char_entry.pack(ipady=3)
    verif_button=Button(r,text="Verifier",command=saisie_char,font="Candara 11 bold",bg="#F18E8E",fg="White")
    verif_button.pack(pady=10)
    statut=StringVar()
    statut_label=Label(r,textvariable=statut,font=("Calibri",15),bg="#33FFE0",fg="#260E82")
    quit_button=Button(r,text="Quitter",command=r.destroy,font="Candara 11 bold",bg="#F18E8E",fg="White")
    quit_button.pack(pady=10)
    r.mainloop()
