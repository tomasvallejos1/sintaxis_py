from functools import reduce #para poder usar el reduce

#09-functtions.py


print("\n ***Closures***")

#funcion closure

def suma_diez(y): #Funcion externa
    def suma(x): #Funcion interna o closure
        return y + x + 10
    return suma

sumar = suma_diez(5)
print(sumar(2)) #la funcion recuerda el y, luego le suma el x (2)

print(suma_diez(5)(2)) #tambien se puede usar asi, pero pierde sentido

#Ejemplo practico

def crear_saludo(saludo):
    def saludar(nombre):
        return f"{saludo}, {nombre}"
    return saludar


saludo_generico = crear_saludo("Hola como estas")
saludo_formal = crear_saludo("Buenos días estimado")

print(saludo_generico("Mj"))
print(saludo_formal("Mar"))

print("\n ________________________________\n")
#Built-in high order functions, ya vienen definidas por python
#map,filter,reduce,zip, enumerate,sorted,etc

lista = [2,3,42,1,9]
lista2 = ['a','b','c','d','e']
#1
print("\n -- map -- \n")
print(list(map(lambda x: x*2, lista)))  #La funcion list convierte un iterable en lista

#2
print("\n -- filter -- \n")

print(list(filter(lambda x: x % 2 == 0, lista)))
#3
print("\n -- reduce -- \n")

print(reduce(lambda x,y: x + y, lista))

#4
print("\n -- zip -- \n")

print(list(zip(lista2, lista)))

#5
print("\n -- sorted -- \n")

print(list(sorted(lista, reverse=True)))

#6
print("\n -- enumerate -- \n")

print(list(enumerate(lista)))
