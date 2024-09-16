while True:
    numero = int(input("Inserisci un numero: "))
    lista = [1,numero]
    numeri_primi= []
    for i in range(numero,0,-1):
        if numero%i !=0:
            numeri_primi.append(numero)
            

