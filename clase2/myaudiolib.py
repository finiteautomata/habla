# -*- coding: utf-8 -*-

import math
import numpy as np
import scipy.io.wavfile
import sounddevice as sd
from sounddevice import play

#import matplotlib.pyplot as pyplot

sd.default.samplerate = 44100

# Defino funciones periódicas entre 0 y 1
def mysin(t, phase=0):
    return np.sin(2*np.pi*t+phase)

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

