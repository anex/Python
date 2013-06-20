#Clase
class Coche:
    def __init__(self,  gasolina):
        self.gasolina = gasolina
        print "Tenemos",  gasolina,  "litros"

    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No se mueve"

#Herencia
class Terrestre:
    def desplazar(self):
        print "El animal anda"

class Acuatico:
    def nadar(self):
        print "El animal nada"

class Cocodrilo(Terrestre, Acuatico):
    pass
