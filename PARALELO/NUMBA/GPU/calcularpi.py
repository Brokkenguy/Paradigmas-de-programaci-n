#--------------------------------------
#  Montecarlo en PYTHON CUDA NUMBA
#--------------------------------------
from __future__ import print_function, absolute_import
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128p_uniform_float64
import numpy as np
import random

@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out):
    """Encontrar el valor máximo en value y guardarlo en result[0]"""
    ii = cuda.grid(1)

    # Calcular pi dibujando puntos (x, y) al azar y encontrando 
    # la fracción de ellos que cae dentro del círculo unitario
    cae_adentro = 0
    for i in range(iteraciones):
