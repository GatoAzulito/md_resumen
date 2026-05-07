#1)Crear un programa que pregunte al usuario su nombre, edad y comida favorita.
#Luego, imprima un mensaje que contenga esa información
#Ejemplo: "Hola, mi nombre es [nombre], tengo [edad] años y mi comida favorita es [comida favorita]."

#2)Crear un programa que pregunte al usuario por un número, y luego muestre
#el numero anterior, el numero ingresado, y el numero siguiente
#Ejemplo: "Números: 3, 4, 5"

#3)Crear un programa que pregunte por cantidad de dinero y si tiene receta médica.
#Si tiene el dinero suficiente y tiene receta médica, el medicamento se puede vender(Cuesta $10mil pesos).

#4)Crear un programa que pregunte al usuario su edad y muestre por pantalla todos
#los años que ha cumplido (desde 1 hasta su edad)

#5)Crea un juego que se trate de adivinar una palabra secreta. El usuario tiene 3 intentos.
#el programa debe informar cuando el usuario lo hace mal o bien.
#la palabra secreta es "python"
#Puedes usar .lower() para convertir la respuesta del usuario a minúsculas
#ejemplo: respuesta=PYTHON     respuesta.lower()        respuesta=python
# respuesta= input("Adivina la palabra").lower()         respuesta=python 



#------------------------------------RESPUESTAS------------------------------------------------

def ejercicio1():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    comida= input("Ingrese su comida favorita: ")
    print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mi comida favorita es {comida}.")

def ejercicio2():
    numero = int(input("Ingrese un numero"))
    print(f"Números: {numero-1}, {numero}, {numero+1}")

def ejercicio3():
    dinero = int(input("Ingrese la cantidad de dinero que tiene: "))
    receta = input("¿Tiene receta médica? (si/no): ")
    if dinero >= 10000 and receta == "si":
        print("El medicamento se puede vender.")
    else:
        print("No se puede vender el medicamento.")

def ejercicio4():
    edad = int(input("Ingrese su edad: "))
    for i in range(edad):
        print(f"Ha cumplido {i+1} años")

def ejercicio5():
    palabra_secreta = "python"
    intentos = 3
    for palabra in range(intentos):
        respuesta = input("Adivina la palabra secreta: ").lower()
        if respuesta == palabra_secreta:
            print("¡Correcto! Has adivinado la palabra.")
            break
        else:
            print("Incorrecto. Inténtalo de nuevo.")
    else:
        print("Lo siento, has agotado tus intentos.")
