# Ejercicio 2 Lab 1
import datetime

horaActual = datetime.datetime.now()

print(horaActual.hour, horaActual.minute, horaActual.second)


archivo =open("test_pr2.txt", "r+") 
    # Leemos la lectura y la separamos 
texto = archivo.read().replace("\n", " ")
texto2 = texto.split(" ")
cedula = "3735737263"

if cedula in texto2:
    indice = texto2.index(cedula)
    contra = texto2[indice+1]
    rol = texto2[indice+2]
    print(contra, rol)
    texto2.pop(indice+2)
    texto2.remove(contra)
    texto2.remove(cedula)


archivo2 = open("test_pr2.txt", "w")
contador = 0
archivo2.seek(0)
for i in texto2:
    print(i)
    contador+=1
    if contador!= 3:
        archivo.write(i+" ") 
    else:
        archivo.write(i+"\n")
        contador = 0        
