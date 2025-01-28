import math

class Distancia:
    x1=0
    x2=0
    y1=0
    y2=0
    raiz=0

    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def distancia(self):
        self.raiz = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print("La distancia es: {}".format(self.raiz))

    def pedir(self):
        self.x1=int(input('X 1: '))
        self.x2=int(input('X 2: '))
        self.y1=int(input('Y 1: '))
        self.y2=int(input('Y 2: '))


def main():
    obj = Distancia()
    obj.pedir()
    obj.distancia()

if __name__ == "__main__":
        main()
        
