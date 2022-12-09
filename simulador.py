from Rutinas import loop_rutinas, inicio
from rutina_random import semilla_llegada, semilla_salida_auto, semilla_salida_clasica, setear_lambda, setear_mu_auto, setear_mu_clasica

####################### INICIO #######################

print("############COMENZANDO SIMULACIÓN############")
semilla_llegada(3)
semilla_salida_auto(1)
semilla_salida_clasica(2)
setear_lambda(100)
setear_mu_auto(8)
setear_mu_clasica(3)
inicio()
loop_rutinas(1000000)
# print(Cajas)
