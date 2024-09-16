### continue
numeri = [1,2,3,4,5]
for i in numeri:
    if i == 3:
        continue
    print(i)

### pass
for i in range(5):
    if i == 3:
        pass
    print(i)

### slpat *
# L'operatore * in Python è noto come operatore di "splat". 
# Viene utilizzato per espandere un iterabile (come una lista, una tupla o un range) in elementi separati. 
# Ecco un esempio:

numeri = [*range(1,11)]
print(numeri)

#In questo caso, [*range(1, 11)] espande la sequenza di numeri generati da range(1, 11) nella lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
# L'operatore * svolge il ruolo di "splat", consentendo di trattare gli elementi dell'iterabile come elementi separati nella lista.