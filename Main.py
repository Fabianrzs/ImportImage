import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, Label


print("Librerias Leidas")

def loadImage():
    img = Image.open("Test/PC.jpg")
    new_img = img.resize((300,256))
    render = ImageTk.PhotoImage(new_img)
    imgView = Label(windows, image=render)
    imgView.image = render
    imgView.place(x=350, y=150)
    labelResult = Label(windows, text="El reconocimiento Determino la letra (A)")
    labelResult.place(x=350, y=410)

def loadMessage():
    labelframe = Label(windows, text="No sea Bruto Eso todavia no sirve")
    labelframe.place(x=350, y=410)

def loadCompents(windows):
    labelframe = Label(windows, text="Entrenamiento de redes neuronales con Bagpropagations")
    labelframe.place(x=10, y=30)

    labelSubtitle = Label(windows, text="Ingrese los parametrros de entramiento de la red")
    labelSubtitle.place(x=10, y=80)


    labelEpoch = Label(windows, text="Iteraciones")
    labelEpoch.place(x=10, y=150)

    labelError = Label(windows, text="Error Permitido")
    labelError.place(x=10, y=230)

    labelTheta = Label(windows, text="Taza de aprenzaje")
    labelTheta.place(x=10, y=310)

    buttonLoad = tk.Button(windows, command=loadImage, text="Cargar Imagen", height=2, width=15)
    buttonLoad.place(x=300, y=450)

    buttonLearn = tk.Button(windows, command=loadMessage, text="Entrenar La red", height=1, width=15)
    buttonLearn.place(x=10, y=400)


windows = tk.Tk()
windows.title("Testing")
windows.geometry("700x500")
loadCompents(windows)
windows.mainloop()

