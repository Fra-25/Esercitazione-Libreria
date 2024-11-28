Libreria = []
Prestiti = []

def Primo():
    print("Che libro vuoi aggiungere alla Libreria?")
    Libro1 = input()
    Libreria.append(Libro1) #Aggiungi Libro
    print(Libro1,"è stato aggiunto alla Libreria")

def Secondo():
        print("Che libro è stato preso in prestito?")
        Libro2 = input()
        if(Libro2 in Libreria):
            Prestiti.append(Libro2) #Prestito Libro
            Libreria.remove(Libro2)
            print(Libro2, "è stato prestato")
        else:
            print("Questo libro non è disponibile")

def Terzo():
        print("Che libro è stato riportato?")
        Libro3 = input()
        Prestiti.remove(Libro3)
        Libreria.append(Libro3)
        print(Libro3 , "è stato restituito") #Riporta Libro
        if(Libro3 not in Prestiti):
             print("Questo libro non è stato preso in prestito")

def Quarto():
        print("Di quale libro vuoi verificare la disponibilità?")
        Libro4 = input()
        if(Libro4 in Libreria):
            print("Questo libro è disponibile")
        elif(Libro4 in Prestiti):
            print("Questo libro è stato preso in prestito")
        else:
            print("Questo libro non è disponibile") #Disponibilità Libro

def Quinto():
    print("Libreria")
    print(Libreria) #Libri disponibili nella Libreria

def Sesto():
    print("Prestiti")
    print(Prestiti) #Libri dati in prestito