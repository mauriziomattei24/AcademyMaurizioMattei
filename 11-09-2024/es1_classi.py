# Esercizio 1 (Facile):
# Crea una classe chiamata Punto. Questa classe dovrebbe avere:
# Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
# Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
# coordinate del punto di questi valori.
# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
# piano.





import math as m
class Punto: 
 def __init__(self,x,y):
   self.x = x
   self.y = y

 def muovi(self, dx, dy): 
   self.x = self.x + dx 
   self.y = self.y + dy 

 def distanza_da_origine(self): 
   distanza = m.sqrt(self.x**2 + self.y**2)
   return distanza
 

 
p = Punto(3, 4)
print(f"coordinate iniziali: {p.x}, {p.y}")

p.muovi(2, 1)
print(f"nuove coordinate: {p.x}, {p.y}")

distanza = p.distanza_da_origine()
print(f"distanza dall'origine: {distanza}")