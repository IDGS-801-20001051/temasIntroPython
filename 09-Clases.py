class OperasBas:
    #declaración de propiedades
    #public es normal
    num1=0
    num2=0
    #private _
    #protected __
    res=0
    
    #declaración del constructor this = self
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2


    #declaración de metodos de clase
    def suma(self):
        self.res=self.num1 + self.num2
        print("La sumas es: {}".format(self.res))

    def resta(self):
        self.res=self.num1 - self.num2
        print("La sumas es: {}".format(self.res))

def main():
        obj=OperasBas(3,4)
        obj.suma()

if __name__ == "__main__":
        main()



