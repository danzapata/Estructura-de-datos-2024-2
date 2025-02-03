# Importaciones
from queue import Queue
from stack import Stack
from usuario import Usuario

# Clase
class TurnoUsuario:

    # Constructor
    def __init__(self):
        self._registro = Queue()
        self._usuarioAtendido = Stack()

    # Métodos
    def registrar(self, usuario):
        self._registro.enqueue(usuario)

    def atenderSiguiente(self):
        temp = self._registro.dequeue().getData()
        self._usuarioAtendido.push(temp)
        return temp

    def toFile(self):
        # Texto cola
        txtCola = open("Lab 6/usuariosPendientes.txt", "w")
        for i in range(0, self._registro.size()):
            temp = self._registro.dequeue().getData()
            txtCola.write(f"{temp.getNombre()} {str(temp.getId())}\n")
        txtCola.close()

        # Texto pila
        txtPila = open("Lab 6/usuariosAtendios.txt", "w")
        for i in range(0, self._usuarioAtendido.size()):
            temp = self._usuarioAtendido.pop().getData()
            txtPila.write(f"{temp.getNombre()} {str(temp.getId())}\n")
        txtPila.close()

# Pruebas 

if __name__ == "__main__":

    sistema = TurnoUsuario()
    
    usuario1 = Usuario("Juliana", 777)
    usuario2 = Usuario("Daniel", 666)
    usuario3 = Usuario("LisSangel", 111)
    usuario4 = Usuario("Nikolas", 888)
    usuario5 = Usuario("Peibac", 333)

    sistema.registrar(usuario1)
    sistema.registrar(usuario2)
    sistema.registrar(usuario3)
    sistema.registrar(usuario4)
    sistema.registrar(usuario5)

    # Primera prueba, no atender ninguno
    """sistema.toFile()"""

    # Segunda prueba, atender dos 
    """sistema.atenderSiguiente()
    sistema.atenderSiguiente()
    sistema.toFile()"""