# Imports
from listaSimple import ListaSimple
from nodoSimple import NodoSimple
from direccion import Direccion
from usuario import Usuario
from fecha import Fecha

# Coleccion 
class colection: 
    
    # Constructor 
    def __init__(self):
        self._lista = ListaSimple()

    def getLista(self):
        return self._lista
    
    # Métodos
    def add(self, objeto):
        if self.getLista().size()!= 0:
            temp = self.getLista()._head
            condicion = temp.getNext()
            while condicion != None:
                temp = temp.getNext()
                condicion = temp.getNext()
            nodo = NodoSimple(objeto)
            temp.setNext(nodo)
            self.getLista()._tail = nodo
            self.getLista()._size += 1
        else:
            self.getLista().addFirst(objeto)

    def remove(self, objeto):
        temp = self.getLista()._head

        while temp.getData()!=objeto:
            prev = temp
            temp = temp.getNext()
        
        if temp == self.getLista()._head:
            self.getLista()._head = temp.getNext()
            temp.setNext(None)
        else:
            apuntador = temp.getNext()
            prev.setNext(apuntador)
            temp.setNext(None)

if __name__ == "__main__":
    # Ejercicio Números -----------------------------------------------------------------------------------------------
    coleccion = colection()
    contador = 1
    coleccion.add(contador)
    for i in range(2, 21, 2):
        coleccion.add(i)

    temp = coleccion.getLista()._head
    condicion = temp.getNext()
    print("Lista tiene: ")
    while condicion !=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()
    
    print("Eliminamos y queda: ")
    coleccion.remove(1)
    coleccion.remove(10)
    coleccion.remove(20)

    temp = coleccion.getLista()._head
    condicion = temp.getNext()
    while condicion !=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()

    # Ejercicio usuarios -------------------------------------------------------------------------------------------
    print("\nEjercicio usuarios")
    coleccion2 = colection()
    # Creación usuarios
    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("Trapiche")
    miDir.setCalle(57)
    miDir.setNomenclatura(6927)
    miDir.setEdificio(16)
    miDir.setApto("1359")
    miUsuario = Usuario("Daniel", 666, 5435355, miFecha, "danzapata@unal", miDir, "Medellin")
    coleccion2.add(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Medellin")
    miDir.setBarrio("Candelaria")
    miDir.setCalle(53)
    miDir.setNomenclatura(3212)
    miDir.setEdificio(1)
    miDir.setApto("412")
    miUsuario = Usuario("juan", 777, 2415433, miFecha, "zjuanR@gmail", miDir, "medellin")
    coleccion2.add(miUsuario)

    miFecha = Fecha(24, 7, 2005)
    miDir = Direccion()
    miDir.setCiudad("Bello")
    miDir.setBarrio("barrio-nuevo")
    miDir.setCalle(27)
    miDir.setNomenclatura(2423)
    miDir.setEdificio("")
    miDir.setApto("")
    miUsuario = Usuario("Jose", 999, 4421414, miFecha, "nel@unal.edu", miDir, "Medellin")
    coleccion2.add(miUsuario)

    temp = coleccion2.getLista()._head
    condicion = temp.getNext()
    while condicion !=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()

    print("crea un usuario: ")
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

    coleccion2.getLista().addFirst(miUsuario)

    print("Crea un segundo usuario: ")
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

    coleccion2.add(miUsuario)

    print("\nResultado final: ")
    temp = coleccion2.getLista()._head
    condicion = temp.getNext()
    while condicion !=None:
        print(temp.getData())
        condicion = temp.getNext()
        temp = temp.getNext()