# Ejercicio 2 Lab 1

with open("Lab 1/test_pr2.txt", "r") as archivo:
    # Leemos la lectura y la separamos por los espacios
    lectura = archivo.read()
    palabras = lectura.split(" ")

    # Contamos los En y en
    contador = 0
    for i in palabras:
        if i == "En" or i == "en":
            contador+=1
    print("La cantidad de (en) fue:", contador)

