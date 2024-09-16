# Esercizio 2 slide 2

stringa = input("inserire testo: ")

# menu
print("Menu:")
print("Aggiungi")
print("Rimuovi")
print("Elimina")
print("Esci")

scelta = input("Seleziona un'opzione: ")

if scelta == "Aggiungi":
    testo_da_aggiungere = input("Inserisci il testo da aggiungere: ")
    stringa += testo_da_aggiungere
    print("Stringa aggiornata:", stringa)
elif scelta == "Rimuovi":
    testo_da_rimuovere = input("Inserisci il testo da rimuovere: ")
    stringa = stringa.replace(testo_da_rimuovere, "")
    print("Stringa aggiornata:", stringa)
elif scelta == "Elimina":
    stringa = ""
    print("Stringa eliminata.")
else:
    print("Uscita dal programma.")
