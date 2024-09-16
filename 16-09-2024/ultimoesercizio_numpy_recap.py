import numpy as np

def creare_matrice(dimensioni):
    return np.random.randint(1, 10, size=dimensioni)

def trasporre_matrice(matrice):
    return np.transpose(matrice)

def calcolare_somma(matrice):
    return np.sum(matrice)

def calcolare_media(matrice):
    return np.mean(matrice)



def menu():
    matrice = None
    while True:
        print("\nMenu:")
        print("1. Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.")
        print("2. Trasporre la matrice e stamparla.")
        print("3. Calcolare e stampare la somma di tutti gli elementi della matrice.")
        print("4. Calcolare e stampare la media di tutti gli elementi della matrice.")
        print("5. Uscire dal programma.")
        
        scelta = input("Seleziona un'opzione (1-5): ")
        
        if scelta == '1':
            righe = int(input("Inserisci il numero di righe: "))
            colonne = int(input("Inserisci il numero di colonne: "))
            matrice = creare_matrice((righe, colonne))
            print("matrice creata:")
            print(matrice)
        
        elif scelta == '2':
            if matrice is not None:
                matrice_trasposta = trasporre_matrice(matrice)
                print("matrice trasposta:")
                print(matrice_trasposta)
            else:
                print("nessuna matrice disponibile")
        
        elif scelta == '3':
            if matrice is not None:
                somma = calcolare_somma(matrice)
                print("somma di tutti gli elementi della matrice: ")
                print(somma)
            else:
                print("nessuna matrice disponibile")
        
        elif scelta == '4':
            if matrice is not None:
                media = calcolare_media(matrice)
                print("media di tutti gli elementi della matrice: ")
                print(media)
            else:
                print("nessuna matrice disponibile")

        elif scelta == '5':
            print("Esci dal programma")
            break

        
        else:
            print("opzione non valida. Seleziona un'opzione tra 1 e 5")

menu()
