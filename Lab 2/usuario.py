# Clase usuario
class Usuario:
    
    # Constructor
    def __init__(self, nombre="", id= 0):
        self._nombre = nombre
        self._id = id

    # métodos setter 
    def setNombre(self, nombre):
        self._nombre = nombre

    def setId(self, id):
        self._id = id

    def setFecha_Nacimiento(self, fecha):
        self._fecha_nacimiento = fecha
    
    def setCiudad_nacimiento(self, ciudad):
        self._ciudad_nacimiento = ciudad

    def setTel(self, telefono):
        self._telefono =  telefono

    def setEmail(self, email):
        self._email = email

    def setDir(self, direccion):
        self._direccion = direccion

    # Métodos getter 
    def getNombre(self):
        return self._nombre
    
    def getId(self):
        return self._id
    
    def getFecha_nacimiento(self):
        return self._fecha_nacimiento
    
    def getCiudad_nacimiento(self):
        return self._ciudad_nacimiento
    
    def getTel(self):
        return self._telefono
    
    def getEmail(self):
        return self._email
    
    def getdir(self):
        return self._direccion
    
    # Método toString
    def __str__(self):
        return f"Nombre {self._nombre}\nDocumento {self._id}\nFecha de Nacimiento {self._fecha_nacimiento}\nCiudad de nacimiento {self._ciudad_nacimiento}\nTeléfono {self._telefono}\nEmail {self._email}\nDireeción {self._direccion}"