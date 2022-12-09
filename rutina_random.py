from numpy.random import MT19937, Generator, SeedSequence

# Rutina Random
sg = SeedSequence(1234)
sAuto = SeedSequence(1234)
sClasica = SeedSequence(1234)
sEspera = SeedSequence(1234)
lambdaS = 20
muClasica = 0.5
muAuto = 3


def obt_prox_llegada():
    return Generator(MT19937(sg.spawn(1)[0])).exponential(1/lambdaS)


def obt_prox_salida_Auto():
    return Generator(MT19937(sAuto.spawn(1)[0])).exponential(1/lambdaS)


def obt_prox_salida_Clasica():
    return Generator(MT19937(sClasica.spawn(1)[0])).exponential(1/lambdaS)


def obt_tiempo_espera():
    return Generator(MT19937(sEspera.spawn(1)[0])).exponential(1/lambdaS)


def semilla_llegada(s):
    global sg
    sg = SeedSequence(s)


def semilla_salida_auto(s):
    global sAuto
    sAuto = SeedSequence(s)


def semilla_salida_clasica(s):
    global sClasica
    sClasica = SeedSequence(s)


def semilla_espera(s):
    global sEspera
    sEspera = SeedSequence(s)


def setear_lambda(lam):
    global lambdaS
    lambdaS = lam


def setear_mu_auto(mu):
    global muAuto
    muAuto = mu


def setear_mu_clasica(mu):
    global muClasica
    muClasica = mu
