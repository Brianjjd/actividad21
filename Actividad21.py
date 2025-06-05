import random

numeros= []
for i in range (100):
    numeros.append(random.randint(1,10))

for i in range (2,len(numeros),2):
    print(f"Indice {i}:  {numeros[i]}")

mayor = numeros[0]
indice_mayor = 0
for n in range (len(numeros)):
    if numeros[n] > mayor:
        mayor = numeros[n]
        indice_mayor = n
print(f"El elemento mayor es {mayor} en el indice {indice_mayor}")

menor = numeros[99]
indice_menor = 0
for n in range (len(numeros)):
    if numeros[n] < menor:
        menor = numeros[n]
        indice_menor = n
print(f"El elemento menor es {menor} en el indice {indice_menor}")