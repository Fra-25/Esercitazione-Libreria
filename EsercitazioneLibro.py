from Libro import Libreria
from Libro import Prestiti
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
        print("Che libro vuoi aggiungere alla Libreria?")
        Libro1 = input()
        Libreria.append(Libro1) #Aggiungi Libro
        print(Libro1,"è stato aggiunto alla Libreria")
    elif(x==2):
        print("Che libro è stato preso in prestito?")
        Libro2 = input()
        if(Libro2 in Libreria):
            Prestiti.append(Libro2) #Prestito Libro
            Libreria.remove(Libro2)
            print(Libro2, "è stato prestato")
        else:
            print("Questo libro non è disponibile")
    elif(x==3):
        print("Che libro è stato riportato?")
        Libro3 = input()
        Prestiti.remove(Libro3)
        Libreria.append(Libro3)
        print(Libro3 , "è stato restituito") #Riporta Libro
    elif(x==4):
        print("Di quale libro vuoi verificare la disponibilità?")
        Libro4 = input()
        if(Libro4 in Libreria):
            print("Questo libro è disponibile")
        elif(Libro4 in Prestiti):
            print("Questo libro è stato preso in prestito")
        else:
            print("Questo libro non è disponibile") #Disponibilità Libro
    elif(x==5):
        print("Libreria")
        print(Libreria) #Libri disponibili nella Libreria
    elif(x==6):
        print("Prestiti")
        print(Prestiti) #Libri dati in prestito
    elif(x==7):
        break
    else:
        ("Errore")