from tkinter import*
from tkinter import messagebox
from random import randint

def fin_jeu(x):
    if x:
        msg="Bravo vous avez gagnée ! :)"
    elif not x:
        msg="Tu as perdu ! :( Bonne chance la prochaine fois."
    messagebox.showinfo("Fin jeu",msg)
    debut.forget()
    cpu_label.forget()
    allum_choisi_entry.forget()
    allum_choisi_button.forget()
    quitter_jeu.pack(pady=70)

def choisir_verif(x):
    global allum_choisi
    global num_allum
    if x==0:
        while 1:
            allum_choisi=randint(1,3)
            if num_allum-allum_choisi>=0:
                tour_cpu()
                break
    elif x==1:
        allum_choisi=int(allum_choisi_entry.get())
        if allum_choisi in [1,2,3] and num_allum-allum_choisi>=0:
            tour_humain()
        else:
            messagebox.showinfo("Mauvais Choix","Veuillez choisir moins de 3 allumettes et moins que les allumettes restantes!")

def tour_cpu():
    global info
    global allum_choisi
    global num_allum
    num_allum-=allum_choisi
    info.set("Je prends "+str(allum_choisi)+" allumette(s). Il en reste "+str(num_allum))
    if num_allum==0:
        fin_jeu(1)

def tour_humain():
    global allum_choisi
    global num_allum
    num_allum-=allum_choisi
    if num_allum==0:
        fin_jeu(0)
    elif num_allum!=0:
        choisir_verif(0)
    
def lancer():
    global r
    global info
    global debut
    global cpu_label
    global allum_choisi_entry
    global allum_choisi_button
    global quitter_jeu
    global num_allum
    global allum_choisi
    num_allum=randint(20,70)
    allum_choisi=0
    r=Tk()
    r.title("Jeu d'allumettes")
    r.geometry("300x200")
    r.config(background="#33FFE0")
    debut=Label(r,text="Jeu avec "+str(num_allum)+" Allumettes",font=("Cambria",15),fg="blue",bg="#33FFE0")
    debut.pack()
    info=StringVar()
    choisir_verif(0)
    cpu_label=Label(r,textvariable=info,font=("Calibri",13),fg="#FF3383",bg="#33FFE0")
    cpu_label.pack()
    allum_choisi_entry=Entry(r,font="Arial 12",width=14)
    allum_choisi_entry.pack()
    allum_choisi_button=Button(r,text="Choisir Allumettes",font="Candara 11 bold",bg="#F18E8E",fg="White",command=lambda :choisir_verif(1))
    allum_choisi_button.pack(pady=10)
    quitter_jeu=Button(r,text="Quitter",command=r.destroy,font="Candara 11 bold",bg="#F18E8E",fg="White")
    quitter_jeu.pack(pady=10)
    r.mainloop()
