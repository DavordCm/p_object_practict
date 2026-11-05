#INPUT
class Alumno:
    Paises = "Peru"

    def __init__(self, codigo, edad, nombre, not1, not2):

        self.codigo = codigo #Codigo del alumno

        self.edad = edad     #Edad del alumno

        self.nombre = nombre #Nombre del alumno

        self.not1 = not1     # Nota 1 del alumno

        self.not2 = not2     # Nota 2 del alumno

    def C_Promedio(self):
        #Promedio de las notas 1 y nota 2 dando resultados
        Promedio = (self.not1 + self.not2) / 2
        return Promedio

def main():

    estudiante = Alumno(750145023, 24, "Davor", 14.5, 15.5)
    estudiante2 = Alumno(740243061, 18, "Brayan", 15, 20)

    print (f"Promedio: {estudiante.nombre} con el codigo {estudiante.C_Promedio()}")
    #print ("Promedio: ",estudiante.nombre, "Con el codigo",estudiante.codigo , estudiante.C_Promedio())
    print ("-----------------------------------------------")
    print ("Promedio:",estudiante2.nombre,"Con el codigo",estudiante2.codigo,estudiante2.C_Promedio())
    
if __name__ == "__main__":
    main()