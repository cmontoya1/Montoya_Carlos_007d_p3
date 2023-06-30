import funciones as fn

while True:
    fn.mostrar_menu()
    opc=fn.validar_opcion()
    if opc==1:
        fn.grabar()
    elif opc==2:
        fn.buscar_mascota()
    elif opc==3:
        fn.Retirarse()
    else:
        fn.salir()
        