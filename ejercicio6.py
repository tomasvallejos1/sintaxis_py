#Reducción personalizada:
#Usa reduce para multiplicar todos los elementos de una lista de números.
from functools import reduce
lista = [20,3,2,3,4]

Nlist = reduce(lambda x,y: x * y, lista)
print(Nlist)
