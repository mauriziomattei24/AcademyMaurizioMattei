lista = [] #inizializzo
len = int(input("inserisci lunghezza lista: ")) 
for i in range(len):
    num = int(input("inserisci numero: ")) 
    lista.append(num) # aggiungo uno alla volta i numeri
scelta = input("Vuoi aggiungere un altro numero? ")
if scelta != "si":
    print("il massimo della lista è ", max(lista))

conteggio = 0    
while conteggio!=len:
    conteggio += 1
    print(conteggio)

if len == 0:
    print("Lista Vuota")
else:
    print("il massimo della lista è ", max(lista))
    print(conteggio)


       
    
        





