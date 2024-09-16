lista1 = []
lista2 = []
for i in range(1,6):
    numero1 = int(input("inserisci numero: "))
    lista1.append(numero1)
    numero2 = int(input("inserisci numero: "))
    lista2.append(numero2)
print(lista1)
print(lista2)
somma = []
for i in range(5):
    somma.append(lista1[i] + lista2[i])
print(somma) 