import es2_classi as l

class Biblioteca:
    def __init__(self):
        self.libri = [] 

    def aggiungi_libro(self, titolo, autore, pagine):
        libro = l.Libro(titolo, autore, pagine)
        self.libri.append(libro)

    def stampa_libri(self):
        for i in self.libri:
            print(i.descrizione())

    def crea_libri(self):
        numero_libri = int(input("inserisci numero libri da stampare: "))
        for i in range(numero_libri):
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            pagine = int(input("Inserisci il numero di pagine: "))
            
            self.aggiungi_libro(titolo, autore, pagine)

        print("Ecco i libri nella biblioteca:")
        self.stampa_libri()


biblioteca = Biblioteca()
biblioteca.crea_libri()
