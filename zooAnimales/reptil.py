from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    _listado = []

    def __init__(self):
        Reptil._listado.append(self)

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def cantidadReptiles():
        return len(Reptil._listado)   
    def movimiento():
        return "reptar"
    
    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    @staticmethod
    def getListado():
        return Reptil._listado
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola
    
    @staticmethod
    def setListado(nuevoListado):
        Reptil._listado = nuevoListado
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola