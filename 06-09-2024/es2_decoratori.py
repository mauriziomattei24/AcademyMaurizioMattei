def decoratore(funz):
    def wrapper(numero):
        print(f"Sto verificando se {numero} è un numero primo")
        risultato = funz(numero)  
        return risultato
    return wrapper

@decoratore
def primo_o_no(numero):
    for i in range(2, numero - 1):
        if numero % i == 0: 
            return False 
        else:
            print("il numero è primo")
            return True
        
def esercizio():
    lista_numeri_primi = []
    while True:
        numero = int(input("inserisci numero: "))
        return_primo = primo_o_no(numero)
        if return_primo == True:
            lista_numeri_primi.append(numero)
            print(lista_numeri_primi)
        else:
            count = 0
            if numero%2==0:
                divisore = 2
            else:
                divisore = 3

            while numero % divisore == 0:
                count+= 1
                numero //= divisore
                print((count))

esercizio()




        

