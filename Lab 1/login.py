# Ejercicio 3 Lab 1
usuarios = {"Juan1223":"J12an*.", "Maria2345":"M23a*.", "Pablo1459":"P14o*.", "Ana3456":"A34a"}

# Login 
intentos = 0
while intentos<3:
    nombre = str(input("Ingrese el nombre: "))
    contraseña = str(input("Ingrese la contraseña: "))

    if nombre not in usuarios:
        intentos+=1
        print("El nombre de usuario fue incorrecto")
    else:
        if usuarios[nombre] == contraseña:
            print("Bienvenido al sistema :)")
            break
        else:
            intentos+=1
            print("La contraseña es incorrecta")