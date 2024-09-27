# Esercizio 1: Oggetti
# 
# Descrizione:  Crea un programma in Python per gestire una semplice libreria di libri. 
# Il programma dovrebbe presentare un menu all'utente con le seguenti opzioni:
# 
# Aggiungere un nuovo libro: L'utente può inserire il titolo, l'autore e l'anno di pubblicazione del libro e quantità.
# 
# Visualizzare tutti i libri: Mostra una lista di tutti i libri attualmente nella libreria.
# 
# Cercare un libro per titolo: L'utente inserisce un titolo e il programma cerca e mostra i dettagli del libro se trovato.
# 
# Gestione libri: Far rimuovere modificare e/o aggiungere una copia in più del libro
# 
# Uscire dal programma: Termina l'esecuzione del programma.

class Libro:
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Quantità: {self.quantita}"


class Libreria:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, titolo, autore, anno, quantita):
        nuovo_libro = Libro(titolo, autore, anno, quantita)
        self.libri.append(nuovo_libro)
        print("libro aggiunto")

    def visualizza_libri(self):
        if not self.libri:
            print("nessun libro trovato")
        else:
            print("lista dei libri:")
            for libro in self.libri:
                print(libro)

    def cerca_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo:
                return libro
        return None

    def gestione_libri(self, titolo):
        libro = self.cerca_libro(titolo)
        print("Libro trovato")
        print("1. rimuovere il libro")
        print("2. modificare il libro")
        print("3. aggiungere una copia in più")
        scelta = input("Scegli un'opzione (1, 2, 3): ")

        if scelta == '1':
            self.libri.remove(libro)
            print("libro rimosso")
        elif scelta == '2':
            nuovo_titolo = input("Inserisci il nuovo titolo: ")
            nuovo_autore = input("Inserisci il nuovo autore: ")
            nuovo_anno = input("Inserisci il nuovo anno di pubblicazione: ")
            nuova_quantita = int(input("Inserisci la nuova quantità: "))
            libro.titolo = nuovo_titolo
            libro.autore = nuovo_autore
            libro.anno = nuovo_anno
            libro.quantita = nuova_quantita
            print("libro modificato")
        elif scelta == '3':
            libro.quantita += 1
            print("copia del libro aggiunta")
        else:
            print("scelta non valida")
        

    def menu(self):
        while True:
            print("1. Aggiungere un nuovo libro")
            print("2. Visualizzare tutti i libri")
            print("3. Cercare un libro per titolo")
            print("4. Gestione libri")
            print("5. Uscire dal programma")

            scelta = input("Scegli un'opzione (1-5): ")

            if scelta == '1':
                titolo = input("Inserisci il titolo del libro: ")
                autore = input("Inserisci l'autore del libro: ")
                anno = input("Inserisci l'anno di pubblicazione: ")
                quantita = int(input("Inserisci la quantità: "))
                self.aggiungi_libro(titolo, autore, anno, quantita)
            elif scelta == '2':
                self.visualizza_libri()
            elif scelta == '3':
                titolo = input("Inserisci il titolo del libro da cercare: ")
                libro = self.cerca_libro(titolo)
                print(libro)
            elif scelta == '4':
                titolo = input("Inserisci il titolo del libro da gestire: ")
                self.gestione_libri(titolo)
            elif scelta == '5':
                break
            else:
                print("scelta non valida,riprova")

libreria = Libreria()
libreria.menu()