# Importaciones
from binarytree import BinaryTree
from bstentry import BSTEntry
from nodoDoble import NodoDoble

# Clase
class BinarySearchTree(BinaryTree):
    
    # Constructor 
    def __init__(self):
        super().__init__()

    # Métodos
    def find(self, key):
        return self.searchTree(key, self._root)

    def searchTree(self, key, nodo):
        temp = nodo.getData()
        if key == temp.getKey():
            return nodo
        elif key<temp.getKey():
            return self.searchTree(key, self.left(nodo))
        else:
            return self.searchTree(key, self.right(nodo))
        
    # Insertar al árbol 
    def addEntry(self, nodo, BSTEntry):
        temp = nodo.getData()
        nodoNuevo = NodoDoble(BSTEntry)
        if BSTEntry.getKey()<temp.getKey():
            if self.hasLeft(nodo):
                self.addEntry(self.left(nodo), BSTEntry)
            else:
                nodo.setPrev(nodoNuevo)
        else:
            if self.hasRight(nodo):
                self.addEntry(self.right(nodo, BSTEntry))
            else:
                nodo.setNext(nodoNuevo)

    def insert(self, objeto, key):
        temp = BSTEntry(objeto, key)
        if self.isEmpty():
            self.addRoot(temp)
        else:
            self.addEntry(self._root, temp)

    # Eliminar del árbol 
    def maxNodo(self, nodo):
        if self.hasRight(nodo):
            return self.maxNodo(self.right(nodo))
        else:
            return nodo

    def predecesor(self, nodo):
        temp = self.left(nodo)
        return self.maxNodo(temp)

    def Remove(self, key):
        v = self.find(key)
        temp = v.getData()
        if self.hasLeft(v) and self.hasRight(v):
            W = self.predecesor(v)
            v.setData(W.getData())
            self.remove(W)
        else:
            self.remove(v)
        return temp