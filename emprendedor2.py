print("Bienvenida/o Este programa te entrega las posibles utilidades del negocio \nconsiderando dos tipos de usuarios.\n")

seguir=1

while(seguir==1):
    precio_suscripcion = int(input("\nIngrese el valor de la suscripción: "))
    usuarios_normales = int(input("Ingrese el número de usuarios estandar: "))
    usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
    gastos_totales = int(input("Ingrese el gasto total a incurrir: "))

    utilidades= precio_suscripcion * (usuarios_normales + (usuarios_premium*1.5)) - gastos_totales

    print(f"\nLas utilidades calculadas son: {utilidades:.0f}")

    print("\n\n¿Deseas volver a calcular las utilidades?")
    respuesta=input("Ingresa la letra \'S\' en caso de querer seguir, sino cualquier otra letra para salir: ")
    if(respuesta == "s") or (respuesta == "S"):
        print("\nGenial, Volvamos a calcular'\n\n")

    else:
        seguir=0
        print("\nNos vemos en una próxima ocasión para calcular las utilidades, Chao")

    


