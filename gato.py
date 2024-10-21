#! /usr/bin/pyhton3

from itertools import count
class gato:
    
    __count = count(0) # ,, self.id
    __nombr = None
    __saciado = False
    
    def __init__(self, nom = "kitt"):
        self.id = next(self.__count)
        self.__nombr = nom 
        print(f"{self.__nombr}: meaow!")

    def __str__(self) -> str:
        return f"{self.id}: meaow"

    def comer(self, comida = "pienso"):
        self.saciado = True

    def dormir(self):
        self.saciado = False
        
    def tocar(self):
        if self.__saciado: 
            print("dejame en paz, esclavo")
        else:
            self.pedirComida()

    def pedirComida(self):
        print(f"{self.__nombr}: dame mi comida, esclavo")
        
if __name__ == "__main__":

    g1 = gato("Noche")
    g2 = gato("Bamban")
    
    print(g1)
    print(g2)    
    g1.pedirComida()
    g1.tocar()
    g1.comer()    
    g1.tocar()
