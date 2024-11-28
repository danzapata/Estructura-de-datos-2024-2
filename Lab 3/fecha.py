# Clase Fecha 
class Fecha:

    # Constructor 
    def __init__(self, dia = 0, mes = 0, year = 0):
        self._dd = dia
        self._mm = mes
        self._aa = year
    
    # Métodos setter
    def setDia(self, dia):
        self._dd = dia

    def setMes(self, mes):
        self._mm = mes

    def setA(self, year):
        self._aa = year

    # Métodos getter 
    def getDia(self):
        return self._dd

    def getMes(self):
        return self._mm
    
    def getA(self):
        return self._aa
    
    # Método toString
    def __str__(self):
        return f"{self._dd}-{self._mm}-{self._aa}"