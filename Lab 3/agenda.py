# Imports
from usuario import Usuario
from fecha import Fecha 
from direccion import Direccion

# Clase Agenda
class Agenda:
    
    # Constructor 
    def __init__(self, capacidad = 0):
        self._registro = []
        self._no_reg = 0 
        self._capacity = capacidad
        for i in range(0, self._capacity, 1):
            self._registro.

    # Métodos 
    def buscar(self, id):
        position = 0 
        for i in self._registro:
            if i.getId()==id:
                return position 
            position += 1
        return -1
    
    def agregar(self, usuario):
        if self.buscar(usuario.getId()) == -1:
            if self._capacity>self._no_reg:
                self._registro[self._no_reg] = usuario
        else:
            return False
    
    def eliminar(self, id):
        busqueda = self.buscar(id)
        if busqueda == -1:
            return False
        else:
            eliminado = self._registro[busqueda]
            self._registro[busqueda] = None

            while self._no_reg >= busqueda:
                self._registro[busqueda] = self._registro[busqueda+1]
                busqueda+=1

            return eliminado
        
if __name__ == "__main__":
    agenda = Agenda(5)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    miUsuario = Usuario("Daniel", 666)
    miUsuario.setTel(3214256)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("danzapata@unal.edu.co")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellín")
    agenda.agregar(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    miUsuario = Usuario("juan", 777)
    miUsuario.setTel(3214256)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("danzapata@unal.edu.co")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellín")
    agenda.agregar(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    miUsuario = Usuario("Daniel", 666)
    miUsuario.setTel(3214256)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("danzapata@unal.edu.co")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellín")
    agenda.agregar(miUsuario)

    print(agenda._registro)