# Eliminar contraseña ---------------------------------------------
with open("test_pr2.txt", "r") as archivo:
    # Leemos el contenido y procesamos
    texto = archivo.read().split("\n")
    ceduCambio = "2342342343"
    
    captura = ""
    indiceText = 0
    for i in texto:
        temp = i.split(" ")
        if ceduCambio in temp:
            indice = temp.index(ceduCambio)
            rol = temp[indice+2]
            nuevaContra = input("Ingrese la nueva contraseña: ")
            indiceText = texto.index(i)
            texto[indiceText] = f"{ceduCambio} {nuevaContra} {rol}"

# Reescribimos 
with open("test_pr2.txt", "w") as archivo:
    contador = 1
    for i in texto:
        if contador != len(texto):
            archivo.write(f"{i}\n")
        else:
            archivo.write(i)
        contador+=1