# Importaciones
from queue import Queue
from nodoDoble import NodoDoble
from nodoSimple import NodoSimple

# Clase 
class BinaryTree:
    
    # Constructor 
    def __init__(self):
        self._root = None
        self._size = 0

    # Métodos booleanos
    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def isRoot(self, nodo):
        if nodo == self._root:
            return True
        else:
            return False
    
    def hasLeft(self, nodo):
        if nodo.getPrev() != None:
            return True
        else: 
            return False
    
    def hasRight(self, nodo):
        if nodo.getNext() != None:
            return True
        else:
            return False
    
    def isInternal(self, nodo):
        return self.hasLeft(nodo) or self.hasRight(nodo)

    # Métodos retorno de nodos    
    def left(self, nodo):
        return nodo.getPrev()
    
    def right(self, nodo):
        return nodo.getNext()
    
    def root(self):
        return self._root
    
    # Altura y profundidad
    def depth(self, nodo):
        if self.isRoot(nodo):
            return 0
        else:
            return 1 + self.depth(nodo)

    def height(self, nodo):
        if self.isInternal(nodo)==False:
            return 0
        else:
            h = 0
            h = max(self.height(self.left(nodo)), self.height(self.right(nodo)))
            return 1+h
        
    # Conseguir padre
    def Parent(self, nodo):
        if self.isRoot(nodo):
            return None
        else:
            cola = Queue()
            cola.enqueue(self._root)
            temp = self._root
            while cola.isEmpty()!=True and self.left(cola.first().getData())!=nodo and self.right(cola.first().getData())!=nodo:
                print(nodo.getData())
                print(cola.first().getData())
                temp = cola.dequeue()
                temp = temp.getData()
                if self.hasLeft(temp):
                    cola.enqueue(self.left(temp))
                if self.hasRight(temp):
                    cola.enqueue(self.right(temp))
            return temp
        
    # Parent 
    def parent(self, nodo):
        if self.isRoot(nodo):
            return None
        else:
            cola = Queue()
            cola.enqueue(self._root)
            while cola.isEmpty()!=True:
                temp = cola.dequeue()
                temp = temp.getData() 
                if self.hasLeft(temp) and self.left(temp)==nodo:
                    return temp
                if self.hasRight(temp) and self.right(temp)==nodo:
                    return temp
                if self.hasLeft(temp):
                    cola.enqueue(self.left(temp))
                if self.hasRight(temp):
                    cola.enqueue(self.right(temp))
            return None
        
    # Agregar al arbol
    def addRoot(self, objeto):
        self._root = NodoDoble(objeto)
        self._size = 1

    def insertLeft(self, nodo, objeto):
        izquierdo = NodoDoble(objeto)
        nodo.setPrev(izquierdo)
        self._size+=1

    def insertRight(self, nodo, objeto):
        derecho = NodoDoble(objeto)
        nodo.setNext(derecho)
        self._size+=1

    # Eliminar un nodo
    def remove(self, nodo):
        padre = self.parent(nodo)
        # Si tiene al menos un hijo
        if self.hasLeft(nodo) or self.hasRight(nodo):
            if self.hasLeft(nodo):
                hijo = self.left(nodo)
            else:
                hijo = self.right(nodo)
            
            # Se conecta el hijo de nodo al padre
            if self.left(padre) == nodo:
                padre.setPrev(hijo)
            else:
                padre.setNext(hijo)

            # Desconectamos el nodo 
            nodo.setPrev(None)
            nodo.setNext(None)

        else:
            print("Entró acá", nodo.getData(),"y",self.right(padre).getData())
        # Caso en que no tiene hijos
            if self.left(padre) == nodo:
                padre.setPrev(None)
            else:
                padre.setNext(None)

        self._size-=1 # Quitamos una unidad

    # Visitar
    def visit(self, nodo):
        print("BST Entry con:",nodo.getData())

    # Minimo 
    def minimo(self, nodo):
        if self.hasLeft(nodo):
            return self.minimo(self.left(nodo))
        else: 
            return nodo
    # Maximo 
    def maximo(self, nodo):
        if self.hasRight(nodo):
            return self.maximo(self.right(nodo))
        else:
            return nodo

    # Devolver en orden
    def inorder(self, nodo):
        if self.hasLeft(nodo):
            self.inorder(self.left(nodo))
        self.visit(nodo)
        if self.right(nodo):
            self.inorder(self.right(nodo))