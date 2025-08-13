#Transformación de cadenas:
#Usa map y una función lambda para convertir todas las palabras 
# de una lista de strings a mayúsculas.

lista = ['a','b','c','d']
fun = lambda x: list(map(lambda x: x.upper(),x))

print(fun(lista))