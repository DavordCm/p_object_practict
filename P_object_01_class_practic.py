class Caballo:

    def __init__(self,color,raza,tipo,tamano,sexo,velocidad,posx,posy,posz):

        self.color = color
        self.raza = raza
        self.tipo = tipo
        self.tamano = tamano
        self.sexo = sexo
        self.velocidad = velocidad
        self.posy = posy
        self.posx = posx
        self.posz = posz

    def saltar(self):
        print(f"El caballo {self.raza} ha saltado")

    def correr(self):
        print(f"El caballo {self.raza} ha corrido con una velocidad de {self.velocidad}")

    def parar(self):
        print(f"El caballo {self.raza} ha parado")

def main():

    caballo1 = Caballo("Negro","KWPN","Deportivo","Grande","Macho", "70 km/h",0 ,0 ,0)

    caballo2 = Caballo("Blanco","Shire","Paseo","Mediano","Macho", "70  km/h",1 ,1 ,0)

    caballo1.correr
    caballo2.parar

    print(f"caballo1.correr")
    print(f"caballo2.parar")


if __name__ == "__main__":
    main()