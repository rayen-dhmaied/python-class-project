from tkinter import*
from tkinter import simpledialog
from tkinter import messagebox

def saisie():
    while 1:
        N=simpledialog.askinteger("Jeu de tir a l’arc","Donner la nombre des joueurs : >= 2\t\t")
        if 2<=N:
            break
    return N

def tri():
    global dict_jr
    trie_dict={}
    trie_keys=sorted(dict_jr,key=dict_jr.get)
    for k in reversed(trie_keys):
        trie_dict[k]=dict_jr[k]
    dict_jr=trie_dict

def saisie_chaine():
    global info
    global dict_jr
    global ch
    global nb_essai
    ch=info_entry.get()
    if (all(c.isalpha() or c.isspace() for c in ch)) and ch[0].isupper() and ch.count(" ")==1 and ch[ch.find(" ")+1:].isupper():
        nb_essai=0
        dict_jr[ch]=0
        info.set("Donner L'essai "+str(nb_essai+1)+" de %s :"%ch)
        info_entry.delete(0,END)
        nom_button.forget()
        quit_button.forget()
        essai_button.pack(pady=10)
        quit_button.pack(pady=10)
    else:
        messagebox.showinfo("Jeu de tir a l'arc","Le nom de joueur doit etre sur la forme : 'Prenom NOM'")
        info_entry.delete(0,END)
        
def  affichage():
    global dict_jr
    classement=Frame(r,highlightthickness=1,highlightbackground="black",bg="#33FFEC")
    rangs=[]
    i=0
    for k in dict_jr:
        rangs.append(Label(classement,text=str(i+1)+" - "+k+" avec un score de "+str(dict_jr[k]),font=("Arial",13),bg="#33FFEC"))
        rangs[i].pack()
        i+=1
    classement.pack(pady=10)

def saisie_essai():
    global N
    global ch
    global nb_essai
    global dict_jr
    global nb_joueur
    es=int(info_entry.get())
    if 0<=es<=10:
        dict_jr[ch] += es
        info_entry.delete(0,END)
        nb_essai+=1
        info.set("Donner L'essai "+str(nb_essai+1)+" de %s :"%ch)
        if nb_essai==3:
            if  nb_joueur<N-1:
                nb_joueur+=1
                info.set("Donner le nom de joueur numero %d :"%(nb_joueur+1))
                essai_button.forget()
                quit_button.forget()
                nom_button.pack(pady=10)
                quit_button.pack(pady=10)
            else :
                tri()
                info.set("Classement :")
                essai_button.forget()
                nom_button.forget()
                info_entry.forget()
                quit_button.forget()
                affichage()
                quit_button.pack(pady=10)
    else :
        messagebox.showinfo("Jeu de tir a l’arc","L'essai ne peut pas etre plus de 10.")
        info_entry.delete(0,END)

def lancer():
    global r
    global N
    global info
    global info_label
    global info_entry
    global nom_button
    global essai_button
    global quit_button
    global dict_jr
    global ch
    global nb_joueur
    global nb_essai
    dict_jr={}
    ch=""
    nb_joueur=0
    nb_essai=0
    r=Tk()
    r.title("Jeu de tir a l’arc")
    r.geometry("500x300")
    r.config(background="#33FFE0")
    titre=Label(r,text="Jeu de tir a l’arc",font=("Cambria",20),fg="blue",bg="#33FFE0")
    titre.pack()
    N=saisie()
    info=StringVar()
    info.set("Donner le nom de joueur numero %d :"%(nb_joueur+1))
    info_label=Label(r,textvariable=info,font=("Calibri",15),bg="#33FFE0",fg="#260E82")
    info_label.pack(pady=2)
    info_entry=Entry(r,width=32,font="Arial 12")
    info_entry.pack(ipady=3)
    nom_button=Button(r,text="Saisir Nom",command=saisie_chaine,font="Candara 11 bold",bg="#F18E8E",fg="White")
    nom_button.pack(pady=10)
    essai_button=Button(r,text="Saisir Essai",command=saisie_essai,font="Candara 11 bold",bg="#F18E8E",fg="White")
    quit_button=Button(r,text="Quitter",command=r.destroy,font="Candara 11 bold",bg="#F18E8E",fg="White")
    quit_button.pack(pady=10)
    r.mainloop()
