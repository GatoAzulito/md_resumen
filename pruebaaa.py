opcion=0
harina=0
huevos=0
agua=0
while opcion!= 3:
    print("Menú:")
    print("1. Agregar ingredientes")
    print("2. Verificar receta")
    print("3. Salir")
    print("4. Empezar de cero")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        harina += int(input("Ingrese la cantidad de harina (en gramos): "))
        huevos += int(input("Ingrese la canti|dad de huevos: "))
        agua += int(input("Ingrese la cantidad de agua (en ml): "))
    elif opcion == 2:
        if harina == 100 and huevos == 2 and agua == 50:
            print("La receta se siguió correctamente.")
        else:
            print("La receta no se siguió correctamente.")
    elif opcion == 3:
        print("Saliendo del programa")
    elif opcion == 4:
        harina = 0
        huevos = 0
        agua = 0
        print("Cantidades de ingredientes reiniciadas a 0.")
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")