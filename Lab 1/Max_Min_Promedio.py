## Programa 1 lab 1

n = int(input()) # Cantidad de números que el usuario va a ingresar 

lista = [] # Lista donde guardaremos los números

for i in range(0, n, 1):
    num = int(input())
    lista.append(num)


# Max y Min 
Max = 0
Min = 0
for i in range(0, len(lista), 1):
    if i == 0:
        Max = lista[i]
        Min = lista[i]
    else:
        if lista[i]>=Max:
            Max = lista[i]
        elif lista[i]<=Min:
            Min = lista[i]

print("El máximo es:", Max)
print("El mínimo es:", Min)

# promedio y suma ingresados
sum = 0
for i in lista:
    sum+=i
print("La suma de los ingresados es:", sum)
print("El promedio es:", sum/lista.__len__())