from numpy.random import SeedSequence
import random
LLEGADA = 0
ATENDER = 1
SALIDA = 2
Cajas = []
DISPONIBLE = 1
OCUPADA = 0
for i in range(0, 10):
    if i != 9:
        Caja = [i, DISPONIBLE, []]
        Cajas.append(Caja)
    else:
        Caja = ["auto", DISPONIBLE, []]
        Cajas.append(Caja)

FEL = []
agenda_cola = []
n = 0


def crear_atributos():
    atributos = []
    edad = random.randint(15, 80)
    articulos = random.randint(1, 40)
    pago = random.randint(0, 20)
    if pago <= 6:
        pago = "efectivo"
    else:
        pago = "tarjeta"
    atributos = [pago, edad, articulos]
    return atributos


def chequear_requisitos(pago, edad, articulos):
    cumple = 0
    conteo = 0
    if pago == "tarjeta":
        conteo = conteo+1
    if edad <= 55:
        conteo = conteo+1
    if articulos <= 30:
        conteo = conteo+1
    if conteo == 3:
        cumple = "cumple"
    else:
        cumple = "no cumple"
    return cumple


def chequear_colas(Cajas, evento):
    min_cola = 100
    colamin = -1
    for i in range(len(Cajas)):
        if min_cola > len(Cajas[i][2]):
            min_cola = len(Cajas[i][2])
            colamin = i
    if Cajas[colamin][0] == "auto":
        c = chequear_requisitos(evento[0], evento[1], evento[2])
        if c == "cumple":
            print("cumple")
            return colamin
        else:
            print("no cumple")
            min_cola = 100
            colamin = -1
            for i in range(len(Cajas)-1):
                if min_cola > len(Cajas[i][2]):
                    min_cola = len(Cajas[i][2])
                    colamin = i
            return colamin
    else:
        return colamin


for i in range(len(Cajas)):
    if i < 9:
        r = random.randint(1, 4)
        for j in range(0, r):
            cliente = crear_atributos()
            Cajas[i][2].append(cliente)

# print(cola[0][0])
# Cajas[2][2].append(cola)
for i in range(len(Cajas)):
    print(Cajas[i])
    print(len(Cajas[i][2]))
atributos = crear_atributos()
cliente = (atributos)
print(cliente)
eleccion = chequear_colas(Cajas, cliente)
print(eleccion)
evento = (LLEGADA, 1, 0, eleccion)
agenda_cola.append(evento)
evento = (SALIDA, 1, 0, 5)
agenda_cola.append(evento)
print(agenda_cola)
print(agenda_cola[0][3])
agenda_cola.pop(0)
print(agenda_cola[0])
