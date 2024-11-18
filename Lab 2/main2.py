from usuario import Usuario
from direccion import Direccion
from fecha import Fecha

# Programa principal del punto 4 Lab 1
if __name__ == "__main__":
    print("Registro de Usuario, ingrese correctamente sus datos.")

    miUsuario = Usuario(input("Nombre: "), int(input("Numero de documento: ")))
    miUsuario.setTel(int(input("Número de telefono: ")))

    print("Fecha de nacimiento")
    miFecha = Fecha(int(input("Dia: ")), int(input("Mes: ")), int(input("Año: ")))

    miUsuario.setFecha_Nacimiento(miFecha)
    miUsuario.setCiudad_nacimiento(input("Ingrese ciudad de nacimiento: "))
    miUsuario.setEmail(input("Correo electrónico: "))

    miDir = Direccion()
    print("Información de residencia.")
    miDir.setCiudad(input("Ciudad en donde vive: "))
    miDir.setBarrio(input("Barrio: "))
    miDir.setCalle(input("Calle: "))
    miDir.setNomenclatura(input("Nomenclatura: "))
    miDir.setEdificio(input("Edificio: "))
    miDir.setApto(input("Apartamento: "))
    miUsuario.setDir(miDir)
    print("\n",miUsuario,"\n",sep="")