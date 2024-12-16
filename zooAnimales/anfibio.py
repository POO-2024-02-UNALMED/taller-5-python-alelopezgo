from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    _listado = []

    def __init__(self):
        Anfibio._listado.append(self)

    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, colorPiel = None, venenoso = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def cantidadAnfibios():
        return len(Anfibio._listado)
    def movimiento():
        return "saltar"

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre,edad, "selva", genero, "rojo", True)
    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
    @staticmethod
    def getListado():
        return Anfibio._listado
    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso
    
    @staticmethod
    def setListado(nuevoListado):
        Anfibio._listado = nuevoListado
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso