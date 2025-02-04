# Importaciones
from heap import Heap
import random

# Clase 
class PriorityQueue:
    
    # Construtor 
    def __init__(self, heap):
        self._heap = heap
        self._list = heap._lista

    # Métodos
    def max_heap_insert(self, k):
        self._list.append(k)
        lista = self._list
        heap = self._heap
        contador = len(lista)-1

        while contador>0 and lista[heap.parent(contador)] < lista[contador]:
            temp = lista[heap.parent(contador)]
            lista[heap.parent(contador)] = lista[contador]
            lista[contador] = temp
            contador = heap.parent(contador)

    def heap_extract_max(self):
        maximo = self._list[0]
        self._list.pop(0)
        nuevaLista = self._list
        self._heap.build_max_heap(nuevaLista)
        return maximo
    
    def heap_maximum(self):
        return self._list[0]

if __name__ == "__main__":

    lista = []
    for i in range(10):
        lista.append(random.randint(0, 50))
    print("Lista inicial: ")
    print(lista,"\n")

    heap = Heap(11)
    heap.build_max_heap(lista)
    print("Heap creado: ")
    print(heap._lista,"\n")

    ColaPrioridad = PriorityQueue(heap)
    ColaPrioridad.max_heap_insert(20)
    print("Cola de prioridad, con un insert: ")
    print(ColaPrioridad._list, "\n")

    print("Cola de prioridad, con extraer máximo: ")
    print("Maximo anterior: ",ColaPrioridad.heap_extract_max())
    print(ColaPrioridad._list, "\n")

    print("Por último, retornar el máximo con heap_maximum: ",ColaPrioridad.heap_maximum(),"\n")

