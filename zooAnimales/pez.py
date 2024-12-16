from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []

    def __init__(self):
        Pez._listado.append(self)

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def cantidadPeces():
        return len(Pez._listado)   
    def movimiento():
        return "nadar"
    
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "océano", genero, "rojo", 6)
    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "océano", genero, "gris", 6)
    
    @staticmethod
    def getListado():
        return Pez._listado
    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @staticmethod
    def setListado(nuevoListado):
        Pez._listado = nuevoListado
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas