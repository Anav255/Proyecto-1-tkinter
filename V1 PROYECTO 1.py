from tkinter import *
from PIL import Image, ImageTk
import os
import random
import csv
from tkinter import messagebox
import threading
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
b_1 = Button(canvas, image=Personaje1, command=lambda: personajepelea(b_1, Personaje1))
b_1.place(x=100, y=300)
Personaje2 = cargarImg("personaje2.png", size=(130,300))
b_2 = Button(canvas, image=Personaje2, command=lambda: personajepelea(b_2, Personaje2))
b_2.place(x=250, y=300)
Personaje3 = cargarImg("personaje3.png", size=(130,300))
b_3= Button(canvas, image=Personaje3, command=lambda: personajepelea(b_3, Personaje3))
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

Personaje = None
def personajepelea(opciones, imagen):
    global Personaje
    Personaje = imagen
    desha_personajes(personajes, 0, opciones)
#Animales 
Label(canvas, text="Seleccione 1 animal por columna", font=('Times New Roman',14), 
      bg="#77b67c", fg='black').place(x=1120,y=50)

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
    if len(Animales) < 3 and Aanimal not in Animales:
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

def crear_animal(fila):
    animal = Animal(
        nombre = fila["nombre"],
        vida   = int(fila["vida"]),
        atq    = int(fila["atq"]),
        defen  = int(fila["defen"]),
        mundo  = fila["mundo"]
    )
    animal.vida_max = animal.vida
    return animal
def info_animales(ruta):
    with open(ruta, "r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo, delimiter=";")
        return list(map(crear_animal, lector))
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

#listas de mundos        
mundos = [
    {"nombre": "desierto","codigo": "D", "completado": False},
    {"nombre": "playa","codigo": "P", "completado": False},
    {"nombre": "sabana", "codigo": "S", "completado": False},
    {"nombre": "bosque", "codigo": "B", "completado": False},
    {"nombre": "montaña", "codigo": "M", "completado": False},
]
# -----------------------------------------
# Pantalla del mapa 
# -----------------------------------------
capturados = []
proximos = []
list_enemigos = None
Denemigo = None
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
    
    #Imagen personaje 
    global Personaje
    L_Personaje = Label(fjuego, image=Personaje, text="Personaje", font=('Times New Roman',18), bg="#000000", fg="white", borderwidth=15, justify='center')
    L_Personaje.place(x=50, y=600)
    L_Personaje.image = Personaje

    #Titulo MAPA
    Label(fjuego, text="Mapa", font=('Times New Roman',18), bg="#000000", fg="white", borderwidth=15, justify='left').place(x=700, y=50)

    # -----------------------------------------
    #MUNDOS
    # -----------------------------------------
    b_mundos = []

    def CbMundos(mundos, i):
        if i >= len(mundos):
            return
        b = Button(fjuego, text=f"Mundo {i+1}", state="disabled", command=lambda i=i: mapa(mundos[i]))
        b.pack()
        b_mundos.append(b)
        CbMundos(mundos, i + 1)

    def desbloquearM(lista, i, mundo_actual):
        if i >= len(lista):
            return
        if lista[i] == mundo_actual:
            if i + 1 < len(lista) and i + 1 < len(b_mundos):
                b_mundos[i + 1].config(state="normal")
            return
        desbloquearM(lista, i + 1, mundo_actual)

    def Cmundo(mundo):
        mundo["completado"] = True
        Cmundo(mundos[0])
        desbloquearM(mundos, 0, mundo)
        
    def mapa(mundo):
        if mundo["completado"]:
            return
        global Denemigo, AmigoD, list_enemigos
        list_enemigos = None
        Mundos.withdraw()

        ventana = Toplevel()
        ventana.title(mundo["nombre"])
        ventana.minsize(1500, 800)
        ventana.resizable(width=NO, height=NO)

        fondo = Canvas(ventana, width=1500, height=800)
        fondo.pack()

        fd_img = cargarImg(f"{mundo['nombre']}G.jpg", size=(1500,800))
        fondo.create_image(0,0,anchor='nw', image=fd_img) 
        fondo.image = fd_img

        def Cl_animal(enemigo):
            clonar = type(enemigo)(
            enemigo.nombre,
            enemigo.vida_max,
            enemigo.atq,
            enemigo.defen,
            enemigo.mundo)
            clonar.vida_max = enemigo.vida_max
            return clonar
        
        #Random enemigo
        
        def enemigo_P(mundo):
            global Denemigo, list_enemigos, capturados
            if list_enemigos is None:
                Eanimales = info_animales("Infoanimales.csv")
                list_enemigos = list(filter(lambda a: a is not None and a.mundo == mundo["codigo"] and a.nombre not in capturados, Eanimales))
            if not list_enemigos:
                mundo["completado"] = True
                Animales.extend(proximos)
                proximos.clear()
                i = mundos.index(mundo)
                if i < len(b_mundos):
                    b_mundos[i].config(state="disabled")
                ventana.destroy()
                Mundos.deiconify()
                desbloquearM(mundos, 0, mundo)
                BPlaya()
                BSabana()
                Bbosque()
                Bmontaña()
                return
            
            enemigo_base = random.choice(list_enemigos)
            list_enemigos.remove(enemigo_base)
            Denemigo = Cl_animal(enemigo_base)
            imgD_enemigo = cargarImg(f"{Denemigo.nombre}.png", size=(300, 350))
            fondo.imgD_enemigo = imgD_enemigo
            fondo.create_image(1000, 600, image=imgD_enemigo)
            fondo.create_text(140, 100, text=Denemigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="enemigo")
            fondo.create_text(140, 150, text=f"Vida: {Denemigo.vida}", font=("Times New Roman", 18, "bold"), fill="red", tags="enemigo")

        enemigo_P(mundo)

        #El animal para pelear escogido
        def amigo_P():
            global AmigoD
            if len(Animales) == 0:
                ventana.destroy()
                Mundos.deiconify()
                return None
            fondo.delete("amigo")
            fondo.delete("animal_img")
            AmigoD = Animales[0]
            imgAnimal = cargarImg(f"{AmigoD.nombre}.png", size=(330, 390))
            fondo.imgAnimal = imgAnimal
            fondo.create_image(200, 600, image=imgAnimal, tags="animal_img")
            fondo.create_text(140, 200, text=AmigoD.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="amigo")
            fondo.create_text(140, 250, text=f"Vida: {AmigoD.vida}", font=("Times New Roman", 18, "bold"), fill="white", tags="amigo")
        amigo_P()
        
        #PELEA
        def daño_amigo(amigo, enemigo):
            if len(Animales) == 0:
                return amigo_P()
            if amigo.vida <= 0:
                Animales.pop(0)
                amigo_P()
                return 
            else: 
                daño = int(amigo.atq * (enemigo.defen / 10))
                enemigo.vida = max(0, enemigo.vida - daño) 
                fondo.delete("enemigo")
                fondo.create_text(140, 100, text=Denemigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="enemigo")
                fondo.create_text(140, 150, text=f"Vida: {Denemigo.vida}", font=("Times New Roman", 18, "bold"), fill="red", tags="enemigo")
                fondo.after(500, lambda: enemigo_daño(Animales[0], Denemigo, mundos[0]))
            
        def enemigo_daño(amigo, enemigo, mundo):
            global capturados
            if enemigo.vida <= 0:
                proximos.append(Cl_animal(Denemigo))
                capturados.append(Denemigo.nombre)
                enemigo_P(mundo)
                return
            else: 
                daño = int(enemigo.atq * (amigo.defen / 10))
                amigo.vida = max(0, amigo.vida - daño)
                fondo.delete("amigo")
                fondo.create_text(140, 200, text=amigo.nombre, font=("Times New Roman", 20, "bold"), fill="white", tags="amigo")
                fondo.create_text(140, 250, text=f"Vida: {amigo.vida}", font=("Times New Roman", 18, "bold"), fill="white", tags="amigo")
                return      
        Button(fondo, text="Atacar", command=lambda: daño_amigo(Animales[0], Denemigo)).place(x=1000, y=400)
    #Boton desierto
    
    playdesert = cargarImg("DesiertoP.jpg", size=(350,190))
    Button(fjuego, text="desierto", image=playdesert, command=lambda: mapa(mundos[0])).place(x=100, y=200)
    fjuego.playdesert = playdesert
    #Boton playa
    def BPlaya():
        global mundos
        if mundos[0]["completado"]:
            jugarplaya = cargarImg("PlayaP.jpg", size=(350,190))
            Button(fjuego, text="playa", image=jugarplaya, command=lambda: mapa(mundos[1])).place(x=300, y=500)
            fjuego.jugarplaya = jugarplaya
        else:
            print("falta completar el desierto")
    BPlaya()
    #Boton sabana
    def BSabana():
        global mundos
        if mundos[1]["completado"]:
            jugarsabana = cargarImg("SabanaP.jpg", size=(350,190))
            Button(fjuego, text="sabana", image=jugarsabana, command=lambda: mapa(mundos[2])).place(x=550, y=200)
            fjuego.jugarsabana = jugarsabana
        else:
            print("falta completar la playa")
    BSabana()
    #Boton bosque
    def Bbosque():
        global mundos
        if mundos[2]["completado"]:
            jugarbosque = cargarImg("BosqueP.jpg", size=(350,190))
            Button(fjuego, text="sabana", image=jugarbosque, command=lambda: mapa(mundos[3])).place(x=700, y=500)
            fjuego.jugarbosque = jugarbosque
        else:
            print("falta completar la sabana")
    Bbosque()
    #Boton montaña
    def Bmontaña():
        global mundos
        if mundos[3]["completado"]:
            jugarbosque = cargarImg("MontañaP.jpg", size=(350,190))
            Button(fjuego, text="sabana", image=jugarbosque, command=lambda: mapa(mundos[4])).place(x=1000, y=200)
            fjuego.jugarbosque = jugarbosque
        else:
            print("falta completar el bosque")
    Bmontaña()
    #Mensaje final
    def reiniciar_juego():
        threading.Thread(target=resultado).start()

    def resultado():
        global mundos, Animales
        if mundos[5]["completado"]:
            messagebox.showinfo("Has ganado el juego", "Felicidades")
            yesno = messagebox.askyesno("Confirmar", "¿Jugar de nuevo?")
            if yesno:
                reiniciar_juego()
            else:
                Mundos.quit()
        if len(Animales) == 0:
            messagebox.showinfo("Perdiste", "tu personaje murió")
            yesno = messagebox.askyesno("Confirmar", "¿Jugar de nuevo?")
            if yesno:
                reiniciar_juego()
            else:
                Mundos.quit()
    threading.Thread(target=resultado).start()
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