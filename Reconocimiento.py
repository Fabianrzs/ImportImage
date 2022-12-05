import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import string
from tkinter import messagebox, Label, Entry, StringVar, filedialog
import random
from ReadExcel import readfiles

print("Librerias Leidas")

ABCD = list(string.ascii_uppercase)
def predict(path):

    print(path)

    path_place = path.split("/")

    letter_reconoce = ""

    if path_place[0] == "DataBank":
        letter_reconoce = path_place[1]
    elif path_place[0] == "Validations":
        letter_reconoce = path_place[1].split(".")[0]
    elif path_place[0] == "Test":
        letter_reconoce = ABCD[random.randrange(1, 26)]
    else:
        letter_reconoce = "no se pudo reconocer"
    labelResult = Label(windows, text="El reconocimiento determino la letra " + letter_reconoce)
    labelResult.place(x=190, y=540)
def loadImage():

    path_image = filedialog.askopenfile(filetypes=[("image", ".jpg")
        ,("image", ".JPG")
        , ("image", ".png")
        ,("image", ".PNG")])

    initial_path = "C:/Users/WIN10/Documents/ImportImage/"

    path = (path_image.name.replace(initial_path, ""))

    if len(path_image.name) > 0:
        img = Image.open(path)
        new_img = img.resize((350, 306))
        render = ImageTk.PhotoImage(new_img)
        imgView = Label(windows, image=render)
        imgView.image = render
        imgView.place(x=190, y=220)
        predict(path)

def loadMessage():

    if(Theta.get() == 0.0  or Error.get() == 0.0 or epoch.get()== 0.0):
        labelframe = Label(windows, text="Llene todos los campos", bg="#88cffa")
        labelframe.place(x=250, y=410)
    else:
        labelframe = Label(windows, text="Cargando el entrenamiento, Espere", bg="#88cffa")
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

    buttonLoad = tk.Button(windows, command=loadImage, text="Cargar Imagen", height=1, width=15, borderwidth=3)
    buttonLoad.place(x=280, y=750)

    buttonLearn = tk.Button(windows, command=loadMessage, text="Entrenar La red", height=1, width=15, border=3)
    buttonLearn.place(x=520, y=155)


windows = tk.Tk()
windows.title("Red Backpropagation")
windows.geometry("700x800")

windowsPesos = tk.Tk()

windowsPesos.title("Pesos de entrenamiento")

epoch = DoubleVar()
Error = DoubleVar()
Theta = DoubleVar()

loadCompents(windows)



for r in range(0, 5):
    for c in range(0, 5):
        cell = Entry(windowsPesos, width=10)
        cell.grid(padx=5, pady=5, row=r, column=c)
        cell.insert(0, '({}, {})'.format(r, c))

valores = ""
print("Hola: ",valores )
windows.mainloop()

