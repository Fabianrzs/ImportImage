import tkinter as tk
from tkinter import *
#from PIL import Image, ImageTk
from tkinter import messagebox, Label, Entry, StringVar

print("Librerias Leidas")

#def loadImage():
 #   img = Image.open("Test/PC.jpg")
 #  new_img = img.resize((300,256))
 #   render = ImageTk.PhotoImage(new_img)
 #   imgView = Label(windows, image=render)
 #   imgView.image = render
 #   imgView.place(x=250, y=220)
 #   labelResult = Label(windows, text="El reconocimiento Determino la letra (A)")
 #   labelResult.place(x=250, y=410)

def loadMessage():
    labelframe = Label(windows, text="No sea Bruto Eso todavia no sirve", bg="#88cffa")
    labelframe.place(x=250, y=410)

    print(Theta.get())
    print(Error.get())
    print(epoch.get())

def loadCompents(windows):


    windows.title("Redes Neuronales Bagpropagations")
    #image_fondo=tk.PhotoImage(file="1.png")
    windows.configure(bg="#88cffa")
    labelframe = Label(windows, text="Entrenamiento de redes neuronales con Bagpropagations", font=("Arial",18,"bold"),bg="#88cffa")
    labelframe.place(x=10, y=30)

    labelSubtitle = Label(windows, text="Parametrros de entramiento de la red", font=("Arial",15), bg="#88cffa")
    labelSubtitle.place(x=140, y=80)


    labelEpoch = Label(windows, text="Iteraciones", font=("Arial",13), bg="#88cffa")
    labelEpoch.place(x=10, y=130)

    entryEpoch = Entry(windows, relief="flat", width=20, textvariable=epoch)
    entryEpoch.place(x=10, y=160)

    labelError = Label(windows, text="Error Permitido",font=("Arial",13), bg="#88cffa")
    labelError.place(x=170, y=130)

    entryError = Entry(windows, relief="flat", width=20, textvariable=Error)
    entryError.place(x=170, y=160)

    labelTheta = Label(windows, text="Taza de aprenzaje", font=("Arial",13), bg="#88cffa")
    labelTheta.place(x=320, y=130)

    entryTheta = Entry(windows, relief="flat", width=20, textvariable=Theta)
    entryTheta.place(x=324, y=160)

    #buttonLoad = tk.Button(windows, command=loadImage, text="Cargar Imagen", height=2, width=15, borderwidth=5)
    #buttonLoad.place(x=280, y=450)

    buttonLearn = tk.Button(windows, command=loadMessage, text="Entrenar La red", height=1, width=15, border=5)
    buttonLearn.place(x=520, y=145)



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

