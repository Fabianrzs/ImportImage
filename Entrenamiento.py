import numpy as np
from numpy import random
import matplotlib.pyplot as plt


class MLP():
    def __init__(self, xi, d, w_1, w_2, us, uoc, precision, epocas, fac_ap, n_ocultas, n_entras, n_salidas):
        print("Init")
def tanh(x):
    return np.tanh(x)

def dtanh(x):
    return 1.0 - np.tanh(x)**2

def sigmoide(x):
    return 1/(1+np.exp(-x))

def dsingmoide(x):
    s =  1/(1+np.exp((-x)))
    return s*(1-s)

