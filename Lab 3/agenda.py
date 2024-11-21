# Clase Agenda

class Agenda:
    
    # Constructor 
    def __init__(self, capacidad = 0):
        self._registro = []
        self._no_reg = 0 
        self._capacity = capacidad

    # Métodos 
    def buscar(self, id):
        position = 0 
        for i in self._registro:
            if i.getId()==id:
                return position 
            position += 1
        return -1
    
    def agregar(self, usuario):
        if self.buscar() == -1:
            if self._capacity>self._no_reg:
                self._registro[self._no_reg] = usuario
        else:
            return False