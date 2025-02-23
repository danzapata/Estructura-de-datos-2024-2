# Importaciones
from binarySearchTree import BinarySearchTree
from usuario import Usuario

# Main
if __name__ == "__main__":

    print("Prueba 2 Lab 8\n")

    # Creamos un arbol binario y añadimos usuarios
    arbol = BinarySearchTree()
    arbol.insert(Usuario("Andres", 902), 11)
    arbol.insert(Usuario("Juliana", 777), 21)
    arbol.insert(Usuario("Daniel", 666), 18)
    arbol.insert(Usuario("Juan", 111), 3)
    arbol.insert(Usuario("Luis", 333), 9)
    arbol.insert(Usuario("Miguel", 555), 15)
    arbol.insert(Usuario("Esteban", 232), 7)
    # Mostrar arbol
    arbol.print_tree()
    print("------------------------------")
    # Imprimir en orden
    arbol.inorder(arbol._root)
    print("------------------------------")
    # Imprimir Maximo y minimo 
    print("Imprimir máximo y minimo:")
    print(arbol.maximo(arbol._root).getData())
    print(arbol.minimo(arbol._root).getData())
    print("------------------------------")
    # Hacer una búsqueda
    print("Búsqueda:")
    print(arbol.find(18).getData())
    print("------------------------------")
    # Eliminar usuario
    print("Eliminar: Luis con clave 9")
    arbol.Remove(9)
    arbol.print_tree()
    print("------------------------------")
