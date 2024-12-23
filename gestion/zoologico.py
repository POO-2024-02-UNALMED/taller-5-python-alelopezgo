class Zoologico:
    _zonas = []

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidadAnimales()
        return total
    @classmethod
    def getZona(cls):
        return cls._zonas
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    
    @classmethod
    def setZona(cls, zonas):
        cls._zonas = zonas
    def setNombre(self, nombre):
        self._nombre = nombre
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion