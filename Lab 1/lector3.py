# leer solicitudes en Control de cambio
control = open("solis.txt", "r") 
texto = control.read().split("\n")
indu = int(input("¿Qué categoría desea ver? (1. eliminar 2. agregar) equipos: "))

if indu==2:

    contador = 1
    for i in texto:
        separado = i.split(" ")
        if "agregar" in separado:
            print(f"{contador}. {i}")
        contador+=1

    indice = int(input("Selecione la solicitud que desea revisar: "))
    indice = indice-1
    comparador = texto[indice].split(" ")
    if "pendiente" not in comparador:
        print("La solicitud ya fue contestada.")
    else: 
        respuesta = int(input("Desea 1. rechazar o 2. aceptar, indique el número de su respuesta: "))
        if respuesta == 1:
            nuevo = texto[indice].split(" ")
            nuevo[-1] = "rechazar"
            print("operación realizada con éxito")
            concatenar = ""
            for i in nuevo:
                if i is not nuevo[-1]:
                    concatenar+=i+" "
                else:
                    concatenar+=i
            texto[indice] = concatenar
        elif respuesta == 2:
            nuevo = texto[indice].split(" ")
            nuevo[-1] = "aceptar"
            print("operación realizada con éxito, inventario general actualizado.")
            concatenar = ""
            for i in nuevo:
                if i is not nuevo[-1]:
                    concatenar+=i+" "
                else:
                    concatenar+=i
            texto[indice] = concatenar
            
            # Actualizar inventario general
            t = open("solisdeberas.txt" , "r+")
            t.read()
            t.write("\n")
            inventario = texto[indice].split(" ")
            inventario.pop(-1)
            inventario.pop(-1)
            for i in inventario:
                if i == inventario[-1]:
                    t.write(i)
                else: 
                    t.write(f"{i} ")
        else: 
            print("índice no válido")
        j = open("solis.txt", "w")
        for i in texto:
            if i is not texto[-1]:
                j.write(f"{i}\n")
            else:
                j.write(f"{i}")
elif indu==1:
    contador = 1
    for i in texto:
        separado = i.split(" ")
        if "eliminar" in separado:
            print(f"{contador}. {i}")
        contador+=1


else:
    print("Indice inválido")
        

# Actualizar lista de control cambios
#with open("solis.txt", "w") as textonuevo:    
 #   for i in texto:
  #      if i is not texto[-1]:
   #         textonuevo.write(f"{i}\n")
    #    else:
     #       textonuevo.write(f"{i}")                 