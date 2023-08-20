from ex_pack import*
from sys import argv
import ctypes

if int(argv[1]) !=0:
    if int(argv[1])==1:
        exercice_1.lancer()
    elif int(argv[1])==2:
        exercice_2.lancer()
    elif int(argv[1])==3:
        exercice_3.lancer()
    elif int(argv[1])==4:
        exercice_4.lancer()
    elif int(argv[1])==5:
        exercice_5.lancer()
    elif int(argv[1])==6:
        exercice_6.lancer()
    elif int(argv[1])==7:
        exercice_7.lancer()
    elif int(argv[1])==8:
        exercice_8_cli.lancer()
    elif int(argv[1])==9:
        exercice_9_cli.lancer()
    elif int(argv[1])==10:
        exercice_10_cli.lancer()
    print("Appuyez sur enter pour revenir au menu général.")
    input()
elif int(argv[1]) ==0:
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)
    if int(argv[2])==8:
        exercice_8_gui.lancer()
    elif int(argv[2])==9:
        exercice_9_gui.lancer()
    elif int(argv[2])==10:
        exercice_10_gui.lancer()
