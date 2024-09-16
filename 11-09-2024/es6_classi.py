class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita)
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione






############################################################################
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        Prodotto.__init__(self,nome,costo_produzione,prezzo_vendita)
        self.garanzia = garanzia

   

    def descrizione(self):
        return f"{self.nome}, con {self.garanzia} anni di garanzia"


############################################################################
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def descrizione(self):
        return f"{self.nome}, fatto di {self.materiale}"


############################################################################
class Fabbrica:
    def __init__(self):
        self.inventario = {}

# ---

    def aggiungi_prodotto(self, nome_prodotto, quantita):

        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]['quantita'] += quantita
        else:
            self.inventario[nome_prodotto] = {'prodotto': nome_prodotto, 'quantita': quantita}
        print(f"aggiunte {quantita} unità di {nome_prodotto} all'inventario")

# ---

    def vendi_prodotto(self, nome_prodotto, quantita):
        if nome_prodotto in self.inventario and self.inventario[nome_prodotto]['quantita'] >= quantita:
            prodotto = self.inventario[nome_prodotto]['prodotto']
            self.inventario[nome_prodotto]['quantita'] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            print(f"vendute {quantita} unità di {nome_prodotto}. Profitto: {profitto} euro")
        else:
            print(f"quantità insufficiente di {nome_prodotto} in inventario o prodotto non trovato")

# ---

    def stampa_inventario(self):
        for chiave, valore in self.inventario.items():
            print(f"{chiave}: {valore['quantita']} unità disponibili")



tv = Elettronica("televisore", 200, 500, 2)
maglietta = Abbigliamento("maglietta", 10, 25, "Cotone")
computer = Elettronica("computer", 400, 1000, 3)

fabbrica = Fabbrica()

fabbrica.aggiungi_prodotto(tv, 10)
fabbrica.aggiungi_prodotto(maglietta, 50)
fabbrica.aggiungi_prodotto(computer, 5)

fabbrica.stampa_inventario()

fabbrica.vendi_prodotto("televisore", 3)
fabbrica.vendi_prodotto("maglietta", 20)

fabbrica.stampa_inventario()

