# Importaciones
import random

# Clase 
class Heap:

    # Construtor
    def __init__(self, capacidad):
        self._lista = []
        self._size = 0
        self._capacity = capacidad

    # Métodos
    def parent(self, indice):  # Retorna el índice del padre
        return (indice - 1) // 2

    def left(self, indice):  # Hijo izquierdo
        return (indice * 2) + 1

    def right(self, indice):  # Hijo derecho
        return (indice * 2) + 2

    def max_heapify(self, i):  # Intercambios
        hijo_izq = self.left(i)
        hijo_der = self.right(i)
        mas_grande = i

        # Comparar con los hijos
        if hijo_izq < self._size and self._lista[hijo_izq] > self._lista[mas_grande]:
            mas_grande = hijo_izq
        if hijo_der < self._size and self._lista[hijo_der] > self._lista[mas_grande]:
            mas_grande = hijo_der
        if mas_grande != i:
            self._lista[i], self._lista[mas_grande] = self._lista[mas_grande], self._lista[i]
            self.max_heapify(mas_grande) 

    def build_max_heap(self, args):  # Construir un heap
        self._lista = args
        self._size = len(args)
        # Empezar desde el último nodo y avanzar a la raíz
        for i in range((self._size // 2) - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self, args):  # Ordenar el heap
        self.build_max_heap(args)
        for i in range(self._size - 1, 0, -1):
            self._lista[0], self._lista[i] = self._lista[i], self._lista[0]
            self._size -= 1
            self.max_heapify(0)

if __name__ == "__main__":

    lista = []
    for i in range(10):
        lista.append(random.randint(0, 50))
    print("Lista inicial: ")
    print(lista,"\n")

    print("Construyendo el heap: ")
    heap = Heap(10)
    heap.build_max_heap(lista)
    print(heap._lista,"\n")

    print("Aplicado el sort: ")
    heap.heap_sort(lista)
    print(heap._lista,"\n")