from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self):
        Mamifero._listado.append(self)

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    def cantidadMamiferos(self):
        return len(Mamifero._listado)
    
    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    @staticmethod
    def getListado():
        return Mamifero._listado
    def getPatas(self):
        return self._patas
    def isPelaje(self):
        return self._pelaje

    def setListado(self, listado):
        Mamifero._listado = listado
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def setPatas(self, patas):
        self._patas = patas