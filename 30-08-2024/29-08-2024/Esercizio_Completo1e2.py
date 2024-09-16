#1 scrivi un sistema che prende un numero e stampa "Pari" o è "Dispari"
numero = int(input("Inserisci un numero"))

if numero%2 == 0:
    print("Numero pari")
else:
    print("Numero dispari")

#2 while e range
# Dato un numero stampare i numeri da numero a 0 decrementando di 1. Deve potersi ripetere all'inifnito

while True:
    # inserire numero
    numero = int(input("Inserisci un numero: "))
    # conto alla rovescia
    for i in range(numero, -1, -1):
        print(i)
    # ripetere
    ripeti = input("Vuoi ripetere?: ")
    if ripeti != "si":
        print("Fine")
        break
    
    

