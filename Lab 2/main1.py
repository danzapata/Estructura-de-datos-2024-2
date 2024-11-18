from usuario import Usuario
from direccion import Direccion
from fecha import Fecha

# Programa principal del punto 4 Lab 1
if __name__ == "__main__":
    
    miFecha = Fecha(24, 7, 2005)
    print(miFecha)

    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    print(miDir)

    miUsuario = Usuario("Daniel", 666)
    miUsuario.setTel(3214256)
    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setEmail("danzapata@unal.edu.co")
    miUsuario.setDir(miDir)
    miUsuario.setCiudad_nacimiento("Medellín")
    print(miUsuario)