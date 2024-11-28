from Libro import Libreria
from Libro import Prestiti
from Libro import Primo
from Libro import Secondo
from Libro import Terzo
from Libro import Quarto
from Libro import Quinto
from Libro import Sesto
while(True):
    print("")
    print("MAIN MENU")
    print("Aggiungi Libro:1")
    print("Prestito Libro:2")
    print("Riporta Libro:3")
    print("Disponibilità Libro:4")
    print("Libreria:5")
    print("Prestiti:6") #Menu Principale
    print("Esci:7")
    x = int(input())
    if(x==1):
        Primo()
    elif(x==2):
        Secondo()
    elif(x==3):
        Terzo()
    elif(x==4):
        Quarto()
    elif(x==5):
        Quinto()
    elif(x==6):
        Sesto()
    elif(x==7):
        break
    else:
        ("Errore")