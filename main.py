import tkinter
from rembg import remove
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog
import random



def selectImage():

        path = './Images'

        file_path = filedialog.askopenfilename(  # Abrir el explorador de archivos
            title="Seleccionar imagen",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]  # Filtrar tipos de archivo
        )

        if not os.path.exists(path):
            os.mkdir(path)


        if file_path:
            print(f"Ruta seleccionada: {file_path}")  # Mostrar la ruta en consola
            output_path = 'Images/'+str(random.randint(0, 10000000))+'.png'
            input = Image.open(file_path)
            output = remove(input)
            output.save(output_path)



#Config variables
background = "#d4e6f1"


#Window´s parameters
window = tkinter.Tk()
window.title("Image background remover")
window.config(width=300,height=200, bg=background)
window.resizable(False, False)


#Widgets
title = tkinter.Label(text="Image background remover", anchor="center", font="{Arial 30 bold}", bg=background)
title.place(x=30, y=0)


#Load image
image_path = "src/cover_page.jpg"

try:
    image = Image.open(image_path)
    max_width, max_height = 200, 180
    image.thumbnail((max_width, max_height))

    image_tk = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")


# Show image
image_label = tk.Label(image= image_tk)
image_label.place(x=60, y=35)


#Button
button = tkinter.Button(text='Select image',width=28, bg="#fafafa", command=selectImage)
button.place(x=60,y=160)


#start window
window.mainloop()