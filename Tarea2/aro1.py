import os
from OpenGL.GL import *
from CC3501Utils import *
from random import *

global velx
velx=Vector(-2,0)

class Aro1(Figura):
    def __init__(self,pos=Vector(0,0),rgb=(1.0,1.0,1.0)):
        self.a=randint(50,100)
        self.b=randint(20,40)
        self.c=False
        super().__init__(pos,rgb)

    def figura(self):

        glPointSize(5)
        glBegin(GL_POINTS)
        glColor3f(0, 0, 1)
        i=0.0
        while (i<pi):
            x=self.a*cos(i)
            y=self.b*sin(i)
            glVertex2f(x,y)
            i=i+0.001
        glEnd()

    def mover(self):
        self.pos = sumar(self.pos, ponderar(2, velx))
        if self.pos.x < -300:
            self.c = True

    def cambiar(self):
        if self.c == True:
            return True





