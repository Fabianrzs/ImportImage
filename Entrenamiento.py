import openpyxl
import pandas as pd


#Leer los archivos desde el excel

wb = openpyxl.Workbook()


theta = 0.4

aprove = 0.2

#Definicion de pesos
#Pesos por entradas o columnas
w = 0.3

epochs = 0

#Vector de entradas
#Dados por columnas
x1 = 1 #Columnas del archivo
x2 = 1 #Columnas del archivo Hasta finalizar


#Matriz de validacion
#Dada por columnas
s = 3 #Columnas del archivo de validacion

n_muestra = len(s) #Numero de salidas asociadas



def entrenar(theta, aprove, pesos, epochs, entradas, salidas, muestras):

    errores = True
    while errores :
        errores = False
        for i in range (muestras):

            z = ((entradas[i][i] * pesos[i]) + ())