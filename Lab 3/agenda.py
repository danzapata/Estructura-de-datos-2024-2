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
                self._registro.append(usuario)
                self._no_reg += 1
                return True
        else:
            return False
    
    def eliminar(self, id):
        busqueda = self.buscar(id)
        if busqueda == -1:
            return False
        else:
            while self._no_reg-1 > busqueda:
                self._registro[busqueda] = self._registro[busqueda+1]
                busqueda+=1
            self._registro.pop()
            self._no_reg-=1
            return True
        
    def toFile(self, documento):
        with open(documento, "w") as texto:
            for i in range(0, self._no_reg, 1):
                if i == (self._no_reg-1):
                    texto.write(f"{self._registro[i].__str__()}")
                else: 
                    texto.write(f"{self._registro[i].__str__()}\n")               

    def importar(self, documento):
        with open(documento, "r") as texto:
            leer = texto.read()
            usuarios = leer.split("\n")
            
            linea = 0
            while len(usuarios) > linea:
                crearUsuario = usuarios[linea].split(" ",8)
                miFecha = Fecha(int(crearUsuario[2]),int(crearUsuario[3]),int(crearUsuario[4]))
                midir = Direccion(crearUsuario[8])
                miUsuario = Usuario(crearUsuario[0], int(crearUsuario[1]))
                miUsuario.setFecha_Nacimiento(miFecha)
                miUsuario.setDir(midir)
                miUsuario.setCiudad_nacimiento(crearUsuario[5])
                miUsuario.setTel(int(crearUsuario[6]))
                miUsuario.setEmail(crearUsuario[7])
                self.agregar(miUsuario)
                linea+=1

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
    miUsuario.setCiudad_nacimiento("Medellin")
    agenda.agregar(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Medellin")
    miDir.setBarrio("Candelaria")
    miDir.setCalle(53)
    miDir.setNomenclatura(3212)
    miDir.setEdificio(1)
    miDir.setApto("412")
    miUsuario = Usuario("juan", 777)
    miUsuario.setTel(3214256)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("danzapata@unal.edu.co")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellin")
    agenda.agregar(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("barrio-nuevo")
    miDir.setCalle(27)
    miDir.setNomenclatura(2423)
    miDir.setEdificio("")
    miDir.setApto("")
    miUsuario = Usuario("Jose", 999)
    miUsuario.setTel(3214256)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("danzapata@unal.edu.co")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellin")
    agenda.agregar(miUsuario)

    miFecha = Fecha(25, 11, 2007)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    miUsuario = Usuario("Isabella", 555)
    miUsuario.setTel(542142142)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("isa@gmail.com")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellin")
    agenda.agregar(miUsuario)

    miFecha = Fecha(25, 11, 2007)
    miDir = Direccion()
    miDir.setCiudad("Medellin")
    miDir.setBarrio("Buenos-Aires")
    miDir.setCalle(43)
    miDir.setNomenclatura(4042)
    miDir.setEdificio("")
    miDir.setApto("")
    miUsuario = Usuario("Luis-Angel", 111)
    miUsuario.setTel(542142142)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("isa@gmail.com")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellin")
    agenda.agregar(miUsuario)  

    print("Buscando usuario: ")
    print(agenda.buscar(111))

    agenda.toFile("agenda.txt")