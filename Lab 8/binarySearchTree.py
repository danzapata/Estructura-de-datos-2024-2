# Importaciones
from binarytree import BinaryTree
from bstentry import BSTEntry

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
        
    #