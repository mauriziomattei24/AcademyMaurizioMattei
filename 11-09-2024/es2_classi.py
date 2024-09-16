# Esercizio 2 (Facile):
# Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto
# da 'autore' e ha 'pagine' pagine.

class Libro: 
 def __init__(self,titolo,autore,pagine):
    self.titolo = titolo
    self.autore = autore
    #controllo che sia un intero
    if type(pagine) == int:
        self.pagine = pagine
    else:
        print("valore di pagine non valido, impostato a 0")
        self.pagine = 0 

 
 def descrizione(self): 
   print(f"il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine")
   


# libro1 = Libro("Manuale d'uso delle classi","Maurizio Mattei",57)
# libro1.descrizione()

# libro2 = Libro("Manuale d'uso delle classi","Maurizio Mattei","ciao")
# libro2.descrizione()
