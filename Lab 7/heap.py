# Importaciones
import random

# Clase 
class Heap():

    # Constructor 
    def __init__(self, capacidad):
        self._lista = []
        self._size = 0
        self._capacity = capacidad

    # Métodos
    def parent(self, indice): # Retorna el índice del padre
        return  (indice//2)-1
    
    def left(self, indice): # Hijo izquierdo
        return (indice*2)+1
    
    def right(self, indice): # Hijo derecho
        return (indice*2)+2
    
    def max_heapify(self, i): # Intercambios
        hijoIzq = self.left(i)
        hijoDer = self.right(i)
        # Comparamos padre con hijos
        if (hijoIzq <= self._size) and (self._lista[hijoIzq]>self._lista[i]):
            masGrande = hijoIzq
        else:
            masGrande = i
        if (hijoDer <= self._size) and (self._lista[hijoDer]>self._lista[masGrande]):
            masGrande = hijoDer
        # Cambio hijo con padre
        if masGrande != i:
            temp = self._lista[i]
            self._lista[i] = self._lista[masGrande]
            self._lista[masGrande] = temp
            self.max_heapify(masGrande)

    def build_max_heap(self, args): # Construir un heap
        self._lista = args
        self._size = len(args)
        for i in range(((len(args)//2)-1), 0, -1):
            self.max_heapify(i)

    def heap_sort(self, args): # Ordenar el heap
        self.build_max_heap(args)
        heapSize = len(args)
        for i in range((len(args)-1), 1, -1):
            temp = args[i]
            args[i] = args[0]
            args[0] = temp
            heapSize-=1
            self.max_heapify(heapSize)

if __name__ == "__main__":

    lista = []
    for i in range(20):
        lista.append(random.randint(0, 50))
    print("Lista inicial: ")
    print(lista,"\n")

    print("Aplicado el heap: ")
    heap = Heap(20)
    heap.heap_sort(lista)
    print(heap._lista,"\n")
