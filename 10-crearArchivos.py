from io import open
import math

#w archivo distinro  a modifica el mismo archivo o lo crea   r para leer
lectura=""
texto = open("archivo.txt","r")
lectura=texto.readlines()
print(type(lectura))
print(lectura)

for i in lectura:
    print(i)
#texto.write("Hola, Mundo\n")
texto.close()

