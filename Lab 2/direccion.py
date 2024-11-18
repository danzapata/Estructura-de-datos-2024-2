# Clase Direccion 
class Direccion:
    
    # Constructor 
    def __init__(self):
        pass

    # Métodos setter
    def setCalle(self, calle):
        self._calle = calle

    def setNomenclatura(self, nomen):
        self._nomenclatura = nomen

    def setBarrio(self, barrio):
        self._barrio = barrio

    def setCiudad(self, city):
        self._ciudad = city

    def setEdificio(self, edi):
        self._Edificio = edi

    def setApto(self, apt):
        self._Apto = apt

    # Métodos getter
    def getCalle(self):
        return self._calle

    def getNomenclatura(self):
        return self._nomenclatura
    
    def getBarrio(self):
        return self._barrio
    
    def getCiudad(self):
        return self._ciudad
    
    def getEdificio(self):
        return self._Edificio

    def getApto(self):
        return self._Apto
    
    # Método toString
    def __str__(self):
        return f"[Calle {self._calle}, Número {self._nomenclatura}, Barrio {self._barrio}, Ciudad {self._ciudad}, Edificio {self._Edificio}, Apto {self._Apto}]"