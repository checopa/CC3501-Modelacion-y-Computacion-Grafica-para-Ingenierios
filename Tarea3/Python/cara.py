from CC3501Utils import *
import os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Cara:
    def __init__(self,pos=Vector(0,0,0)):
        self.pos = pos
        self.angulo=0
        self.lista=0
        self.crear()
    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        glEnable(GL_COLOR_MATERIAL)

        glBegin(GL_TRIANGLES)

        #cara externa
        color = [21,81,126] #azul no tan claro
        Ncolor = [color[0]/255.0,color[1]/255.0,color[2]/255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(250,40,Vector(0,0,0))
        #cara interna
        color = [19,54,99] #azul un poco mas oscuro
        Ncolor = [color[0]/255.0,color[1]/255.0,color[2]/255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(180,40.5,Vector(0,0,0))
        #Anillo
        color = [0,0,0] #azul un poco mas oscuro
        Ncolor = [color[0]/255.0,color[1]/255.0,color[2]/255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(110,2,Vector(0,0,40))
        color = [19,54,99] #azul un poco mas oscuro
        Ncolor = [color[0]/255.0,color[1]/255.0,color[2]/255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        cilindro(108,2.3,Vector(0,0,40))
        #circulos interiores
        for i in range(4):
            color = [21, 81, 126]  #azul no tan claro
            Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
            glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
            cilindro(20,2.5, Vector(109*cos(pi/4+(i*pi/2)),109*sin(pi/4+(i*pi/2)),40))
        #esferasexteriores
        for i in range(6):
            color = [19, 54, 99]  # azul un poco mas oscuro
            Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
            glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
            esfera(50, Vector(250*cos(pi/6+i*pi/3),250*sin(pi/6+i*pi/3),20))
        #esfera interior
        color = [21, 81, 126]  # azul no tan claro
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        esfera(35, Vector(0,0,40))
        #ojos
        color = [255, 255, 255]  # azul no tan claro
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        elipse(15, 30,3, Vector(109,0,40))
        elipse(15, 30, 3, Vector(-109, 0, 40))
        #pupila
        color = [0, 0, 0]  # azul no tan claro
        Ncolor = [color[0] / 255.0, color[1] / 255.0, color[2] / 255.0]
        glColor3f(Ncolor[0], Ncolor[1], Ncolor[2])
        elipse(7.5, 15, 3, Vector(109,0,40))
        elipse(7.5, 15, 3, Vector(-109, 0, 40))
        glEnd()
        glEndList()
    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.pos.x, self.pos.y, self.pos.z)
        glRotatef(self.angulo, 0, 0, 1)  # Rotacion en torno a eje Z
        glCallList(self.lista)
        glPopMatrix()