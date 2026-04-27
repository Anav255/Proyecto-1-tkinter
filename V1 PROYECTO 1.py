from tkinter import *
from PIL import Image, ImageTk
import os
import random
import csv

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

img = cargarImg("fondo.jpg")
canvas.image = img
canvas.create_image(0, 0, anchor='nw', image=img)


#Solicitar nombre

Label(canvas, text="Ingrese su nombre: ", font=('Times New Roman',14), 
      bg="#f8f8f8", fg='black').place(x=130,y=80)
nombre1 = Entry(canvas, width=20, font=('Agency FB',14))
nombre1.place(x=130,y=105)


# Texto About

Button(canvas, text="Información", font=('Times New Roman',14), bg="#f8f8f8", fg='black', command=lambda: infocanva()).place(x=130,y=140)
def infocanva():
    info = Toplevel()
    info.title("Información")
    info.resizable(width=NO,height=NO)

    Canvainfo = Canvas(info, width=285, height=170)
    Canvainfo.pack()

    Label(Canvainfo, text=about, font=('Times New Roman',14), bg="#73b1ca", fg='black', borderwidth=10, justify='center').place(x=0,y=0)
    
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
Label(canvas, text="Seleccione un personaje", font=('Times New Roman',18), bg="#CAD4E2", fg='black').place(x=130,y=220)
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

Personaje = []
def personajepelea(opciones):
    global Personaje
    if opciones in Personaje:
        return Personaje.clear()
    Personaje.append(opciones)
    desha_personajes(personajes, 0, opciones)
#Animales 
Label(canvas, text="Seleccione 3 animales", font=('Times New Roman',14), 
      bg="#77b67c", fg='black').place(x=1150,y=50)

CamelloP = cargarImg("Camello.png", size=(80,120))
b_ca = Button(canvas, text="camello", image=CamelloP,command=lambda: animalpelea(b_ca))
b_ca.place(x=1100, y=100)
AlacranP = cargarImg("alacran.png", size=(80,120))
b_al = Button(canvas, text="alacran", image=AlacranP,command=lambda: animalpelea(b_al))
b_al.place(x=1200, y=100)
AvestruzP = cargarImg("avestruz.png", size=(80,120))
b_av = Button(canvas, text="avestruz", image=AvestruzP,command=lambda: animalpelea(b_av))
b_av.place(x=1300, y=100)
BuhoP = cargarImg("buho.png", size=(80,120))
b_bu = Button(canvas, text="buho", image=BuhoP,command=lambda: animalpelea(b_bu))
b_bu.place(x=1100, y=250)
ZorroP = cargarImg("zorro.png", size=(80,120))
b_zo = Button(canvas, text="zorro", image=ZorroP,command=lambda: animalpelea(b_zo))
b_zo.place(x=1200, y=250)
OsoP = cargarImg("oso.png", size=(80,120))
b_os = Button(canvas, text="oso", image=OsoP,command=lambda: animalpelea(b_os))
b_os.place(x=1300, y=250)
TortugaP = cargarImg("tortuga.png", size=(80,120))
b_to = Button(canvas, text="tortuga", image=TortugaP,command=lambda: animalpelea(b_to))
b_to.place(x=1100, y=400)
PelicanoP = cargarImg("pelicano.png", size=(80,120))
b_pe = Button(canvas, text="pelicano", image=PelicanoP,command=lambda: animalpelea(b_pe))
b_pe.place(x=1200, y=400)
CangrejoP = cargarImg("cangrejo.png", size=(80,120))
b_can = Button(canvas, text="cangrejo", image=CangrejoP,command=lambda: animalpelea(b_can))
b_can.place(x=1300, y=400)
LeonP = cargarImg("leon.png", size=(80,120))
b_le = Button(canvas,text="leon", image=LeonP,command=lambda: animalpelea(b_le))
b_le.place(x=1100, y=550)
JirafaP = cargarImg("jirafa.png", size=(80,120))
b_ji = Button(canvas, text="jirafa", image=JirafaP,command=lambda: animalpelea(b_ji))
b_ji.place(x=1200, y=550)
CobraP = cargarImg("cobra.png", size=(80,120))
b_co = Button(canvas,text="cobra", image=CobraP, command=lambda: animalpelea(b_co))
b_co.place(x=1300, y=550)
LinceP = cargarImg("lince.png", size=(80,120))
b_li = Button(canvas, text="lince", image=LinceP, command=lambda: animalpelea(b_li))
b_li.place(x=1100, y=700)
YakP = cargarImg("yak.png", size=(80,120))
b_ya = Button(canvas, text="yak",image=YakP, command=lambda: animalpelea(b_ya))
b_ya.place(x=1200, y=700)
RenoP = cargarImg("reno.png", size=(80,120))
b_re = Button(canvas, text="reno", image=RenoP, command=lambda: animalpelea(b_re))
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
    desha_botones(botones, j + 1, animal)


Animales = []
def animalpelea(opciones):
    global Animales
    nombreA = b_nombres[opciones]
    Aanimal = dic_animales[nombreA]
    if Aanimal not in Animales:
        Animales.append(Aanimal)
    desha_animales(botones, 0, opciones)
    print(f"Animales = {nombres_animales(Animales)}")

def nombres_animales(lista, i=0):
    if i >= len(lista):
        return []
    return [lista[i].nombre] + nombres_animales(lista, i + 1)

# Información de los animales
class Animal:
    def __init__(self, nombre, vida, atq, defen, mundo):
        self.nombre = nombre
        self.vida = vida
        self.atq = atq
        self.defen = defen
        self.mundo = mundo

def info_animales(ruta):
    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo, delimiter=";")
    
        return list(map(
            lambda fila: Animal(
                nombre  = fila["nombre"],
                vida    = int(fila["vida"]),
                atq  = int(fila["atq"]),
                defen = int(fila["defen"]),
                mundo = fila["mundo"]
            ),
            lector
        ))

list_animales = info_animales("Infoanimales.csv")

def diccionario(lista, i=0):
    if i >= len(lista):
        return {}
    animal = lista[i]
    resto = diccionario(lista, i + 1)
    resto[animal.nombre] = animal
    return resto

dic_animales = diccionario(list_animales)
b_nombres = {
    b_ca: "camello", b_al: "alacran", b_av: "avestruz",
    b_bu: "buho",    b_zo: "zorro",   b_os: "oso",
    b_to: "tortuga", b_pe: "pelicano",b_can: "cangrejo",
    b_le: "leon",    b_ji: "jirafa",  b_co: "cobra",
    b_li: "lince",   b_ya: "yak",     b_re: "reno"}
# -----------------------------------------
# Pantalla del mapa 
# -----------------------------------------
list_desierto = None
Denemigo = None
MapaD = False
list_playa = None
Penemigo = None
MapaP = False
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
    #Nombre jugador
    L_nombre = Label(fjuego, text=f"Jugador:\n {nombre_jugador} ", font=('Times New Roman',16), fg='white', bg='#353a4e')
    L_nombre.place(x=50, y=550)
    
    #Personaje PENDIENTE REVISAR 
    global Personaje

    L_Personaje = Label(fjuego, image=Personaje, text="Personaje", font=('Times New Roman',18), bg="#000000", fg="white", borderwidth=15, justify='center')
    L_Personaje.place(x=50, y=600)
    #Titulo MAPA
    Label(fjuego, text="Mapa", font=('Times New Roman',18), bg="#000000", fg="white", borderwidth=15, justify='center').place(x=500, y=50)

    # -----------------------------------------
    #Primer mundo - DESIERTO 
    # -----------------------------------------
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

        #Random enemigo
        
        def enemigo_desierto():
            global list_desierto, Denemigo, MapaD
            if list_desierto is None:
                Eanimales = info_animales("Infoanimales.csv")
                list_desierto = list(filter(lambda a: a.mundo == "D", Eanimales))
            if len(list_desierto) == 0:
                MapaD = True
                desierto.destroy()
                Mundos.deiconify()
                BPlaya()
                return
            Denemigo = random.choice(list_desierto)
            list_desierto.remove(Denemigo)
            imgD_enemigo = cargarImg(f"{Denemigo.nombre}.png", size=(300, 350))
            fdesierto.imgD_enemigo = imgD_enemigo
            fdesierto.create_image(1000, 600, image=imgD_enemigo)
            fdesierto.create_text(140, 100, text=Denemigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="enemigo")
            fdesierto.create_text(140, 150, text=f"Vida: {Denemigo.vida}", font=("Times New Roman", 18, "bold"), fill="red", tags="enemigo")

        enemigo_desierto()

        #El animal para pelear escogido
        def animales_para_pelearD():
            global AmigoD
            print(f"Animales = {Animales}")
            if len(Animales) == 0:
                desierto.destroy()
                Mundos.deiconify()
                return None
            
            fdesierto.delete("amigo")
            fdesierto.delete("animal_img")
            AmigoD = Animales[0]
            imgAnimal = cargarImg(f"{AmigoD.nombre}.png", size=(330, 390))
            fdesierto.imgAnimal = imgAnimal
            fdesierto.create_image(200, 600, image=imgAnimal, tags="animal_img")
            fdesierto.create_text(140, 200, text=AmigoD.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="amigo")
            fdesierto.create_text(140, 250, text=f"Vida: {AmigoD.vida}", font=("Times New Roman", 18, "bold"), fill="white", tags="amigo")
            return AmigoD
        
        animales_para_pelearD()
        
        #PELEA DESIERTO
        def daño_amigo(amigo, enemigo):
            if len(Animales) == 0:
                return animales_para_pelearD()
            else: 
                if amigo.vida <= 0:
                    Animales.pop(0)
                    animales_para_pelearD()
                    return 
                else: 
                    daño = int(amigo.atq * (enemigo.defen / 100))
                    enemigo.vida = max(0, enemigo.vida - daño) 
                    fdesierto.delete("enemigo")
                    fdesierto.create_text(140, 100, text=Denemigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="enemigo")
                    fdesierto.create_text(140, 150, text=f"Vida: {Denemigo.vida}", font=("Times New Roman", 18, "bold"), fill="red", tags="enemigo")
                    fdesierto.after(500, lambda: enemigo_daño(Animales[0], Denemigo))
            
        def enemigo_daño(amigo, enemigo):
            if len(list_desierto)== 0:
                return enemigo_desierto()
            else: 
                if enemigo.vida <= 0:
                    enemigo_desierto()
                    return
                else: 
                    daño = int(enemigo.atq * (amigo.defen / 100))
                    amigo.vida = max(0, amigo.vida - daño)
                    fdesierto.delete("amigo")
                    fdesierto.create_text(140, 200, text=amigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="amigo")
                    fdesierto.create_text(140, 250, text=f"Vida: {amigo.vida}", font=("Times New Roman", 18, "bold"), fill="white", tags="amigo")
                    return
            
        Button(fdesierto, text="Atacar", command=lambda: daño_amigo(Animales[0], Denemigo)).place(x=1000, y=400)
    playdesert = cargarImg("DesiertoP.jpg", size=(350,190))
    Button(fjuego, text="desierto", image=playdesert, command=mapa_desierto).place(x=100, y=200)
    fjuego.playdesert = playdesert

    # -----------------------------------------
    #Segundo mundo - PLAYA 
    # -----------------------------------------

    def mapa_playa():
        Mundos.withdraw()

        playa = Toplevel()
        playa.title("Playa")
        playa.minsize(1500, 800)
        playa.resizable(width=NO, height=NO)

        fplaya = Canvas(playa, width=1500, height=800)
        fplaya.pack()

        fd_img2 = cargarImg("PlayaG.jpg", size=(1500,800))
        fplaya.create_image(0,0,anchor='nw', image=fd_img2) 
        fplaya.image = fd_img2
        def enemigo_playa():
            global list_playa, Penemigo, MapaP
            if list_playa is None:
                Eanimales = info_animales("Infoanimales.csv")
                list_desierto = list(filter(lambda a: a.mundo == "P", Eanimales))
            if len(list_desierto) == 0:
                MapaP = True
                playa.destroy()
                Mundos.deiconify()
     ###############################################################################
                return
            Penemigo = random.choice(list_playa)
            list_playa.remove(Penemigo)
            imgP_enemigo = cargarImg(f"{Penemigo.nombre}.png", size=(300, 350))
            fplaya.imgD_enemigo = imgP_enemigo
            fplaya.create_image(1000, 600, image=imgP_enemigo)
            fplaya.create_text(140, 100, text=Denemigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="enemigo")
            fplaya.create_text(140, 150, text=f"Vida: {Denemigo.vida}", font=("Times New Roman", 18, "bold"), fill="red", tags="enemigo")

        enemigo_playa()

        #El animal para pelear escogido
        def animales_para_pelearP():
            global AmigoP
            print(f"Animales = {Animales}")
            if len(Animales) == 0:
                playa.destroy()
                Mundos.deiconify()
                return None
            
            fplaya.delete("amigo")
            fplaya.delete("animal_img")
            AmigoP = Animales[0]
            imgAnimal = cargarImg(f"{AmigoP.nombre}.png", size=(330, 390))
            fplaya.imgAnimal = imgAnimal
            fplaya.create_image(200, 600, image=imgAnimal, tags="animal_img")
            fplaya.create_text(140, 200, text=AmigoP.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="amigo")
            fplaya.create_text(140, 250, text=f"Vida: {AmigoP.vida}", font=("Times New Roman", 18, "bold"), fill="white", tags="amigo")
            return AmigoP
        
        animales_para_pelearP()
        
        #PELEA DESIERTO
        def daño_amigo(amigo, enemigo):
            if len(Animales) == 0:
                return animales_para_pelearP()
            else: 
                if amigo.vida <= 0:
                    Animales.pop(0)
                    animales_para_pelearP()
                    return 
                else: 
                    daño = int(amigo.atq * (enemigo.defen / 100))
                    enemigo.vida = max(0, enemigo.vida - daño) 
                    fplaya.delete("enemigo")
                    fplaya.create_text(140, 100, text=Denemigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="enemigo")
                    fplaya.create_text(140, 150, text=f"Vida: {Denemigo.vida}", font=("Times New Roman", 18, "bold"), fill="red", tags="enemigo")
                    fplaya.after(500, lambda: enemigo_daño(Animales[0], Denemigo))
            
        def enemigo_daño(amigo, enemigo):
            if len(list_playa)== 0:
                return enemigo_playa()
            else: 
                if enemigo.vida <= 0:
                    enemigo_playa()
                    return
                else: 
                    daño = int(enemigo.atq * (amigo.defen / 100))
                    amigo.vida = max(0, amigo.vida - daño)
                    fplaya.delete("amigo")
                    fplaya.create_text(140, 200, text=amigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="amigo")
                    fplaya.create_text(140, 250, text=f"Vida: {amigo.vida}", font=("Times New Roman", 18, "bold"), fill="white", tags="amigo")
                    return

    #Botón playa
    def BPlaya():
        if MapaD == True:
            jugarplaya = cargarImg("PlayaP.jpg", size=(350,190))
            Button(fjuego, text="playa", image=jugarplaya, command=mapa_playa).place(x=400, y=500)
            fjuego.jugarplaya = jugarplaya
        else:
            print("falta completar el desierto")
        BPlaya()

    #Botón para devolverse 
    def atras():
        Mundos.destroy()
        canva.deiconify()
    Btn_atras = Button(fjuego, text="Atras", bg="#3e4d58",fg="white", font=('Times New Roman',16), command=atras)
    Btn_atras.place(x=100, y=60)

def empezar_juego():
    nombre2 = nombre1.get()
    ventanajuego(nombre2)

Button(canva, text="Jugar", fg="#000000", font=('Times New Roman',14), command=empezar_juego).place(x=280,y=140)


canva.mainloop()
