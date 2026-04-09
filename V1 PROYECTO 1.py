from tkinter import *
from PIL import Image, ImageTk
import os

# -----------------------------------------
# canva
# -----------------------------------------
canva = Tk()
canva.title("Proyecto 1") 
canva.minsize(1500,1000) 
canvas = Canvas(canva, width=1500, height=1000)
canvas.pack() 

#Fondo de la pantalla principal 
def cargarImg(nombre, size=None):
    ruta = os.path.join('img', nombre)
    img = Image.open(ruta)
    if size:
        img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

img = cargarImg("Laboratorio.png")
canvas.image = img
canvas.create_image(0, 0, anchor='nw', image=img)

#Solicitar nombre

Label(canvas, text="Ingrese su nombre: ", font=('Agency FB',14), 
      bg="#f8f8f8", fg='black').place(x=130,y=80)
nombre = Entry(canvas, width=20, font=('Agency FB',14))
nombre.place(x=130,y=105)

# Texto About

Button(canvas, text="Información", font=('Agency FB',14), 
      bg="#f8f8f8", fg='black', command=lambda: infocanva() ).place(x=130,y=140)
def infocanva():
    info = Toplevel()
    info.title("Información")
    info.resizable(width=NO,height=NO)

    Canvainfo = Canvas(info, width=319, height=190)
    Canvainfo.pack()

    Label(Canvainfo, text=about, font=('Agency FB',14), 
      bg="#8a4747", fg='black', borderwidth=10, justify='center').place(x=0,y=0)
    
about = """Instituto Tecnologico de Costa Rica
Computer Engineering
Introducción a la programación
Ana Victoria Araya Núñez
Juego de peleas 3 vs 3 
2026
Version: 1
"""
# -----------------------------------------
# botones
# -----------------------------------------
Label(canvas, text="Seleccione un personaje", font=('Agency FB',14), 
      bg="#77b67c", fg='black').place(x=130,y=200)

# -----------------------------------------
# Pantalla del mapa 
# -----------------------------------------

def ventanajuego():
    canva.withdraw()

    Mundos = Toplevel()
    Mundos.title("Mundos")
    Mundos.minsize(1500,800)
    Mundos.resizable(width=NO,height=NO)

    fjuego = Canvas(Mundos, width=1500, height=800)
    fjuego.pack()


    fp_img = cargarImg("fondoprincipal.jpg", size= (1500, 800))
    fjuego.create_image(0,0,anchor='nw', image=fp_img) 
    fjuego.image = fp_img 

    #Titulo de los mundos
    Label(fjuego, text="Mapa", font=('Agency FB',18), bg="#000000", fg="white", borderwidth=15, justify='center').place(x=700, y=50)
    

    #Boton Primer mundo - DESIERTO 
    def mapa_desierto():
        Mundos.withdraw()

        desierto = Toplevel()
        desierto.title("desierto")
        desierto.minsize(1500, 800)
        desierto.resizable(width=NO, height=NO)

        fdesierto = Canvas(desierto, width=1500, height=800)
        fdesierto.pack()

        fd_img = cargarImg("DesiertoG.jpg", size=(1500,800))
        fdesierto.create_image(0,0,anchor='nw', image=fd_img) 
        fdesierto.image = fd_img

    playdesert = cargarImg("DesiertoP.jpg", size=(350,190))
    Button(fjuego, text="desierto", image=playdesert, fg= "#970f0f", command=mapa_desierto).place(x=100, y=200)
    Image.open (playdesert)


Button(canva, text="Jugar", fg="#206d91", font=('Agency FB',14),
       command=ventanajuego).place(x=280,y=140)


canva.mainloop()
