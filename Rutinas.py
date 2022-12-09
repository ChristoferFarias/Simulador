from funciones import graficos, crear_titulo, tiempo_rutina, tiempo_espera, tiempo_prox_llegada, tiempo_prox_salida, crear_atributos, chequear_colas, agregar_FEL, imprimir_evento, imprimir_encabezado


# Variables
LLEGADA = 0
ELECCION = 1
ATENDER = 2
SALIDA = 3
DISPONIBLE = 1
OCUPADA = 0
FEL = []
tiempos = []
llegadas = []
atenciones = []
elecciones = []
salidas = []
filas = []
# print(Cajas)


####################### LOOP #######################

def inicio():
    global Cajas, n, agenda_cola, FEL
    Cajas = []
    agenda_cola = []
    n = 0
    n_cajas = 5
    for i in range(0, n_cajas):
        if i != (n_cajas-1):
            Caja = [i, DISPONIBLE, []]
            Cajas.append(Caja)
        else:
            Caja = ["auto", DISPONIBLE, []]
            Cajas.append(Caja)
    cliente = crear_atributos()
    eleccion = chequear_colas(Cajas, cliente)
    primer_evento = (LLEGADA, 3, 1, eleccion)
    FEL = [primer_evento]


def loop_rutinas(numero_rutinas):
    global cola
    reloj = 0
    cola = []
    agenda_cola = []
    llegadas_clientes = 0
    atenciones_clientes = 0
    elecciones_clientes = 0
    salidas_clientes = 0
    imprimir_encabezado()
    crear_titulo()
    for i in range(numero_rutinas):
        evento, reloj = tiempo_rutina(FEL, reloj)
        imprimir_evento(evento, agenda_cola, Cajas)
        if evento[0] == LLEGADA:
            llegada_cajas(evento[2], FEL, reloj, Cajas, agenda_cola, cola)
            llegadas_clientes += 1
        elif evento[0] == ELECCION:
            eleccion_cola(evento[2], FEL, reloj, Cajas, agenda_cola, cliente)
            elecciones_clientes += 1
        elif evento[0] == ATENDER:
            atencion(evento[2], FEL, reloj, Cajas, evento[3])
            atenciones_clientes += 1
        elif evento[0] == SALIDA:
            salida(evento[2], FEL, reloj, Cajas, evento[3])
            salidas_clientes += 1
        tiempos.append(reloj)
        llegadas.append(llegadas_clientes)
        elecciones.append(elecciones_clientes)
        atenciones.append(atenciones_clientes)
        salidas.append(salidas_clientes)
    graficos(tiempos, llegadas, elecciones, atenciones, salidas)
    return


####################### RUTINAS #######################

def llegada_cajas(n, FEL, tiempo_evento, Cajas, agenda_cola, cola):
    global cliente, eleccion
    tiempo = tiempo_prox_llegada(tiempo_evento)
    atributos = crear_atributos()
    evento = (LLEGADA, tiempo, n+1)
    agregar_FEL(FEL, evento)
    cliente = atributos
    eleccion = chequear_colas(Cajas, cliente)
    if len(Cajas[eleccion][2]) <= 10:
        evento = (ELECCION, tiempo_evento, n, eleccion)
        agregar_FEL(FEL, evento)
        agenda_cola.append(evento)
    cola.append(n)
    return


def eleccion_cola(n, FEL, tiempo_evento, Cajas, agenda_cola, cliente):
    caja = agenda_cola[0][3]
    Cajas[caja][2].append(n)
    # print(Cajas[caja][2])
    agenda_cola.pop(0)
    cola.pop(0)
    tiempo = tiempo_espera(tiempo_evento, cliente)
    if (Cajas[caja][1] == DISPONIBLE and len(Cajas[caja][2]) == 1):
        n = Cajas[caja][2].pop(0)
        evento = (ATENDER, tiempo, n, caja)
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
