# Generar erchivo solicitudes
with open("solis.txt","r") as archivo:
    # Creamos el texto
    texto = archivo.read().split("\n")
    conditional = int(input())
    textoNuevo = []

    if conditional == 2: # Solis de eliminar--------------------------------
        for i in texto:
            temp = i.split(" ")
            guardar = len(temp)
            if (int(guardar)==6) and (temp[-1]=="pendiente"):
                concatenar = ""
                for e in temp:
                    if e == temp[-1]:
                        concatenar+=e
                    else:
                        concatenar+=e+" "
                textoNuevo.append(concatenar)
        with open("solicitudes eliminar.txt", "w") as j:
            for i in textoNuevo:
                if i is textoNuevo[-1]:
                    j.write(i)
                else:
                    j.write(f"{i}\n")
    elif conditional == 1: # Solis aceptar-------------------------
        for i in texto:
            temp = i.split(" ")
            guardar = len(temp)
            if (int(guardar)==10) and (temp[-1]=="pendiente"):
                concatenar = ""
                for e in temp:
                    if e == temp[-1]:
                        concatenar+=e
                    else:
                        concatenar+=e+" "
                textoNuevo.append(concatenar)
        with open("solicitudes agregar.txt", "w") as j:
            for i in textoNuevo:
                if i is textoNuevo[-1]:
                    j.write(i)
                else:
                    j.write(f"{i}\n")
    else: 
        print("El índice no fue correcto, intente mas tarde.")