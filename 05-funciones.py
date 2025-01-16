import os

def function1():
    os.system('cls')
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))
    res = num1+num2;
    print(f'Resultado: {res}')


def function2():
    os.system('cls')
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))
    res = num1-num2;
    print(f'Resultado: {res}')

def function3():
    os.system('cls')
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))
    res = num1*num2;
    print(f'Resultado: {res}')

def function4():
    os.system('cls')
    num1=int(input('Numero1: '))
    num2=int(input('Numero2: '))
    res = num1/num2;
    print(f'Resultado: {res}')


def run():
    x=0
    while x !=5:
        
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Salir')
        op=int(input('Opcion: '))
        os.system('cls')
        if op==1:
            function1()
        if op==2:
            function2()
        if op==3:
            function3()
        if op==4:
            function4()
        x=op


if __name__ == "__main__":
    run()