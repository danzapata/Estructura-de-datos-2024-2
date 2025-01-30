# Importaciones
from listaSimple import ListaSimple

# Clase
class Queue:

    # Constructor
    def __init__(self):
        self._list = ListaSimple()

    # Métodos
    def size(self):
        return self._list.size()
    
    def isEmpty(self):
        return self._list.isEmpty()
    
    def enqueue(self, objeto):
        self._list.addLast(objeto)

    def dequeue(self):
        return self._list.removeFirst()
    
    def first(self):
        return self._list.first()
    

# Pruebas

if __name__ == "__main__":

    cola = Queue()

    cola.enqueue("2")
    cola.enqueue("4")
    cola.enqueue("6")
    cola.enqueue("8")
    cola.enqueue("10")

    for i in range(0, cola.size()):
        print(cola.dequeue().getData())