from initializers import *
from Eje import *
from CC3501Utils import *

import os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import uniform
from cara import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

def main():
    # inicializar
    ancho = 800
    alto = 600
    init(ancho, alto, "Bronzor version fruna")

    # crear objetos
    clock = pygame.time.Clock()

    # camara
    camPos = Vector(400, 400, 1000) 	#posicion de la camara
    camAt = Vector(0, 0, -1000)	#posicion que se enfoca

    # luz
    light = GL_LIGHT0
    l_position = Vector(1000.0, 100.0, 500.0)

    # crear una luz coherente con su color base
    l_diffuse = [1.0, 1.0, 1.0, 1.0]
    l_ambient = [0.2, 0.2, 0.2, 1]
    l_specular = [1.0, 1.0, 1.0, 1.0]

    # otros valores estandar
    l_constant_attenuation = 1.5
    l_linear_attenuation = 0.5
    l_quadratic_attenuation = 0.2

    l_spot_cutoff = 60.0
    l_spot_direction = Vector(-1.0, -1.0, 0.0)  # direccion de rebote de luz
    l_spot_exponent = 2.0


    cara=Cara(Vector(400,400,0))
    eje = Eje(400.0)  # R,G,B = X,Y,Z

    # variables de tiempo
    fps = 30
    dt = 1.0 / fps

    run = True
    while run:
        # manejo de eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # obtener teclas presionadas
        pressed = pygame.key.get_pressed()

        if pressed[K_UP]:
            camPos = sumar(ponderar(10,normalizar(camAt)), camPos)
        if pressed[K_DOWN]:
            camPos = sumar(ponderar(-10,normalizar(camAt)), camPos)
        if pressed[K_RIGHT]:
            camPos = sumar(ponderar(-10,rotarFi(normalizar(camAt),90)), camPos)
        if pressed[K_LEFT]:
            camPos = sumar(ponderar(10,rotarFi(normalizar(camAt),90)), camPos)

        if pressed[K_w] :
            camAt = sumar(Vector(0, 0, 1000), camAt)
        if pressed[K_s]:
            camAt = sumar(Vector(0, 0, -1000), camAt)
        if pressed[K_d]:
            camAt = rotarFi(camAt,-0.08)
        if pressed[K_a]:
            camAt = rotarFi(camAt, 0.08)

        if pressed[K_r]:
            l_position = Vector(uniform(0, 1000), uniform(0, 1000), uniform(0, 1000))

        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # dibujar objetos
        cara.dibujar()
        eje.dibujar()

        # camara
        glLoadIdentity()
        gluLookAt(camPos.x, camPos.y, camPos.z,  # posicion
                  camAt.x, camAt.y, camAt.z,  # mirando hacia
                  0.0, 0.0, 1.0)  # inclinacion

        # luz
        glLightfv(light, GL_POSITION, l_position.cartesianas())
        glLightfv(light, GL_AMBIENT, l_ambient)
        glLightfv(light, GL_SPECULAR, l_specular)
        glLightfv(light, GL_DIFFUSE, l_diffuse)
        glLightf(light, GL_CONSTANT_ATTENUATION, l_constant_attenuation)
        glLightf(light, GL_LINEAR_ATTENUATION, l_linear_attenuation)
        glLightf(light, GL_QUADRATIC_ATTENUATION, l_quadratic_attenuation)
        glLightf(light, GL_SPOT_CUTOFF, l_spot_cutoff)
        glLightfv(light, GL_SPOT_DIRECTION, l_spot_direction.cartesianas())
        glLightf(light, GL_SPOT_EXPONENT, l_spot_exponent)

        glEnable(light)

        pygame.display.flip()  # cambiar imagen
        clock.tick(fps)  # esperar 1/fps segundos

    pygame.quit()
    return


main()
