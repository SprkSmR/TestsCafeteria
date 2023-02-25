import re
import functools

def comprobarNombre(nombreBebida):
    if re.search('[^a-zA-Z]', nombreBebida):
        raise Exception("El nombre de la bebida contiene caracteres invalidos")
    elif len(nombreBebida) > 15:
        raise Exception("Nombre de bebida demasiado largo (mas de 15)")
    elif len(nombreBebida) < 2:
        raise Exception("Nombre de bebida demasiado corto (menos de 1)")
    else:
        return True

def comprobarTam(tamanosBebidas):
    for i in range(len(tamanosBebidas)):
        iTam = tamanosBebidas[i].replace(" ", "")
        if re.search('[^\d]', iTam):
            raise Exception("Tamano invalido de bebida")
        elif int(iTam) > 48:
            raise Exception("Tamano de bebida fuera del rango (demasiado grande)")
        elif int(iTam) < 1:
            raise Exception("Tamano de bebida fuera del rango (demasiado pequeno)")
        for j in tamanosBebidas[i+1:]:
            j = j.replace(" ", "")
            if re.search('[^\d]', j):
                raise Exception("Tamano invalido de bebida")
            elif int(iTam) > int(j):
                raise Exception("Rango de tamanos incorrecto por estar en desorden")
    return True

def comprobarFormato(bebida):
    if len(bebida.replace(" ", "")) < 1:
        raise Exception("No hay informacion sobre la bebida (nombre, tamanos)")
    regExCheck = re.search('(^[^\d\,])+([^\,\d])*(\,(\s)?(([^\,\s])+)(\,(\s)?(([^\,\s])+))*)*', bebida)
    if regExCheck == None or regExCheck.group() != bebida:
        raise Exception("Los elementos de la bebida no estan formateados correctamente")
    nombreBebida = str.split(bebida, ",")[0].replace(" ", "")
    tamanosBebidas = str.split(bebida, ",")[1:]
    if len(tamanosBebidas) < 1:
        raise Exception("No hay tamanos de bebidas")
    elif len(tamanosBebidas) > 5:
        raise Exception("Hay demasiados tamanos de bebidas ingresados")

    try:
        comprobarNombre(nombreBebida)
        comprobarTam(tamanosBebidas)
    except Exception as error:
        raise

def agregar_nueva_bebida(bebida=""):
    try:
        comprobarFormato(bebida)
        return True
    except Exception as error:
        raise