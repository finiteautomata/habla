#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np
import scipy.io.wavfile
#import matplotlib.pyplot as pyplot

# Definimos una función senoidal simple.
def ondasimple(t, f=440, a=1.0):
    Phi = 0.0  # fase
    return a * np.sin(2 * np.pi * f * t + Phi)

def onda_sinusoidal(hz, length=1, amplitude=10000, sampling=16000):
    # Generamos 16000 puntos a 16kHz.
    ts = np.arange(sampling * length) / float(sampling)
    return np.array([ondasimple(t, f=hz, a=amplitude) for t in ts ])

def guardar(onda, filename):
    # La guardamos como wav.
    with open(filename, "wb") as f:
        scipy.io.wavfile.write(f, 16000, np.array(onda, dtype=np.int16) )


# Ejercicios:
#
# 1. Generar un archivo wav para cada nota musical Do, Re, Mi,
#    Fa, Sol, La, Si. Consultar las frecuencias en
#    http://www.phy.mtu.edu/~suits/notefreqs.html
#    Tomar como referencia La = 440Hz.

notas = [
    ("C4", 261.63),
    ("D4", 293.66),
    ("E4", 329.63),
    ("F4", 349.23), 
    ("G4", 392.00), 
    ("A4", 440.00), 
    ("B4", 493.88)
] 

for (nombre, freq) in notas:
    guardar(onda_sinusoidal(freq, length=1.0, amplitude=30000), "notas/{}.wav".format(nombre))

# 2. Buscar la frecuencia más aguda y más grave que pueden percibir.
#
# 3. Percepcion relativa. Escuchar la diferencia entre dos tonos graves
#    separados por 100Hz (ej: 200 y 300Hz) y dos tonos agudos separados
#    también por 100Hz (ej: 1200 y 1300Hz).
#
# 4. Crear una onda cuadrada a 500 Hz, modificando ondasimple(t) de modo
#    que devuelva solamente 1 o -1. Generar un wav y comparar con una
#    senoidal de la misma frecuencia.
#
# 5. Repetir el punto anterior para 100Hz y para 1000Hz. ¿En algún caso
#    suenan parecidas las ondas senoidales y cuadradas? (Más allá de las
#    diferencias de volumen).

