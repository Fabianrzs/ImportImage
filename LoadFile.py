import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Label, filedialog
import openpyxl
import cv2
from mathLabDB import loadDataBank

wb = openpyxl.Workbook()  # Crear archivo excel

def loadImage():

    path_image = filedialog.askopenfile(filetypes=[("image", ".jpg")
        ,("image", ".JPG")
        , ("image", ".png")
        ,("image", ".PNG")])

    initial_path = "C:/Users/WIN10/Documents/ImportImage/"

    path = (path_image.name.replace(initial_path, ""))

    print(path)

    if len(path_image.name) > 0:
        img = Image.open(path)
        new_img = img.resize((300, 276))
        render = ImageTk.PhotoImage(new_img)
        imgView = Label(windows, image=render)
        imgView.image = render
        imgView.place(x=183, y=75)
        sheet = wb.active

        img = cv2.imread(path, 2)
        ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # sistema de quemado de imagen gray
        bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # vectorizado

        countRow = 1
        countCol = 1

        for row in bw_img:
            countData = 0
            for data in row:
                countData += data / 255
            sheet.cell(row=countRow, column=countCol, value=countData)
            countCol += 1

        print("termine :v")
        wb.save('files/Validations.xlsx')

def loadCompents(windows):
    windows.title("Redes Neuronales Bagpropagations")
    windows.configure(bg="#88cffa")
    labelframe = Label(windows, text="Entrenamiento de redes neuronales con Bagpropagations", font=("Arial",18,"bold"),bg="#88cffa")
    labelframe.place(x=10, y=30)

    buttonLoad = tk.Button(windows, command=loadImage, text="Cargar Imagen", height=1, width=15, borderwidth=3)
    buttonLoad.place(x=380, y=360)

    buttonLoad = tk.Button(windows, command=loadDataBank, text="Banco de Datos", height=1, width=15, borderwidth=3)
    buttonLoad.place(x=180, y=360)

windows = tk.Tk()
windows.title("Red Backpropagation")
windows.geometry("700x400")
loadCompents(windows)
windows.mainloop()

