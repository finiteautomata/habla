# -*- coding: utf-8 -*-

from myaudiolib import onda, guardar, cuadrada, triang, mysin, reproducir
# Ejercicios:
#
# 1. Generar un archivo wav para cada nota musical Do, Re, Mi,
#    Fa, Sol, La, Si. Consultar las frecuencias en
#    http://www.phy.mtu.edu/~suits/notefreqs.html
#    Tomar como referencia La = 440Hz.
# 4. Crear una onda cuadrada a 500 Hz, modificando ondasimple(t) de modo
#    que devuelva solamente 1 o -1. Generar un wav y comparar con una
#    senoidal de la misma frecuencia.
#
# 5. Repetir el punto anterior para 100Hz y para 1000Hz. ¿En algún caso
#    suenan parecidas las ondas senoidales y cuadradas? (Más allá de las
#    diferencias de volumen).

# Esto es la tabla de frecuencias
frecuencias = {
    "do": 261.63,
    "re": 293.66,
    "mi": 329.63,
    "fa": 349.23,
    "sol": 392.00,
    "la": 440.00,
    "si": 493.88
}

# Devuelve un diccionario con todas las ondas de las notas usando func como función periódica

def ondas_de_notas(func=mysin):
    ondas = {}
    for (nota, frecuencia) in frecuencias.iteritems():
        ondas[nota] = onda(frecuencia, fun=func, length=1.0, amplitude=30000)
    return ondas

notas_sin = ondas_de_notas(mysin)
notas_cuad = ondas_de_notas(cuadrada)
notas_triang = ondas_de_notas(triang)

for (nombre, nota) in notas_sin.iteritems():
    guardar(nota, "notas/{}.wav".format(nombre))
