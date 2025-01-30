# Generar archivo gestion cambios 
archivo = open("solis.txt", "r")
texto = archivo.read().split("\n")

nuevaLista = []
for i in texto:
    temp = i.split(" ")
    if "aceptar" in temp:
        nuevaLista.append(i)
archivo.close()

with open("Gestion_cambios.txt", "w") as archiv:
    
    for i in nuevaLista:
        if i == nuevaLista[-1]:
            archiv.write(i)
        else:
            archiv.write(i+"\n")