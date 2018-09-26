import os
from OpenGL.GL import *
from CC3501Utils import *

global gver,velx,vely
gver= Vector(0,-1)
velx=Vector(0,0)
vely=Vector(0,4)


class Pelota(Figura):
    def __init__(self, pos=Vector(0,0),rgb=(1.0, 1.0, 1.0)):
        self.radio=30
        super().__init__(pos,rgb)


    def figura(self):
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0,0)
        i=0.0
        while (i<2*pi):
            x=self.radio*cos(i)
            y=self.radio*sin(i)
            glVertex(x,y)
            i=i+0.1
        glColor3f(0, 0, 0)
        i = 0.0
        glEnd()
        glBegin(GL_POLYGON)
        while (i < (2*pi)):
            x = 20 * cos(i)
            y = 20 * sin(i)
            glVertex(x, y)
            i = i + 0.1
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1,1,1)
        i = 0.0
        while (i < (2*pi)):
            x = 10 * cos(i)
            y = 10 * sin(i)
            glVertex(x, y)
            i = i + 0.1
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1,1,0)
        i=0.0
        while (i < (2*pi)):
            x = 25*cos(3*pi/4)+10 * cos(i)
            y = 25*sin(3*pi/4)+10* sin(i)
            glVertex(x, y)
            i = i + 0.1
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(1,1,0)

        glVertex2f(25*cos(3*pi/4)-20,25*sin(3*pi/4)+10)
        glVertex2f(25*cos(3*pi/4)-20,25*sin(3*pi/4))
        glVertex2f(25*cos(3*pi/4),25*sin(3*pi/4))
        glVertex2f(25 * cos(3 * pi / 4), 25 * sin(3 * pi / 4) + 10)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 0)
        i = 0.0
        while (i < (2 * pi)):
            x = 25*cos(3*pi/4)-20 + 5 * cos(i)
            y = 25 * sin(3 * pi / 4) + 5 + 5 * sin(i)
            glVertex(x, y)
            i = i + 0.1
        glEnd()


    def mover(self,dt ):
            self.pos = sumar(self.pos, sumar(vely, ponderar(dt * dt / 2.0, gver)))

    def chocandotecho(self):
        return self.pos.y-self.radio<=0

    def chocandosuelo(self):
        return self.pos.y+self.radio>=600
