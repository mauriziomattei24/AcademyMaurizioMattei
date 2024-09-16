class Ristorante:
    def __init__(self,nome,tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False

    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} propone prevalentemente cucina {self.tipo_cucina}")

    def stato_apertura(self):
        stato = "aperto" if self.aperto == True else "chiuso"
        print(stato)

    def apri_ristorante(self):
        aperto = True
        print("il ristorante è ora aperto")

    def chiudi_ristorante(self):
        aperto = False
        print("il ristorante è ora chiuso")

    def aggiungi_al_menu(self,menu):
        self.menu = menu
        numero_piatti_aggiuntivi = int(input("quanti piatti vuoi inserire nel menu? "))
        for i in range(numero_piatti_aggiuntivi):
            nuovo_piatto = input("inserisci un nuovo piatto: ")
            if nuovo_piatto in self.menu:
                print("piatto già presente nel menu")
            else:
                self.menu.append(nuovo_piatto)

    def togli_dal_menu(self,menu):
        self.menu = menu
        numero_piatti_da_togliere = int(input("quanti piatti vuoi togliere dal menu? "))
        for i in range(numero_piatti_da_togliere):
            piatto_da_togliere = input("inserisci piatto da togliere: ")
            if piatto_da_togliere in self.menu:
                self.menu.remove(piatto_da_togliere)
            else:
                print("il piatto non era presente nel menu prima dell'operazione")
    
    def stampa_menu(self):


Risto = Ristorante("Barca","Pesce")
# Risto.descrivi_ristorante()
# Risto.stato_apertura()
# Risto.apri_ristorante()
Risto.chiudi_ristorante()
Risto.aggiungi_al_menu(["Orata","Spigola", "Polpo"])
Risto.togli_dal_menu(["Orata","Spigola", "Polpo"])




    
            


