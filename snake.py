import turtle
import time
import random
import pygame
from PIL import Image




pygame.init()





posponer = 0.1

#importando sonido

sonidoLosser = pygame.mixer.Sound("over.mp3")
sonidoComida = pygame.mixer.Sound('comiendo.mp3')


#Marcador
puntuacion = 0
MaxPuntuacion = 0

#Configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego Snake V1.9")
wn.bgcolor("black")  #averiguar cambiar color por uan foto 
wn.setup(width = 600, height = 600)
wn.tracer(0)


#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("YellowGreen")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("red")
comida.penup()
comida.goto(0,100)


#Segmentos
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("red")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("marcador: 0     record: 0",  align = "center", font =("Courier", 24, "normal"))

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")



while True:
    wn.update()

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        sonidoLosser.play() 
        
        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
            
        #Limpiar lista de segmentos
            sonidoLosser.play()

            segmento.clear()
            
        #Resetear marcador
        puntuacion = 0
        texto.clear()   
        texto.write("marcador: {}     record: {}".format(puntuacion, MaxPuntuacion), 
                align = "center", font =("Courier", 24, "normal"))

    #Colisiones comida
    if cabeza.distance(comida) < 20: 
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("OliveDrab")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        sonidoComida.play()
        #Aumentar marcador 
        puntuacion += 1
         
        if puntuacion > MaxPuntuacion: 
           MaxPuntuacion = puntuacion 

        texto.clear()   
        texto.write("marcador: {}    record: {}".format(puntuacion, MaxPuntuacion), 
                align = "center", font =("Courier", 24, "normal"))
    
    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
            sonidoLosser.play()   
            segmentos.clear()
            
            puntuacion = 0
            texto.clear()   
            texto.write("marcador: {}    record: {}".format(puntuacion, MaxPuntuacion), 
                align = "center", font =("Courier", 24, "normal"))
            
    time.sleep(posponer)