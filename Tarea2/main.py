import pygame
from random import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from CC3501Utils import *
from pelota import *
from vista import *
from fondo import *
from nube import *
from aro1 import *
from aro2 import *
from fases import *
from text import *
from sol import *
bestpuntaje=0

os.environ['SDL_VIDEO_CENTERED']='1'
def main() -> object:
    global bestpuntaje
    pygame.init()
    ancho = 1200
    alto = 600
    init(ancho, alto, "Flappy Dunk Chanta")
    fases=Fases()
    vista=Vista()
    text=Text()
    fondo = Fondo()
    sol=Sol(Vector(0,600))
    pelota=Pelota(Vector(150,300))
    nube1=Nube(Vector(100,randint(50,450)))
    nube2=Nube(Vector(600,randint(50,450)))
    nube3 =Nube(Vector(1100, randint(50, 450)))
    aro1=Aro1(Vector(400,randint(200,400)))
    aro2=Aro2(Vector(400,aro1.pos.y),aro1.a,aro1.b)
    aro12=Aro1(Vector(950,randint(200,400)))
    aro22=Aro2(Vector(950,aro12.pos.y),aro12.a,aro12.b)
    aro13=Aro1(Vector(1500,randint(200,400)))
    aro23=Aro2(Vector(1500,aro13.pos.y),aro13.a,aro13.b)
    pjs=[]
    pjs.append(fondo)
    pjs.append(sol)
    pjs.append(nube2)
    pjs.append(nube1)
    pjs.append(nube3)
    pjs.append(aro1)
    pjs.append(aro12)
    pjs.append(aro13)
    pjs.append(pelota)
    pjs.append(aro2)
    pjs.append(aro22)
    pjs.append(aro23)
    dt=0
    puntaje=0
    hecho=True
    esta=True
    empezar=False
    pygame.mixer.music.load("basket.mp3")
    bonus=2
    while not empezar:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                exit()
            if evento.type==KEYDOWN:
                if evento.key==K_q:
                    exit()
                if evento.key==K_SPACE:
                    empezar=True
                    pelota.mover(dt)

        vista.dibujar(pjs)
        pygame.display.flip()
    while (hecho):
        posicion=randint(100,450)
        nube1.mover()
        nube2.mover()
        nube3.mover()
        aro1.mover()
        aro2.mover()
        aro12.mover()
        aro22.mover()
        aro13.mover()
        aro23.mover()
        pelota.mover(dt)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                exit()
            if evento.type==KEYDOWN:
                if evento.key==K_q:
                    exit()
                if evento.key==K_SPACE:
                    dt=0
        if pelota.chocandosuelo() or pelota.chocandotecho():
            hecho=False
        if pelota.pos.x-(aro1.pos.x+aro1.a)>0:
            esta=True
        if pelota.pos.x - (aro12.pos.x + aro12.a) > 0:
            esta = True
        if pelota.pos.x - (aro13.pos.x + aro13.a) > 0:
            esta = True
        if -5<pelota.pos.x-(aro1.pos.x+aro1.a)<0 and esta:
            hecho=False
        if -5<pelota.pos.x - (aro12.pos.x + aro12.a) < 0 and esta:
            hecho = False
        if -5<pelota.pos.x - (aro13.pos.x + aro13.a) < 0 and esta:
            hecho = False
        if fases.pasolim(pelota.pos,aro1.pos,aro1.a,aro1.b) and esta:
            if posant-pelota.pos.y>0:
                puntaje=puntaje+bonus
                bonus=bonus+1
                esta=False
                pygame.mixer.music.play()
                print(str(puntaje))
                pjs[5]=None
                pjs[9]=None
            else:
                hecho=False

        if fases.pasolim(pelota.pos,aro12.pos,aro12.a,aro12.b) and esta:
            if posant-pelota.pos.y>0:
                puntaje=puntaje+bonus
                bonus=bonus+1
                esta=False
                pygame.mixer.music.play()
                print(str(puntaje))
                pjs[6]=None
                pjs[10]=None
            else:
                hecho=False

        if fases.pasolim(pelota.pos,aro13.pos,aro13.a,aro13.b) and esta:
            if posant-pelota.pos.y>0:
                puntaje=puntaje+bonus
                bonus=bonus+1
                esta=False
                pygame.mixer.music.play()
                print(str(puntaje))
                pjs[7]=None
                pjs[11]=None
            else:
                hecho=False

        if fases.pasotoc(pelota.pos,aro1.pos,aro1.a,aro1.b) and esta :
            if posant-pelota.pos.y>0:
                puntaje=puntaje+1
                esta=False
                print(str(puntaje))
                bonus=2
                pjs[5]=None
                pjs[9]=None
            else:
                hecho=False
        if fases.pasotoc(pelota.pos, aro12.pos, aro12.a,aro12.b) and esta:
            if posant-pelota.pos.y>0:
                puntaje=puntaje+1
                esta=False
                print(str(puntaje))
                bonus=2
                pjs[6]=None
                pjs[10]=None
            else:
                hecho=False
        if fases.pasotoc(pelota.pos, aro13.pos, aro13.a,aro13.b) and esta:
            if posant-pelota.pos.y>0:
                puntaje=puntaje+1
                esta=False
                print(str(puntaje))
                bonus=2
                pjs[7]=None
                pjs[11]=None
            else:
                hecho=False
        if aro1.cambiar():
            aro1 = Aro1(Vector(1350, posicion))
            aro2 = Aro2(aro1.pos,aro1.a,aro1.b)
            pjs[5]=aro1
            pjs[9]=aro2
        if aro12.cambiar():
            aro12 = Aro1(Vector(1350, posicion))
            aro22 = Aro2(aro12.pos,aro12.a,aro12.b)
            pjs[6]=aro12
            pjs[10]=aro22
        if aro13.cambiar():
            aro13 = Aro1(Vector(1350, posicion))
            aro23 = Aro2(aro13.pos,aro13.a,aro13.b)
            pjs[7]=aro13
            pjs[11]=aro23

        vista.dibujar(pjs)
        pygame.display.flip()
        posant=pelota.pos.y
        dt=dt+0.1
        pygame.time.wait(int(1000 / 80))
        while (not hecho):
            if bestpuntaje<puntaje:
                bestpuntaje=puntaje
            text.texto(puntaje,bestpuntaje)
            main()

main()
