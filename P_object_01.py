#INTPUT
uit = 3600.0

#PROCESS
def p1 (bsueldo, utilidad ):

    ingreso_anual = (bsueldo * 14) + utilidad

    deduccion_legal = 7 * uit

    base_imposible = ingreso_anual - deduccion_legal

    if base_imposible < 0:

        monto = 0.0

    else:

        monto = base_imposible * 0.21

    return monto

Isueldo = float(input("Insertar sueldo: "))

Iutilidad = float(input("Insertar Utilidad: "))

#output
resultado = p1 (Isueldo,Iutilidad)

print(resultado)