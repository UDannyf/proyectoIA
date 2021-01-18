import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import filedialog

window = Tk()
window.title("Neuronales - Proyecto Inteligencia Artificial")
window.geometry("840x500")
window.resizable(False, False)
window.filename = ""


estilo = Style()
estilo.configure('cargar.Button', font=('Verdana', 12), background='blue')
estilo.configure('resetear.Button', font=('Verdana', 12), background='red')
estilo.configure('analizar.Button', font=('Verdana', 12), background='green')

longitud, altura = 150, 150
modelo = './modeloCNN/modelo.h5'
pesos_modelo = './modeloCNN/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)


def cargarImagen():
  window.filename = filedialog.askopenfilename(initialdir="", title="Select an image", 
                                             filetypes=(("TIFF Files", "*.tiff"), ("JPG Files", "*.jpg"), ("PNG Files", "*.png")))
  if window.filename:
    fondo = ImageTk.PhotoImage(Image.open(window.filename).resize((400, 400), Image.ANTIALIAS))
    subida.configure(image=fondo)
    subida.image = fondo

def reinicarImagen():
  window.filename = ""
  fondo = ImageTk.PhotoImage(Image.open('./img/sinImagen.jpg').resize((400, 400), Image.ANTIALIAS))
  subida.configure(image=fondo)
  subida.image = fondo

  titulo = Label(window, text="", font=('Verdana', 24))
  titulo.place(x=550, y=280)
  titulo.config(width=75)

  muestra = Label(window, text="", font=('Verdana', 14))
  muestra.place(x=465, y=355)
  muestra.config(width=50)

  resultado = Label(window, text="", font=('Verdana', 18))
  resultado.place(x=615, y=350)
  resultado.config(width=50)

  canvas = Canvas(window, width=15, height=15, borderwidth=0, highlightthickness=0)
  canvas.place(x=750, y=360)

def predict():
  file = window.filename
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)

  titulo = Label(window, text="Resultado", font=('Verdana', 24))
  titulo.place(x=550, y=280)
  titulo.config(width=75)

  if answer == 0:
    muestra = Label(window, text="La muestra es: ", font=('Verdana', 14))
    muestra.place(x=465, y=355)
    muestra.config(width=50)

    resultado = Label(window, text="POSITIVA", font=('Verdana', 18))
    resultado.place(x=615, y=350)
    resultado.config(width=50)

    canvas = Canvas(window, width=15, height=15, borderwidth=0, highlightthickness=0, bg="red")
    canvas.place(x=750, y=360)

  elif answer == 1:
    muestra = Label(window, text="La muestra es: ", font=('Verdana', 14))
    muestra.place(x=465, y=355)
    muestra.config(width=50)

    resultado = Label(window, text="NEGATIVA", font=('Verdana', 18))
    resultado.place(x=615, y=350)
    resultado.config(width=50)

    canvas = Canvas(window, width=15, height=15, borderwidth=0, highlightthickness=0, bg="green")
    canvas.place(x=750, y=360)


fondo = ImageTk.PhotoImage(Image.open("./img/sinImagen.jpg").resize((400, 400), Image.ANTIALIAS))
subida = Label(window, image=fondo)
title = Label(window, text="Diagnóstico de Leucemia en muestras de sangre", font=('Verdana', 24))

titulo = Label(window, text="",font=('Verdana', 15))
resultado = Label(window, text="",font=('Verdana', 12))
titulo.config(width=150)

body = Frame(window).pack()
subir = Button(body, text="Subir Imagen", command=cargarImagen)
resetear = Button(body, text="Resetear Imagen", command=reinicarImagen)
analizar = Button(body, text="Analizar Imagen", command=predict)

title.pack(pady=10)
titulo.place(x=750,y=350)
resultado.place(x=750,y=375)
subida.place(x=25, y=70)
subir.place(x=500,y=150)
resetear.place(x=650, y=150)
analizar.place(x=580, y=200)


window.mainloop()