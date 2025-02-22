# Clase
class BSTEntry():
    
    # constructor
    def __init__(self, objeto, k):
        self._data = objeto
        self._key = k

    # Métodos
    def setDataBST(self, objeto):
        self._data = objeto

    def setKey(self, k):
        self._key = k

    def getDataBST(self):
        return self._data
    
    def getKey(self):
        return self._key
    
    # ToString
    def __str__(self):
        return f"Clave {self.getKey()} y objeto {self.getDataBST()}"