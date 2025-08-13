#Filtrado de múltiplos:
#Dada una lista de números, usa filter y una función lambda para 
# obtener una lista solo con los múltiplos de 4.


lista = [1,12,3,2,20,24,5]


func = lambda x: list(filter(lambda x: x % 4 == 0, x))

print(func(lista))