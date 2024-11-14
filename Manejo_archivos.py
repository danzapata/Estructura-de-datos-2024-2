# archivo = open("texto.txt", "r")
# Si le damos a print nos lanza la dirección de memoria
# recomendado cerrarlo archivo.close()
# método readLines del archivo muestra la lista de todo

# Otra forma de abrir el archivo es con la palabra with open(dirección) as archivo: y dentro colocar 
# lo que necesitemos, esto cierra automáticamente el archivo
# Función .replace("Cosa a reemplazar", "Con qué lo vamos a reemplazar")

"""""
with open("prueba.txt", "r") as archivo:
    lineas = archivo.read()
    archivo.seek(0) # Importante porque nos devuelve al inicio del documento 
    leaan = archivo.readlines()

    print("\nVamos a leer el archivo")
    print(leaan,"\n")
    print("Vamos a imprimir las lineas")
    print(lineas,"\n")
"""""

# Vamos a escribir en el archivo 

with open("Tiempos_estudio.txt", "w") as texto:
    for i in range(3, 17, 1):
        texto.write(f"Horas de estudio autonomo semana {i}:\n")
