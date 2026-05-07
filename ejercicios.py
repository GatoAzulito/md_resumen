#Ejercicio 1
#Sumar dos números dados por el usuario e imprimir el resultado
def ejercicio1():
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")

#Ejercicio 2
#Sumar dos números dados por el usuario, y luego multiplicarlos por 2; imprimir el resultado
def ejercicio2():
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    suma = num1 + num2
    resultado = suma * 2
    print(f"La suma de {num1} y {num2} multiplicada por 2 es: {resultado}")

#Ejercicio 3
#Sumar dos números dados por el usuario. Si el resultado es mayor a 10, imprimir:
#"El resultado es mayor a 10". De lo contrario, imprimir: "El resultado es menor o igual a 10"
def ejercicio3(): 
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    resultado = num1 + num2
    if resultado > 10:
        print("El resultado es mayor a 10")
    else:
        print("El resultado es menor o igual a 10")

#Ejercicio 4
#Imprimir cada letra del nombre de un ingrediente dada por el usuario
def ejercicio4():
    palabra = input("Ingrese una palabra: ")
    for letra in palabra:
        print(letra)

#Ejercicio 5  
#Calcular la cantidad de vocales y consonantes en el nombre de un postre e imprimir los resultados
def ejercicio5():
    palabra = input("Ingrese una palabra: ")
    vocales = "aeiouAEIOU"
    cantidad_vocales = 0
    cantidad_consonantes = 0

    for letra in palabra:
        if letra in vocales:
            cantidad_vocales += 1
        else:
            cantidad_consonantes += 1

    print(f"La cantidad de vocales en la palabra '{palabra}' es: {cantidad_vocales}")
    print(f"La cantidad de consonantes en la palabra '{palabra}' es: {cantidad_consonantes}")

#Ejercicio 6
#Crear un programa que verifique si la receta de una masa para pasta es correcta.
#La receta correcta es: 100 gramos de harina, 2 de huevo, y 50ml de agua.
#El programa debe dejarle al usuario ingresar la cantidad de harina, huevo y agua
#El programa debe comprobar e informar si la receta se siguió correctamente.
#El programa debe contar con un menú: "1)Agregar ingredientes(harina, huevos, agua), 2)Verificar receta, 3)Salir, 4)Empezar de cero (reiniciar cantidades de ingredientes a 0)"


def ejercicio6():
    opcion = 0
    harina = 0
    huevos = 0
    agua = 0

    while opcion != 3:
        print("Menú:")
        print("1. Agregar ingredientes")
        print("2. Verificar receta")
        print("3. Salir")
        print("4. Empezar de cero")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            harina += int(input("Ingrese la cantidad de harina (en gramos): "))
            huevos += int(input("Ingrese la cantidad de huevos: "))
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
