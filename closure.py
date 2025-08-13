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