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
                self.addEntry(self.right(nodo), BSTEntry)
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
    
    def print_tree(self):
        self._print_tree_helper(self._root, "", True)

    def _print_tree_helper(self, node, prefix, is_left):
        if node is None:
            return
        
        # Recorre primero el subárbol derecho (para imprimir arriba)
        if self.right(node):
            new_prefix = prefix + ("│   " if is_left else "    ")
            self._print_tree_helper(self.right(node), new_prefix, False)

        # Imprime el nodo actual
        connector = "└── " if is_left else "├── "
        print(prefix + connector + str(node.getData().getDataBST()))

        # Recorre el subárbol izquierdo (para imprimir abajo)
        if self.left(node):
            new_prefix = prefix + ("    " if is_left else "│   ")
            self._print_tree_helper(self.left(node), new_prefix, True)


if __name__ == "__main__":

    print("\nPrueba 1 Lab 8")

    # Creamos un árbol y insertamos entradas
    arbol = BinarySearchTree()
    arbol.insert("15", 15)
    arbol.insert("9", 9)
    arbol.insert("40", 40)
    arbol.insert("6", 6)
    arbol.insert("13", 13)
    arbol.insert("64", 64)
    arbol.insert("20", 20)
    arbol.insert("4", 4)
    arbol.insert("8", 8)
    print("-----------------")
    arbol.print_tree()

    # Mostrar en orden 
    arbol.inorder(arbol._root)

    # Eliminar elemento
    arbol.remove(arbol.find(20))
    print("-----------------")
    arbol.print_tree()
    
    # Buscar elemento
    print("\n-----------------")
    print("busqueda de elemento: ",arbol.find(40).getData())
    # Imprimir máximo y mínimo
    print("Número máximo",arbol.maximo(arbol._root).getData())
    print("Número mínimo",arbol.minimo(arbol._root).getData())
