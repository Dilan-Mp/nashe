import csv
def creaArchivo():
    with open('archivo_csv', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(['Rut','Tipo','Horario','Cantidad','Valor'])
def validaOpcion():
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            if op > 0 and op <  5:
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Ingresaste un valor invalido, intenta de nuevo")
    return op

def validaRut():
    while True:
        try:
            rut = input("Ingrese su rut: ")
            if len(rut.strip()) == 8:
                break
        except ValueError:
            print("Ingresaste un valor invalido, intenta de nuevo")
    return rut

def validaHorario():
    while True:
        try:
            horario = input("Ingrese un horario entre Alto/Bajo/Medio: ")
            if horario.lower() == "alto" or horario.lower() == "bajo" or horario.lower() == "medio":
                break
            else:
                print("Horario no existente")
        except ValueError:
            print("Ingresaste un valor invalido, intenta de nuevo")
    return horario.lower()

def validaTipo():
    while True:
        try:
            tipo = input("Ingrese que tipo de usuario eres Normal/AdultoMayor/Estudiante: ")
            if tipo.lower() == "normal" or tipo.lower() == "adultomayor" or tipo.lower() == "estudiante":
                break
            else:
                print("Tipo de usuario no existente")
        except ValueError:
            print("Ingresaste un valor invalido, intenta de nuevo")
    return tipo.lower()

def validaCantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de boletos que desea: "))
            if cantidad > 0:
                break
            else:
                print("Cantidad invalida")
        except ValueError:
            print("Ingresaste un valor invalido, intenta de nuevo")
    return cantidad

def valorBoleto(tipo, cantidad, horario, rut):
    if tipo == "normal":
        if horario == "alto":
            valor = 2000 * cantidad
        elif horario == "bajo":
            valor = 550 * cantidad
        elif horario == "medio":
            valor = 1200 * cantidad
    elif tipo == "estudiante":
        if horario == "alto":
            valor = 500 * cantidad
        elif horario == "bajo":
            valor = 180 * cantidad
        elif horario == "medio":
            valor = 300 * cantidad
    elif tipo == "adultomayor":
        valor = 50 * cantidad
    
    print(f"Se realizo la siguiente comprar\n Tipo = {tipo}\n Horario = {horario}\n Cantidad = {cantidad}\n Total a cancelar = {valor}")

    with open('archivo_csv', 'a', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerows([
            [rut,tipo,horario,cantidad,valor]
        ])
    return valor

def eliminarVenta(rut):
    ruts = []
    with open('archivo_csv', 'r',newline='') as archivo_csv:
        info = csv.reader(archivo_csv)
        ruts = list(info)

    with open('archivo_csv', 'w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        for fila in ruts:
            if fila[0] != rut:
                escritor.writerow(fila)
    print("Compras del rut, eliminadas del archivo")

def mostrarCompra(rut):
    ruts = []
    try:
        with open('archivo_csv', 'r', newline='') as archivo_csv:
            info = csv.reader(archivo_csv)
            ruts = list(info)
            for fila in ruts:
                if fila[0] == rut:
                    print(f"BOLETO\n Rut = {fila[0]}\n Tipo = {fila[1]}\n Horario = {fila[2]}\n Cantidad = {fila[3]}\n Total a pagar = {fila[4]}")
    except FileNotFoundError:
        print("El archivo no existe")
