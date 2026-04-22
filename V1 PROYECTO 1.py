from tkinter import *
from PIL import Image, ImageTk
import os
import random


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

img = cargarImg("Paisaje.png")
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

#Personajes
Label(canvas, text="Seleccione un personaje", font=('Agency FB',14), 
      bg="#77b67c", fg='black').place(x=130,y=200)
Personaje1 = cargarImg("personaje1.png", size=(130,300))
b_1 = Button(canvas, image=Personaje1, command=lambda: desha_personajes(personajes, 0, b_1))
b_1.place(x=100, y=300)
Personaje2 = cargarImg("personaje2.png", size=(130,300))
b_2 = Button(canvas, image=Personaje2, command=lambda: desha_personajes(personajes, 0, b_2))
b_2.place(x=250, y=300)
Personaje3 = cargarImg("personaje3.png", size=(130,300))
b_3= Button(canvas, image=Personaje3, command=lambda: desha_personajes(personajes, 0, b_3))
b_3.place(x=400, y=300)

personajes = [b_1, b_2, b_3]
def desha_personajes(lista, l, boton):
    if l >= len(lista):
        return
    p = lista[l]

    if boton == p: 
        p.config(relief="sunken")
    else:
        p.config(relief="raised", state=NORMAL)

    desha_personajes(lista, l + 1, boton)
    
#Animales 
Label(canvas, text="Seleccione 3 animales", font=('Agency FB',14), 
      bg="#77b67c", fg='black').place(x=1150,y=50)

CamelloP = cargarImg("Camello.png", size=(80,120))
b_ca = Button(canvas, image=CamelloP,command=lambda: desha_animales(botones, 0, b_ca))
b_ca.place(x=1100, y=100)
AlacranP = cargarImg("alacran.png", size=(80,120))
b_al = Button(canvas, image=AlacranP,command=lambda: desha_animales(botones, 0, b_al))
b_al.place(x=1200, y=100)
AvestruzP = cargarImg("avestruz.png", size=(80,120))
b_av = Button(canvas, image=AvestruzP,command=lambda: desha_animales(botones, 0, b_av))
b_av.place(x=1300, y=100)
BuhoP = cargarImg("buho.png", size=(80,120))
b_bu = Button(canvas, image=BuhoP,command=lambda: desha_animales(botones, 0, b_bu))
b_bu.place(x=1100, y=250)
ZorroP = cargarImg("zorro.png", size=(80,120))
b_zo = Button(canvas, image=ZorroP,command=lambda: desha_animales(botones, 0, b_zo))
b_zo.place(x=1200, y=250)
OsoP = cargarImg("oso.png", size=(80,120))
b_os = Button(canvas, text="oso", image=OsoP,command=lambda: desha_animales(botones, 0, b_os))
b_os.place(x=1300, y=250)
TortugaP = cargarImg("tortuga.png", size=(80,120))
b_to = Button(canvas, text="tortuga", image=TortugaP,command=lambda: desha_animales(botones, 0, b_to))
b_to.place(x=1100, y=400)
PelicanoP = cargarImg("pelicano.png", size=(80,120))
b_pe = Button(canvas, text="pelicano", image=PelicanoP,command=lambda: desha_animales(botones, 0, b_pe))
b_pe.place(x=1200, y=400)
CangrejoP = cargarImg("cangrejo.png", size=(80,120))
b_can = Button(canvas, text="cangrejo", image=CangrejoP,command=lambda: desha_animales(botones, 0, b_can))
b_can.place(x=1300, y=400)
LeonP = cargarImg("leon.png", size=(80,120))
b_le = Button(canvas, image=LeonP,command=lambda: desha_animales(botones, 0, b_le))
b_le.place(x=1100, y=550)
JirafaP = cargarImg("jirafa.png", size=(80,120))
b_ji = Button(canvas, image=JirafaP,command=lambda: desha_animales(botones, 0, b_ji))
b_ji.place(x=1200, y=550)
CobraP = cargarImg("cobra.png", size=(80,120))
b_co = Button(canvas, image=CobraP, command=lambda: desha_animales(botones, 0, b_co))
b_co.place(x=1300, y=550)
LinceP = cargarImg("lince.png", size=(80,120))
b_li = Button(canvas, image=LinceP, command=lambda: desha_animales(botones, 0, b_li))
b_li.place(x=1100, y=700)
YakP = cargarImg("yak.png", size=(80,120))
b_ya = Button(canvas, image=YakP, command=lambda: desha_animales(botones, 0, b_ya))
b_ya.place(x=1200, y=700)
RenoP = cargarImg("reno.png", size=(80,120))
b_re = Button(canvas, image=RenoP, command=lambda: desha_animales(botones, 0, b_re))
b_re.place(x=1300, y=700)
#listas de animales

animal1 = [b_ca, b_bu, b_to, b_le, b_li]
animal2 = [b_al, b_zo, b_pe, b_ji, b_ya]
animal3 = [b_av, b_os, b_can, b_co, b_re]
botones = [animal1, animal2, animal3]

def desha_animales(listas, l, boton):
    if l >= len(listas):
        return
    lista = listas[l]

    if boton in lista:
        desha_botones(lista, 0, boton)

    desha_animales(listas, l + 1, boton)

def desha_botones(botones, j, animal):
    if j >= len(botones):
        return

    if botones[j] == animal:
        botones[j].config(relief="sunken")
    else:
        botones[j].config(relief="raised",state=NORMAL)

# -----------------------------------------
# Pantalla del mapa 
# -----------------------------------------

def ventanajuego(nombre_jugador):
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

    L_nombre = Label(fjuego, text=f"Jugador:\n {nombre_jugador} ", font=('Agency FB',16),
                     fg='white', bg='#353a4e')
    L_nombre.place(x=50, y=550)

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

        fd_img = cargarImg("DesertG.jpg", size=(1500,800))
        fdesierto.create_image(0,0,anchor='nw', image=fd_img) 
        fdesierto.image = fd_img

        #Camello pelea
        camello = cargarImg("camello.png", size=(300,400))
        fdesierto.create_image(1000,400, anchor='nw', image=camello)
        fdesierto.image = camello 
        

    playdesert = cargarImg("DesertP.jpg", size=(350,190))
    Button(fjuego, text="desierto", image=playdesert, fg= "#970f0f", command=mapa_desierto).place(x=100, y=200)
    Image.open (playdesert)

def empezar_juego():
    nombre1 = nombre.get()
    ventanajuego(nombre1)

Button(canva, text="Jugar", fg="#206d91", font=('Agency FB',14),
       command=empezar_juego).place(x=280,y=140)


canva.mainloop()
