#! /usr/bin/pyhton3

from itertools import count
class gato:
    
    __count = count(0) # ,, self.id

    _nombre = None
    _saciado = False
    
    def __init__(self, nom = "kitt"):
        self.id = next(self.__count)
        self._nombre = nom 
        print(f"{self._nombre}: meaow!")

    def __str__(self) -> str:
        return f"{self.id}: meaow"

    def comer(self, comida = "pienso"):
        self._saciado = True

    def dormir(self):
        self._saciado = False
        
    def tocar(self):
        if self._saciado: 
            print("dejame en paz, esclavo")
        else:
            self.pedirComida()

    def pedirComida(self):
        print(f"{self._nombre}: dame mi comida, esclavo")
        
if __name__ == "__main__":

    g1 = gato("Noche")
    g2 = gato("Bamban")
    
    print(g1)
    print(g2)    
    g1.pedirComida()
    g1.tocar()
    g1.comer()    
    g1.tocar()
