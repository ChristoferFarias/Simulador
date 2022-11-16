from Rutinas import loop_rutinas
from rutina_random import semilla_llegada, semilla_salida_auto, semilla_salida_clasica, setear_lambda, setear_mu_auto, setear_mu_clasica

####################### INICIO #######################

print("COMENZANDO SIMULACIÓN")
semilla_llegada(312)
semilla_salida_auto(3)
semilla_salida_clasica(1)
setear_lambda(10)
setear_mu_auto(4)
setear_mu_clasica(.5)
loop_rutinas()
