from numpy.random import SeedSequence
import random
from rutina_random import obt_tiempo_espera, obt_prox_llegada, obt_prox_salida_Auto, obt_prox_salida_Clasica
import csv
from matplotlib import pyplot as plt

LLEGADA = 0
ELECCION = 1
ATENDER = 2
SALIDA = 3


####################### TIEMPOS ALEATORIOS #######################


def tiempo_rutina(FEL, reloj):
    evento_siguiente = FEL.pop(0)
    reloj = evento_siguiente[1]
    return evento_siguiente, reloj


def tiempo_prox_llegada(tiempo_evento):
    tiempo_entre_llegadas = obt_prox_llegada()
    return tiempo_evento + tiempo_entre_llegadas


def tiempo_prox_salida(tiempo_evento, eleccion):
    if (eleccion == 4):
        tiempo_entre_salidas = obt_prox_salida_Auto()+2
    else:
        tiempo_entre_salidas = obt_prox_salida_Clasica()+2
    return tiempo_evento + tiempo_entre_salidas


def tiempo_espera(tiempo_evento, clientes):
    tiempo_productos = clientes[2]*0.1
    tiempo_de_espera = obt_tiempo_espera()+tiempo_productos
    return tiempo_evento + tiempo_de_espera

####################### TIEMPOS DETERMINISTAS #######################

# def tiempo_rutina(FEL, reloj):
#    evento_siguiente = FEL.pop(0)
#    reloj = evento_siguiente[1]
#    return evento_siguiente, reloj


# def tiempo_prox_llegada(tiempo_evento):
#    tiempo_entre_llegadas = 1
#    return tiempo_evento + tiempo_entre_llegadas


# def tiempo_prox_salida(tiempo_evento, eleccion):
#    if (eleccion == 2):
#        tiempo_entre_salidas = 5
#    else:
#        tiempo_entre_salidas = 8
#    return tiempo_evento + tiempo_entre_salidas


# def tiempo_espera(tiempo_evento):
#    tiempo_de_espera = 5
#    return tiempo_evento + tiempo_de_espera


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
            # print("cumple")
            return colamin
        else:
            #print("no cumple")
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
    print("{:<8},{:<15},{:<10},{:<10},{:<10},{:<10}".format(
        'tiempo', 'evento', 'persona', 'servidor', "cola", "cola caja"))


def crear_titulo():
    reporte = open("reporte.csv", "a", newline="")
    escribir = csv.writer(reporte)
    titulo = ("tiempo", "nombre", "persona", "servidor", "cola", "caja")
    escribir.writerow(titulo)
    reporte.close


def generar_reporte(tiempo, nombre, persona, servidor, cola, caja):
    global tiempos, llegadas, atenciones
    reporte = open("reporte.csv", "a", newline="")
    escribir = csv.writer(reporte)
    evento = (tiempo, nombre, persona, servidor, cola, caja)
    escribir.writerow(evento)
    reporte.close


def graficos(tiempos, llegada, eleccion, atencion, salida):
    plt.plot(tiempos, llegada)
    plt.xlabel('tiempos')
    plt.ylabel('llegadas')
    plt.savefig("tiempo_llegada.png")
    plt.clf()
    plt.plot(tiempos, eleccion)
    plt.xlabel('tiempos')
    plt.ylabel('elecciones')
    plt.savefig("tiempo_elecciones.png")
    plt.clf()
    plt.plot(tiempos, atencion)
    plt.xlabel('tiempos')
    plt.ylabel('atenciones')
    plt.savefig("tiempo_atenciones.png")
    plt.clf()
    plt.plot(tiempos, salida)
    plt.xlabel('tiempos')
    plt.ylabel('salidas')
    plt.savefig("tiempo_salidas.png")
    plt.clf()
    plt.plot(tiempos, llegada)
    plt.plot(tiempos, eleccion)
    plt.plot(tiempos, atencion)
    plt.plot(tiempos, salida)
    plt.xlabel('tiempos')
    plt.ylabel('eventos')
    plt.savefig("tiempo_eventos.png")


def imprimir_evento(evento, cola, Cajas):
    global llegadas_clientes, atenciones
    tiempo = round(evento[1], 2)
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
    cola = len(cola)
    servidor = "-"
    caja = 0
    if len(evento) == 4:
        servidor = evento[3]
        caja = len(Cajas[evento[3]][2])
    #print(tiempo, name, persona, servidor, agenda_cola)
    generar_reporte(tiempo, name, persona, servidor, cola, caja)
    # print("{:<8},{:<15},{:<10},{:<10},{:<10},{:<10}".format(
    #    tiempo, name, persona, servidor, cola, caja))
