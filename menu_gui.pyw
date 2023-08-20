from tkinter import*
from tkinter import messagebox
from os import system

r=Tk()
r.title("Mini Projet TP7")
r.geometry("300x580")
r.config(background="#33FFE0")

frame=Frame(r,highlightthickness=1,highlightbackground="black",bg="#33FFEC")
menu=Label(frame,text="MENU GENERAL",font="Andalus 20 bold",fg="#501246",bg="#33FFEC")
menu.pack()
frame.pack(pady=20)

def lancer(m):
    if m in[8,9,10]:
        reponse=messagebox.askquestion("Mode Jeu","Souhaitez-vous démarrer le jeu en mode graphique ?")
        if reponse== "yes":
            system("lancer_dont_touch.py 0 "+str(m))
        else:
            system("lancer_dont_touch.py "+str(m))
    else:
        system("lancer_dont_touch.py "+str(m))

buttons=[]
for i in range(11):
    if i+1==11:
        buttons.append(Button(r,text="QUITTER", command=r.destroy,font="Cambria 11 bold",bg="#944187",fg="White",width=10))
    else:
        buttons.append(Button(r,text="EXERCICE "+str(i+1), command=lambda i=i+1 :lancer(i) ,font="Cambria 11 bold",bg="#944187",fg="White",width=10))
    buttons[i].pack(pady=5)

nom=Label(r,text="Preparé par Rayen DHMAIED\nProposé par Mr. Kais BEN SALAH",font="Courier 11 bold",fg="Black",bg="#33FFE0")
nom.pack(pady=10)

r.mainloop()
