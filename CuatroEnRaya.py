# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 10:36:33 2015

@author: Jesús Sánchez de Castro 

Aplicación Cuatro en Raya
"""
from tkinter import *
import numpy
    
#Variables de jugadores
jugador1 = False
jugador2 = False
ganaJ1 = False
ganaJ2 = False
usados = 0
fin = False

#Para controlar que solo se comience el juego una vez.
juegoComenzado = False

#Matriz para controlar que jugadores han colocado en que posicion
matrix = numpy.zeros((4,4))

#Root global
root = Tk() #Ventana Raíz donde se dibuja todo
canvas = Canvas(root, width=400, height=400)#Inicialización del canvas
#Label global para poder cambiarla con eventos.
texto = StringVar()
texto.set("Estado del juego: No Iniciado.")
label = Label(root, textvariable=texto)


def comenzarPartida():

    global juegoComenzado
    global jugador1
    global jugador2
    global texto
    global canvas
    global matrix
    global fin
    global usados
    
    if juegoComenzado == False:
        jugador1 = True

    #Reiniciamos la partida
    elif juegoComenzado == True:
        
        jugador1 = True
        jugador2 = False
        canvas.delete("all")
        #Canvas donde se dibuja todo
        canvas.create_line(0,100,400,100) #Lineas que dibujan el tablero 4x4
        canvas.create_line(0,200,400,200)
        canvas.create_line(0,300,400,300)
        canvas.create_line(0,400,400,400)
        canvas.create_line(100,0,100,400)
        canvas.create_line(200,0,200,400)
        canvas.create_line(300,0,300,400)
        canvas.create_line(400,0,400,400)
        matrix = numpy.zeros((4,4)) 
        fin = False
        usados=0
        
    texto.set("Estado del juego: Turno jugador 1.")
    juegoComenzado = True

def getGanador():
    #Para un jugador dado comprobar todas las
    global matrix
    ganador = -1

    
    for i in range(0,4):
        suma = 0
        for j in range(0,4):
            
            if matrix[i,j]== 0:
                suma+= -8
            
            else:
                suma += matrix[i,j]
    
                
        if suma == 4:
            return 1
        elif suma == 8:
            return 2
    
    for j in range(0,4):
        suma = 0
        for i in range(0,4):
            
            if matrix[i,j]== 0:
                suma+= -8
            else:
                suma += matrix[i,j]  
                
        if suma == 4:
            return 1
        elif suma == 8:
            return 2

    if(matrix[0,0] == matrix[1,1] == matrix[2,2] == matrix[3,3]==1):
        return 1
    elif(matrix[0,0] == matrix[1,1] == matrix[2,2] == matrix[3,3]==2):
        return 2
    elif(matrix[0,3] == matrix[1,2] == matrix[2,1] == matrix[3,0]==1):
        return 1
    elif(matrix[0,3] == matrix[1,2] == matrix[2,1] == matrix[3,0]==2):
        return 2

         
def getPos(event):
    
    #Variables globales para controlar el jugador actual
    global jugador1
    global jugador2
    global ganaJ1
    global ganaJ2
    global texto
    global usados
    global fin
    
    if jugador1!=False or jugador2!=False:
        #Coordenadas del canvas por pantalla
        #print("Coor:(",event.x,",",event.y,")")
        canvas = event.widget
        
   
        
    #Función para dibujar CRUZ o CIRCULO en función del jugador actual.
    #Se va moviendo en función del tamaño de los cuadrados dibujados en el canvas
    #para saber en que casilla estamos y dibujar correctamente dentro de dicha
    #casilla.
    for i in range(0,400,100):
        for j in range(0,400,100):
            if event.x < i+100 and event.y < j+100 and event.x > i and event.y > j:
                if jugador1:
                    #Comprobar que no hay nada pintado antes de pintar                    
                    tupla = canvas.find_enclosed(i,j,i+100,j+100)
                    if len(tupla)==0:
                        #Circulo
                        if(fin==False):
                            canvas.create_oval(i+25,j+25,i+75,j+75,width=4,outline="#8258FA")#Púrpura
                            jugador1 = False
                            jugador2 = True
                            texto.set("Estado del juego: Turno jugador 2.")
                            #Rellenamos la matrix para comprobar la victoria
                            matrix[i//100,j//100]=1
                            usados+=1
                    
                elif jugador2:

                    #Comprobar que no hay nada pintado antes de pintar                    
                    tupla = canvas.find_enclosed(i,j,i+100,j+100) 
                    if len(tupla) == 0:
                        if(fin==False):
                            #Cruz creada con 2 lineas
                            canvas.create_line(i+30,j+30,i+70,j+70,width=4,fill="#58ACFA")#Azul
                            canvas.create_line(i+30,j+70,i+70,j+30,width=4,fill="#58ACFA")
                            jugador2 = False
                            jugador1 = True
                            texto.set("Estado del juego: Turno jugador 1.")
                            #Rellenamos la matrix para comprobar la victoria
                            matrix[i//100,j//100]=2
                            usados+=1
    
    print(matrix)
    if getGanador()==1:
        texto.set("¡Gana el jugador 1!")
        ganaJ1 = False
        fin = True
    elif getGanador()==2:
        texto.set("¡Gana el jugador 2!")
        ganaJ2 = False
        fin = True
    elif usados==16:
        texto.set("¡EMPATE!")
        fin = True
        
def main():
    global root
   
    root.title("Cuatro en Raya") #Título de la ventana
    root.geometry("400x530") #Tamaño de la ventana
    root.resizable(width=FALSE, height=FALSE) #Tamaño de la ventana fijo
    
    #Canvas donde se dibuja todo
    canvas.create_line(0,100,400,100) #Lineas que dibujan el tablero 4x4
    canvas.create_line(0,200,400,200)
    canvas.create_line(0,300,400,300)
    canvas.create_line(0,400,400,400)
    canvas.create_line(100,0,100,400)
    canvas.create_line(200,0,200,400)
    canvas.create_line(300,0,300,400)
    canvas.create_line(400,0,400,400)
    #Todos los elementos de la ventana han de estar en una posición del grid
    canvas.grid(row=0, column=0)  
    canvas.bind("<ButtonPress-1>",getPos)#Eventos para pulsar en las casillas
    #Label de estado del juego
    
    label.grid(row=1, column=0)    
    label.config(height=3,width=55)
    label.config(bg="#58ACFA")#Azul
    
    #Boton de jugar
    boton = Button(root,text="Click aquí para comenzar la partida", command=comenzarPartida)
    boton.grid(row=2, column=0)
    boton.config(height=4,width=55)
    boton.config(bg="#8258FA")#Púrpura

    #Se mete el programa en un loop que espera eventos programados anteriormente.
    root.mainloop()
    
    
main()
