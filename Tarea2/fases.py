from CC3501Utils import *

class Fases:
    def pasotoc(self,pospe=Vector(0,0),posar=Vector(0,0),anchoar=0,altoar=0):
        if posar.x-anchoar<pospe.x<posar.x+anchoar and posar.y-altoar<pospe.y<posar.y:
            return True
    def pasolim(self,pospe=Vector(0,0),posar=Vector(0,0),anchoar=0,altoar=0):
        if posar.x-anchoar<pospe.x-30 and pospe.x+30<posar.x+anchoar and posar.y-altoar<pospe.y<posar.y:
            return True