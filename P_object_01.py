#INTPUT
uit : float = 3600.00

#PROCESS
def p1 (bsueldo, utilidad ):
    #bsueldo = input("Insertar sueldo: ")
    #utilidad = input("Insertar Utilidad: ")
    ingreso_anual = (bsueldo * 14) + utilidad

    deducción_legal = 7 * uit

    base_imposible = ingreso_anual - deducción_legal

    if base_imposible < 0:

        monto :float = 0.0

    else:

        base_imposible * 0.21

    return monto

Isueldo = input("Insertar sueldo: ")

Iutilidad = input("Insertar Utilidad: ")

#output
print(p1 = Isueldo * Isueldo)