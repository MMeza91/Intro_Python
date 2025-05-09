import math as m


print("Bienvenida/o, este programa te permite saber a que velocidad debes viajar para poder vencer la gravedad y escapar de un planeta. \nen adelante se te preguntarán algunos datos para saber tu velocidad de escape.\n\n")

seguir=1

while(seguir==1):
    g = float(input("Ingrese la constante de gravedad (g) del planeta en metros/segundos al cuadrado: "))
    valor_correcto=0

    while(valor_correcto==0):
        medida = input("\n¿Deseas escribir el radio en Kilometros (km) o Metros (m)?: ")
        if(medida == "m") or (medida == "M"):
            r = float(input("Ingrese el radio del planeta en metros: "))
            valor_correcto=1
            medida="m"
            break
        if(medida == "km") or (medida == "KM") or (medida == "Km") or (medida == "kM"):
            r = float(input("Ingrese el radio del planeta en kilonmetros: "))
            medida="km"
            valor_correcto=1
            break;
        else:
            print("Error, El valor ingresado debe ser \'Km\' o \'m\'")
            valor_correcto=0

    if(medida=="m"):    
        ve = m.sqrt(2*g*r)
        
    else:
        ve = m.sqrt(2*g*r*1000)
        


    print(f"La velocidad mínima para escapar del planeta es de {ve:.2f} m/s")
    print("\n\n¿Deseas calcular una velocidad de escape para otro planeta?")
    respuesta=input("Ingresa la letra \'S\' en caso de querer seguir, sino cualquier otra letra para salir: ")
    if(respuesta == "s") or (respuesta == "S"):
        print("\nGenial, intentemos de nuevo")

    else:
        seguir=0
        print("\nNos vemos en una próxima ocasión para saber nuevas velocidades de escape, Chao")

