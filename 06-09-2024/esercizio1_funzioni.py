# esercizio 1
import random
def genera_numero_casuale(a,b):
    numero_casuale = random.randint(a,b)
    return numero_casuale



def tentativo_funz(numero_casuale):
    tentativo = 0
    while tentativo != numero_casuale:
        tentativo = int(input("Prova ad indovinare il numero: "))
        if tentativo > numero_casuale:
         print("il numero scelto è troppo alto")
        elif tentativo < numero_casuale:
         print("il numero è troppo basso")
        else:
         print("Il numero è corretto")
         break
   

def gioca():
    numero_casuale = genera_numero_casuale(1,100)
    tentativo_funz(numero_casuale)

gioca()

    








