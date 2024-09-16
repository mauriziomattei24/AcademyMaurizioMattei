def UML():
    print("UML (Unified Modeling Language) è un linguaggio standardizzato per visualizzare, specificare, costruire e documentare i componenti di un sistema software tramite diagrammi.")

def ciclo_for():
    stringa = "cicli"
    for lettera in stringa:
        print(f"Usando il for ti stampa tutte le lettere della stringa:questa è la {stringa[lettera]} {lettera}")

def ciclo_while():
    stringa = "cicli"
    indice = 0
    while indice < len(stringa):
        print(f"Usando il while ti stampa tutte le lettere della stringa: questa è la {stringa[indice]} all'indice {indice}")
        indice += 1


def condizioni():
    condizione_if = input("scrivi SI oppure NO: ")
    if condizione_if == "SI":
        print("sei nell'if")
    elif condizione_if == "NO":
        print("sei in elif")
    else:
        print("sei nell'else")


def liste():
    spiegazione = ("Le liste in Python sono una struttura dati che può contenere una raccolta ordinata di elementi")
    lista = spiegazione.split()
    print(lista)

def metodologie():
    scelta = input("scegli metodologia: ")
    waterfall = "La metodologia Waterfall è un approccio di sviluppo software sequenziale in cui ogni fase del progetto deve essere completata prima di passare alla successiva, con poca flessibilità per cambiamenti successivi"
    agile = "La metodologia Agile è un approccio iterativo e incrementale che favorisce la collaborazione continua, adattamento ai cambiamenti e lo sviluppo in brevi cicli chiamati sprint per fornire valore rapidamente"
    if scelta == "waterfall":
        print(waterfall)
    elif scelta == "agile":
        print(agile)




