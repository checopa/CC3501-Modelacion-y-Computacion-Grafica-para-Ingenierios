from OpenGL.GL import *
from CC3501Utils import *

class Vista:
    def dibujar(self, pjs):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for p in pjs:
            if p!=None:
                p.dibujar()