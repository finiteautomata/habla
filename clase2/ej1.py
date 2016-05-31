#!/usr/bin/python
# -*- coding: latin-1 -*-
import math
import numpy as np
import scipy.io.wavfile
import sounddevice as sd
from sounddevice import play

#import matplotlib.pyplot as pyplot

sd.default.samplerate = 44100

# Defino funciones periódicas entre 0 y 1
def mysin(t):
    return np.sin(2*np.pi*t)

def cuadrada(t):
    if (t - math.floor(t)) <= 0.5:
        return 1
    else:
        return -1


def triang(t):
    l = t - math.floor(t)
    if l <= 0.25:
        return 4*l
    elif l <= 0.5:
        return 1 - 4*(l - 0.25)
    elif l <= 0.75:
        return -4*l
    else:
        return -1 + 4*(l - 0.75)
# Definimos una función senoidal simple.

def onda(hz, length=1, fun=mysin, amplitude=10000, sampling=sd.default.samplerate):
    # Generamos 16000 puntos a 16kHz.
    ts = np.arange(sampling * length) / float(sampling)
    return amplitude * np.array([fun(hz * t) for t in ts ])

def to_wav(wave):
    return np.array(wave, dtype=np.int16)

def guardar(onda, filename):
    # La guardamos como wav.
    with open(filename, "wb") as f:
        scipy.io.wavfile.write(f, sd.default.samplerate, to_wav(onda))


def reproducir(onda):
    play(to_wav(onda))
    sd.wait()

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
