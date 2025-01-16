'''x = 0



while x<10:
    print(x)
    x=x+1


operacion de multiplicaion de a * b utilizando sumas
    a=3
    b=4
    salidad:3+3+3+3=12
'''

print('Dame un numero para sumarlo así mismo')
a = int(input('Ingrese un número: '))
b = int(input('Ingrese el número de veces que quieras sumarlo: '))

res = 0

x = 1
while x <= b:
    res += a
    x += 1

print(f"El resultado es = {res}")


