class caballo:

    def __init__(self,color,raza,tipo,tamano,sexo,velocidad,posx,posy,posz):

        self.color = color
        self.raza = raza
        self.tamano = tamano
        self.sexo = sexo
        self.velocidad = velocidad
        self.posy = posy
        self.posx = posx
        self.posz = posz

    def saltar():
        print(f"El caballo {self.raza} ha saltado")

    def correr():
        print(f"El caballo {self.raza} ha corrido con una velocidad de {self.velocidad}")

    def parar():
        print(f"El caballo {self.raza} ha parado")

def main():

    caballo1 = ("Negro","KWPN","Grande","Macho", 70 "km/h"())

    caballo2 = ("Blanco","Shire","Mediano","Macho", 70 "km/h"())