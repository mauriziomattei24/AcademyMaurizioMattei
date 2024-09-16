# 3

lista = [] #inizializzo
while True: #ciclo
    numero = int(input("inserisci numero: ")) 
    lista.append(numero) # aggiungo uno alla volta i numeri
    for i in lista: 
        print(i**2) # stampo il quadrato
    scelta = input("vuoi inserire un altro numero? ") 
    if scelta != "si":
        break