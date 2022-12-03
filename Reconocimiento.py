import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, Label, Entry, StringVar


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

    print(Theta.get())
    print(Error.get())
    print(epoch.get())

def loadCompents(windows):



    labelframe = Label(windows, text="Entrenamiento de redes neuronales con Bagpropagations")
    labelframe.place(x=10, y=30)

    labelSubtitle = Label(windows, text="Ingrese los parametrros de entramiento de la red")
    labelSubtitle.place(x=10, y=80)


    labelEpoch = Label(windows, text="Iteraciones")
    labelEpoch.place(x=10, y=150)

    entryEpoch = Entry(windows, relief="flat", width=20, textvariable=epoch)
    entryEpoch.place(x=10, y=180)

    labelError = Label(windows, text="Error Permitido")
    labelError.place(x=10, y=230)

    entryError = Entry(windows, relief="flat", width=20, textvariable=Error)
    entryError.place(x=10, y=260)

    labelTheta = Label(windows, text="Taza de aprenzaje")
    labelTheta.place(x=10, y=310)

    entryTheta = Entry(windows, relief="flat", width=20, textvariable=Theta)
    entryTheta.place(x=10, y=340)


    buttonLoad = tk.Button(windows, command=loadImage, text="Cargar Imagen", height=2, width=15)
    buttonLoad.place(x=300, y=450)

    buttonLearn = tk.Button(windows, command=loadMessage, text="Entrenar La red", height=1, width=15)
    buttonLearn.place(x=10, y=400)



windows = tk.Tk()
windows.title("Testing")
windows.geometry("700x500")


epoch = DoubleVar()
Error = DoubleVar()
Theta = DoubleVar()

loadCompents(windows)


valores = ""
print("Hola: ",valores )
windows.mainloop()

