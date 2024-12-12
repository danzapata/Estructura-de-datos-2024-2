# importaciones
from agenda import Agenda

# Main
if __name__ == "__main__":
    agenda1 = Agenda(5)

    agenda1.importar("agenda.txt")

    for i in agenda1._registro:
        print(i.__str__())

    # Eliminamos un usuario
    agenda1.eliminar(999)

    # Almacenamos en agenda2.txt
    agenda1.toFile("agenda2.txt")