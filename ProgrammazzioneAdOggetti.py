#Programmazione ad oggetti e Classi

class Triangle:

    #possiamo documentare una classe cosa utile se la classe è molto complessa usando le doc sring
    """Questa classe rappresenta un triangolo"""

    def __init__(self,a,b,c,h):
        self.a, self.b, self.c, self.h=a,b,c,h

    def area(self): #self è una variabile che ci permette di identificare le funzioni, metodi e parametri della classe stessa
        """Calcolo dell'area"""
        return self.b*self.h/2

    def perimetro(self):
        """Calcolo del perimetro"""
        return self.a+self.b+self.c

    def print_info(self):
        """Stampa le info"""
        print("Area del triangolo = %.2f"%self.area())
        print("Perimetro del triangolo = %.2f" % self.perimetro())

triangle=Triangle(4,3,8,5)
triangle.area()
triangle.perimetro()
triangle.print_info()

#possiamo ottenere informazioni sulla classe che rappresenta l'oggetto
help(triangle)