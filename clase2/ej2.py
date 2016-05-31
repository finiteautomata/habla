#!/usr/bin/python
# -*- coding: latin-1 -*-
import matplotlib.pyplot as pyplot
import random
import sounddevice as sd
from myaudiolib import onda, guardar, cuadrada, triang, mysin, reproducir


# # Mostramos su espectrograma.
# import pylab
# pyplot.clf()
# sgram = pylab.specgram(mionda, Fs=16000.0)
# pyplot.savefig('espectrograma.png')


# Ejercicios:
#
# 1. Crear una onda de ruido blanco y mostrar su espectrograma.
#    Ayuda: Usar 'random.uniform(-1, 1)' del módulo random.
#
# 2. Crear una senoidal simple y combinarla con ruido blanco. Mostrar su
#    espectrograma.
#
# 3. Crear una senoidal simple con frecuencia ascendente y mostrar su
#    espectrograma.
#
# 4. Combinar dos senoidales con frecuencias 1000 y 100Hz con distintas
#    fases (ej: 0 y pi), y comparar las formas de onda. ¿Tiene algún efecto
#    perceptual el cambio de fase?
#
# 5. Crear dos senoidales simples con la misma frecuencia pero distintas
#    fases, de modo que al combinarlas se anulen.
#    http://en.wikipedia.org/wiki/Active_noise_control

