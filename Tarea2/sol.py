import os

from CC3501Utils import *

class Sol(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.radio=100
        super().__init__(pos,rgb)

    def figura(self):
        glBegin(GL_POLYGON)
        glColor3f(1, 1,0)
        i=0
        while (i<=2*pi):
            x=self.radio*cos(i)
            y=self.radio*sin(i)
            glVertex(x,y)
            i=i+0.05
        glEnd()