#Imprimir nombre

#Cadena de caracteres
nombre = input("Introduce tu nombre")
print(f"Hola {nombre}")
print("Hola, {}".format(nombre))

# entero
edad=19

#flotante - decimales
altura=1.75

#  Convertir flotante
edadString = str(edad) 

print(edad+edad)
print(edadString+edadString)

print(type(edad))

tuEdad = input("Introduce tu edad: ")
tuEdad = int(tuEdad)

#if
if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad >= 200:
    print("¿Eres inmortal?")
elif tuEdad <=0:
    print("No existes")
else:
    print("Eres menor de edad")

#for
for i in range(0,10):
    print(i)

#switch, no hay switch en piton
