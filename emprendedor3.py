
print("Bienvenida/o Este programa te entrega las posibles utilidades del negocio solo considerando \nun tipo de usuario y analizando las utilidades del año anterior.\n")

seguir=1

while(seguir==1):
    precio_suscripcion = int(input("\nIngrese el valor de la suscripción: "))
    usuarios = int(input("Ingrese el número de usuarios objetivo: "))
    gastos_totales = int(input("Ingrese el gasto total a incurrir: "))
    utilidad_anterior = int(input("Ingrese las utilidades del año anterior: "))

    utilidades= precio_suscripcion * usuarios - gastos_totales
    razon= utilidades/utilidad_anterior
    print(f"\nLas utilidades calculadas son: {utilidades}")
    print(f"Las razón entre las utilidades es de: {razon:.2f}")

    print("\n\n¿Deseas volver a calcular las utilidades?")
    respuesta=input("Ingresa la letra \'S\' en caso de querer seguir, sino cualquier otra letra para salir: ")
    if(respuesta == "s") or (respuesta == "S"):
        print("\nGenial, Volvamos a calcular'\n\n")

    else:
        seguir=0
        print("\nNos vemos en una próxima ocasión para calcular las utilidades, Chao")

    