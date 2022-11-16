from numpy.random import SeedSequence
import random
from rutina_random import obt_tiempo_espera, obt_prox_llegada, obt_prox_salida_Auto, obt_prox_salida_Clasica


LLEGADA = 0
ELECCION = 1
ATENDER = 2
SALIDA = 3

####################### TIEMPOS #######################


def tiempo_rutina(FEL, reloj):
    evento_siguiente = FEL.pop(0)
    reloj = evento_siguiente[1]
    return evento_siguiente, reloj


def tiempo_prox_llegada(tiempo_evento):
    tiempo_entre_llegadas = obt_prox_llegada()
    return tiempo_evento + tiempo_entre_llegadas


def tiempo_prox_salida(tiempo_evento, eleccion):
    if (eleccion == 9):
        tiempo_entre_salidas = obt_prox_salida_Auto()
    else:
        tiempo_entre_salidas = obt_prox_salida_Clasica()
    return tiempo_evento + tiempo_entre_salidas


def tiempo_espera(tiempo_evento):
    tiempo_de_espera = obt_tiempo_espera()
    return tiempo_evento + tiempo_de_espera


####################### Auxiliares #######################


def crear_atributos():
    edad = random.randint(15, 80)
    articulos = random.randint(1, 40)
    pago = random.randint(0, 10)
    if pago <= 3:
        pago = "efectivo"
    else:
        pago = "tarjeta"
    atributos = (pago, edad, articulos)
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


def agregar_FEL(FEL, evento):
    for i in range(len(FEL)):
        if FEL[i][1] > evento[1]:
            FEL.insert(i, evento)
            return
    FEL.append(evento)


def imprimir_encabezado():
    print("{:<8},{:<15},{:<10},{:<10},{:<10}".format(
        'tiempo', 'evento', 'persona', 'servidor', "cola"))


def imprimir_evento(evento, Cajas):
    tiempo = evento[1]
    name = "None"
    if evento[0] == LLEGADA:
        name = "LLEGADA"
    elif evento[0] == ELECCION:
        name = "ELECCION"
    elif evento[0] == ATENDER:
        name = "ATENDER"
    elif evento[0] == SALIDA:
        name = "SALIDA"
    persona = evento[2]
    servidor = "-"
    cola = (len(Cajas[evento[3]][2]))
    if len(evento) == 4:
        servidor = evento[3]
    print("{:<8},{:<15},{:<10},{:<10},{:<10}".format(
        tiempo, name, persona, servidor, cola))
