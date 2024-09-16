
def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_quadrato(lato):
    return lato * lato

def area_rettangolo(base, altezza):
    return base * altezza

def calcolo_aree():
    risultati=[]
    while True:
        scelta = int(input("scegli una forma geometrica: 1.triangolo 2.quadrato 3.rettangolo: "))
        if scelta == 1:
            base_triangolo = input("inserisci la base: ")
            altezza_triangolo = input("inserisci l'altezza")
            area_triangolo = area_triangolo(base_triangolo,altezza_triangolo)
            risultati.append(area_triangolo)
            print(area_triangolo)
        
        elif scelta == 2:
            lato_quadrato = int(input("inserisci il lato: "))
            area_quadrato = area_quadrato(lato_quadrato)
            risultati.append(area_quadrato)
            print(area_quadrato)
        
        elif scelta == 3:
            base_rettangolo = input("inserisci la base: ")
            altezza_rettangolo = input("inserisci l'altezza")
            area_rettangolo = area_rettangolo(base_rettangolo,altezza_rettangolo)
            risultati.append(area_rettangolo)
            print(area_rettangolo)

calcolo_aree()


    

    





