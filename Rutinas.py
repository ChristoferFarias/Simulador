from funciones import tiempo_rutina, tiempo_espera, tiempo_prox_llegada, tiempo_prox_salida, crear_atributos, chequear_colas, agregar_FEL, imprimir_evento, imprimir_encabezado


# Variables
LLEGADA = 0
ELECCION = 1
ATENDER = 2
SALIDA = 3
Cajas = []
DISPONIBLE = 1
OCUPADA = 0
FEL = []
agenda_cola = []
n = 0


for i in range(0, 10):
    # print(i)
    if i != 9:
        Caja = [i, DISPONIBLE, []]
        Cajas.append(Caja)
    else:
        Caja = ["auto", DISPONIBLE, []]
        Cajas.append(Caja)
# print(Cajas)


####################### LOOP #######################

def loop_rutinas():
    reloj = 0
    cliente = crear_atributos()
    eleccion = chequear_colas(Cajas, cliente)
    primer_evento = (LLEGADA, 5, 1, eleccion)
    FEL = [primer_evento]
    cola = []
    agenda_cola = []
    imprimir_encabezado()
    for i in range(100):
        evento, reloj = tiempo_rutina(FEL, reloj)
        imprimir_evento(evento, agenda_cola, Cajas)
        if evento[0] == LLEGADA:
            llegada_cajas(evento[2], FEL, reloj, Cajas, agenda_cola, cola)
        elif evento[0] == ELECCION:
            eleccion_cola(evento[2], FEL, reloj, Cajas, agenda_cola)
        elif evento[0] == ATENDER:
            atencion(evento[2], FEL, reloj, Cajas, evento[3])
        elif evento[0] == SALIDA:
            salida(evento[2], FEL, reloj, Cajas, evento[3])
    return


####################### RUTINAS #######################

def llegada_cajas(n, FEL, tiempo_evento, Cajas, agenda_cola, cola):
    global cliente, eleccion
    tiempo = tiempo_prox_llegada(tiempo_evento)
    atributos = crear_atributos()
    evento = (LLEGADA, tiempo, n+1)
    agregar_FEL(FEL, evento)
    cliente = (atributos)
    eleccion = chequear_colas(Cajas, cliente)
    if len(Cajas[eleccion][2]) <= 10 and Cajas[eleccion][1] == DISPONIBLE:
        evento = (ELECCION, tiempo_evento, n, eleccion)
        agregar_FEL(FEL, evento)
        agenda_cola.append(evento)
    cola.append(n)
    return


def eleccion_cola(n, FEL, tiempo_evento, Cajas, agenda_cola):
    caja = agenda_cola[0][3]
    Cajas[caja][2].append(n)
    agenda_cola.pop(0)
    tiempo = tiempo_espera(tiempo_evento)
    if (Cajas[caja][1] == DISPONIBLE):
        evento = (ATENDER, tiempo, n+1, caja)
        agregar_FEL(FEL, evento)
    return


def atencion(n, FEL, tiempo_evento, Cajas, eleccion):
    if Cajas[eleccion][1] == DISPONIBLE:
        Cajas[eleccion][1] = OCUPADA
    tiempo = tiempo_prox_salida(tiempo_evento, eleccion)
    evento = (SALIDA, tiempo, n, eleccion)
    agregar_FEL(FEL, evento)
    return


def salida(n, FEL, tiempo_evento, Cajas, eleccion):
    if len(Cajas[eleccion][2]) != 0:
        n = Cajas[eleccion][2].pop(0)
        evento = (ATENDER, tiempo_evento, n, eleccion)
        agregar_FEL(FEL, evento)
    else:
        Cajas[eleccion][1] = DISPONIBLE
