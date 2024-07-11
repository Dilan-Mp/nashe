import funcionesMETRO as ff
ff.creaArchivo()
while True:
    print("1. Venta de boletos")
    print("2. Eliminar venta")
    print("3. Mostrar una venta especifica")
    print("4. Salir del programa")

    op = ff.validaOpcion()

    if op == 1:
        rut = ff.validaRut()
        horario = ff.validaHorario()
        tipo = ff.validaTipo()
        cantidad = ff.validaCantidad()
        valorBoleto = ff.valorBoleto(tipo, cantidad, horario, rut)
    
    if op == 2:
        rut = ff.validaRut()
        ff.eliminarVenta(rut)
    
    if op == 3:
        rut = ff.validaRut()
        ff.mostrarCompra(rut)
    
    if op == 4:
        break