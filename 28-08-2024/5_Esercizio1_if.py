# Esercizio 1 slide 71
importo = 5
if importo < 1000:
  print("Bonifico")
  if importo < 500:
    print("Bonifico istantaneo")
    if importo == 0:
      print("Bancarotta")
else:
  print("Blocco")




x = int(input('Digita un numero: '))
count = 0
s = 'ciao'
b = False


if x % 2 == 0:
    count+= 1
    if count > 0:
        b = True
        if not(b == False):
            print(s.replace('ciao','End'))
        else:
            print('La variabile booleana è False')
    else:
        print('Il contatore non è maggiore di 0')
else:
    print('Il numero è dispari')


