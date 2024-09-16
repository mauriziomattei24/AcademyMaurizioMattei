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

