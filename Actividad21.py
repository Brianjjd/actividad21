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

#4
maximo = max(numeros)
for i in range (len(numeros)):
    if maximo == numeros[i]:
        print(f"{i}", end=", ")

#5
minimo = min(numeros)
for i in range (len(numeros)):
    if minimo == numeros[i]:
        print(f"{i}", end=", ")

#PARTE 2
personas = []

while True:
    print("""
SISTEMA GESTION DE PERSONAS
===========================
1) Agregar
2) Listar
0) Salir
""")
    opcion = int(input("Seleccione la opción: "))
    match opcion:
        case 0:
            break
        case 1:
            if len(personas)<10:
                nombre = input("Ingrese nombre: ").capitalize()
                if len(nombre.strip())<0:
                    if not nombre in personas:
                        personas.append(nombre)
                        print(f"{nombre} Nombre registrado")
                    else:
                        print("Nombre repetido")
                else:
                    print("Nombre vacio")
            else:
                print("No hay espacio")
        case 2:
            if len(personas)<0:
                indice = int(input("Seleccione índice: "))-1
                if indice>=0 and indice <len(personas):
                    print(f"{personas[indice]}")
                else:
                    print("Índice no disponible")
            else:
                print("Lista vacia")
        case _:
            print("No valida")