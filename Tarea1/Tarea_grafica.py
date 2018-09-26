# coding=utf-8

# Importar librería
import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.multiarray import ndarray

class Temperaturas:
    def __init__(self,hora,valorrho):
        #Define el valor de tolerancia
        #Crea una matriz de zeros sobre la cual se trabajara
        #Define valor de R
        #Se define hasta donde llega el mar, que es la base para todo

        
        self._tol=0.1
        self._valorrho=valorrho
        self._hora=hora
        self._matrix=np.zeros((101,200))
        self._R=0.184
        self._mar = int(60 + (20 * self._R))


    def _creamar(self):
            #Asigna la temperatura al mar dependiendo de la hora

            for i in range(100, 101):
                for j in range(self._mar):
                    if 0<=self._hora<8:
                        self._matrix[i][j] = 4
                    if 8<=self._hora<16:
                        self._matrix[i][j]=4+(self._hora-8)*2
                    if 16<=self._hora<=24:
                        self._matrix[i][j]=20-(self._hora-16)*2
    def _creaplanta(self):
        #Asigna la temperatura a la planta que llega hasta 120m mas alla del mar

        for i in range(100,101):
            for j in range(0,6):
                self._matrix[i][j+self._mar]=450*((math.cos((math.pi)*self._hora/12))+2)

    def _geografia(self):
        #Se crea la geografia en general, incluyendo el mar, la planta y las montañas
        #Las montañas se crean con valores de -100 para evitar problemas ocurridos con Nan

        self._creamar()
        self._creaplanta()
        planta=(self._mar)+6
        for j in range(0, 14):
            for i in range(int(100-(j/3)),101):
                self._matrix[i][planta+j]=-100
        #donde termina la inclinacion en el eje x
        inclinacionx=planta+14
        #altura de la inclinacion
        inclinaciony=int(100-(14/3))
        #altura de la primera cima
        cima1 =int(100-(75+(10*self._R)))
        #pendiente entre la inclinacion y la cima
        pendiente1=1.8
        for j in range(40):
            for i in range(int(inclinaciony - (j*pendiente1)), 101):
                self._matrix[i][j+inclinacionx]=-100
        #altura de la segunda cima
        cima2=int(100-(65+(10*self._R)))
        #donde se encuentra la primera cima en el eje x
        cima1x=self._mar+60
        #pendiente entre la primera cima y la segunda cima
        pendiente2=-2.0/3.0
        for j in range (0,15):
             for i in range(int(cima1-(j*pendiente2)),101):
                  self._matrix[i][j + cima1x]=-100
        #altura de la tercera cima
        cima3=int(100-(92.5+5*self._R))
        #donde se enceuntra la seguna cima en el eje x
        cima2x=self._mar+75
        #pendiente entre la segunda y tercera cima
        pendiente3=(cima2-cima3)/25
        for j in range(0,25):
            for i in range(int(cima2-(j*pendiente3)),101):
                self._matrix[i][j+cima2x]=-100
        #altura de la tercera cima
        cima3y=cima2-25*pendiente3
        #donde llega la tercera cima en el eje x
        cima3x=self._mar+100
        #pendiente para la ultima parte de la montaña
        pendiente4=-1
        for j in range (0,200-cima3x):
            for i in range(int(cima3y-(j*pendiente4)),101):
                self._matrix[i][cima3x+j]=-100
        self._atmosfera()

    def _rho(self,x,y):
        plantax=self._mar+3
        plantay=100
        X=abs(x-plantax)*20
        Y=abs(y-plantay)*20
        if self._valorrho==0:
            return 0
        else:
            return 400/((X**2+Y**2+120)**(0.5))



    def _atmosfera(self):
        #se asigna la temepratura inicial a la atmosfera dependiendo de la hora

        for i in range(100):
            for j in range (200):
                if 0<=self._hora<8 and self._matrix[i][j]==0:
                    self._matrix[i][j] = -8 + 0.12*i
                if 8<=self._hora<16 and self._matrix[i][j]==0:
                    self._matrix[i][j]=(4+(self._hora-8)*2)-12 + 0.12*i
                if 16<=self._hora<=24 and self._matrix[i][j]==0:
                    self._matrix[i][j]=(20-(self._hora-16)*2)-12 + 0.12*i

    def _omega(self):
        #valor para el omega optimo
        return 4 / (2 + (math.sqrt(4 - (math.cos(math.pi / (101 - 1)) + math.cos(math.pi / (200 - 1))) ** 2))) -1


    def _interacion(self,mat_new,mat_old):
        # type: () -> object
        #para los distintos valores de omega se modifica manualmente
        #w = self._omega() - 1
        w=0.9
        for i in range(100):
                for j in range(199):

                    #General
                    if 0<i<100 and 0<j<199:
                        if mat_old[i][j]!=-100:

                            if mat_old[i+1][j]!=-100 and mat_old[i-1][j]!=-100 and mat_old[i][j-1]!=-100 and mat_old[i][j+1]!=-100:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(mat_old[i+1][j]+mat_old[i-1][j]+mat_old[i][j-1]+mat_old[i][j+1]-4*mat_old[i][j]-self._rho(j,i))
                            if mat_old[i+1][j]==-100 and mat_old[i][j-1]==-100 and mat_old[i][j+1]==-100 and i<=10:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(0+mat_old[i-1][j]+0+0-4*mat_old[i][j]-self._rho(i,j))
                            if mat_old[i+1][j]==-100 and mat_old[i][j-1]==-100 and mat_old[i][j+1]==-100 and i>10:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(20+mat_old[i-1][j]+20+20-4*mat_old[i][j]-self._rho(i,j))
                            if mat_old[i+1][j]==-100 and mat_old[i][j+1]==-100 and i<=10:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(0+mat_old[i-1][j]+mat_old[i][j-1]+0-4*mat_old[i][j]-self._rho(i,j))
                            if mat_old[i+1][j]==-100 and mat_old[i][j+1]==-100 and i>10:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(20+mat_old[i-1][j]+mat_old[i][j-1]+20-4*mat_old[i][j]-self._rho(i,j))
                            if mat_old[i+1][j]==-100 and mat_old[i][j-1]==-100 and i<=10:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(0+mat_old[i-1][j]+mat_old[i][j+1]+0-4*mat_old[i][j]-self._rho(i,j))
                            if mat_old[i+1][j]==-100 and mat_old[i][j-1]==-100 and i>10:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(20+mat_old[i-1][j]+mat_old[i][j+1]+20-4*mat_old[i][j]-self._rho(i,j))
                            if mat_old[i + 1][j] == 20 and i <= 10:
                                mat_new[i][j]=mat_old[i][j] + 0.25 * w * (0 + mat_old[i - 1][j] + mat_old[i][j - 1] + mat_old[i][j + 1] - 4 *mat_old[i][j] - self._rho(i, j))
                            if mat_old[i + 1][j] == 20 and i > 10:
                                mat_new[i][j]=mat_old[i][j] + 0.25 * w * (20 + mat_old[i - 1][j] + mat_old[i][j - 1] + mat_old[i][j + 1] - 4 * mat_old[i][j] - self._rho(i, j))
                    #Borde Superior
                    if i==0 and 0<j:
                        mat_new[i][j] = mat_old[i][j] + 0.25*w*(2*mat_old[i + 1][j]+mat_old[i][j-1]+mat_old[i][j+1]-4*mat_old[i][j] - self._rho(j, i))
                    #Borde Izquierdo
                    if j==0 and 0<i<100:
                        mat_new[i][j] = mat_old[i][j] + 0.25 * w * (mat_old[i + 1][j] + mat_old[i - 1][j] + 2*mat_old[i][j + 1] - 4 *mat_old[i][j] - self._rho(j, i))
                    #Esquina superior izquierda
                    if i==0 and j==0:
                        mat_new[i][j] = mat_old[i][j] + 0.25 * w * (2*mat_old[i + 1][j]+ 2*mat_old[i][j + 1] - 4 *mat_old[i][j] - self._rho(j, i))
                    #Esquina superior derecha
                    if i==0 and j==199:
                        mat_new[i][j] = mat_old[i][j] + 0.25 * w * (2*mat_old[i + 1][j]+ 2*mat_old[i][j - 1] - 4 *mat_old[i][j] - self._rho(j, i))
                    #Borde derecho
                    if j==199 and 0<i<100:
                        if mat_old!=-100:
                            if mat_old[i+1][j]==-100 and mat_old[i][j-1]==-100:
                                mat_new[i][j] = mat_old[i][j] + 0.25*w*(20 + mat_old[i - 1][j] + 2*20 - 4 * mat_old[i][j] - self._rho(j, i))
                            if mat_old[i+1][j]==-100:
                                mat_new[i][j]=mat_old[i][j]+0.25*w*(20 + mat_old[i - 1][j] + 2*mat_old[i][j - 1]- 4 * mat_old[i][j] - self._rho(j, i))
                            else:
                                mat_new[i][j] = mat_old[i][j]+0.25*w*(mat_old[i + 1][j] + mat_old[i - 1][j] + 2*mat_old[i][j - 1]- 4 * mat_old[i][j] - self._rho(j, i))




    def _convergio(self,mat_old, mat_new, tol):
        not_zero = (mat_new != 0)
        diff_relativa = (mat_old - mat_new)[not_zero]
        max_diff = np.max(np.fabs(diff_relativa))
        return [max_diff < tol, max_diff]

    def start(self):
        #itera sobre la matriz hasta que esta converge e imprime el numero de veces que recorrio toda la matriz

        mat_new=np.copy(self._matrix)
        #it=0
        #run = True
        #converg=[]
        #while run:
        for i in range(1000):
            mat_old= np.copy(mat_new)
            self._interacion(mat_new,mat_old)
            #converg = self._convergio(mat_old, mat_new, self._tol)
            #run = not converg[0]
            #it=it+1
        self._matrix=np.copy(mat_old)
        #print (it)

    def grafico(self):
        #Grafica una matriz

        extnt = [0, 4000, 0, 2000];
        plt.imshow(self._matrix,extent=extnt)
        plt.colorbar()
        plt.show()

t=Temperaturas(16,1)
t._geografia()
t.start()
t.grafico()
