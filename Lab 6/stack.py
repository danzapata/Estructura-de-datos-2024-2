# Importaciones
from listaSimple import ListaSimple

# Clase
class Stack:
    
    # Constructor
    def __init__(self):
        self._list = ListaSimple()

    # Métodos 
    def size(self):
        return self._list.size()
    
    def isEmpty(self):
        return self._list.isEmpty()
    
    def push(self, objeto):
        self._list.addFirst(objeto)
    
    def pop(self):
        return self._list.removeFirst()
    
    def top(self):
        return self._list.first()
    

# Pruebas

if __name__ == "__main__":

    pila = Stack()

    pila.push("2")
    pila.push("4")
    pila.push("6")
    pila.push("8")
    pila.push("10")

    for i in range(0, pila.size()):
        print(pila.pop().getData())