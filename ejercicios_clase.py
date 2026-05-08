import random, time
# crea un numero random entre 1 y 100
# Pide al usuario que adivine el numero
# si el usuario pone un numero mayor al generado
# debe decir " Te pasaste", en caso contrario
# " EL numero a adividar es mayor"
# Solo hay 5 posibilidades de adivinar.

def adivina_numero():
    num=random.randint(1,100)
    for i in range(5):
        num_user=int(input("Adivina el número: "))
        if num_user>num:
            print("Te pasaste!!")
        elif num_user<num:
            print("Te falta!!")
        else:
            print("Adivinaste el número!!")

# Dos peleadores se piden al inicio de la pelea
# Cada peleador inicia con 100 de HP 
# se debe hace una pelea por turnos 
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los 2
# tiene su HP menor o igual a 0
# se debe mostrar el ganador al final
# BONUS: mostrar al barras de energia de cada peleador.
# time.sleep(2)

def killer_instinct():
    player_1=input("Nombre del jugador 1: ")
    player_2=input("Nombre del jugador 2: ")
    p1_hp=100
    p2_hp=100
    turno=True
    while p1_hp>0 and p2_hp>0:
        if turno==True:
            print(f"Turno de {player_1}")
            time.sleep(1)
            daño=random.randint(7,18)
            p2_hp-=daño
            if p2_hp < 0:
                p2_ph = 0
            print(f"{player_1} hizo {daño} puntos de daño")
            time.sleep(1)
            print(f"A {player_2} le quedan {p2_hp} puntos de vida ")
            turno=False
        elif turno==False:
            print(f"Turno de {player_2}")
            time.sleep(1)
            daño=random.randint(7,18)
            p1_hp-=daño
            if p1_hp < 0:
                p1_ph = 0
            print(f"{player_2} hizo {daño} puntos de daño")
            time.sleep(1)
            print(f"A {player_1} le quedan {p1_hp} puntos de vida ")
            time.sleep(1)
            turno=True
    if p1_hp>p2_hp:
        time.sleep(3)
        print(f"{player_1} ha ganado!!")
    else:
        time.sleep(3)
        print(f"{player_2} ha ganado!!")

# Ludo 
# 1 jugador juega, y lanzar dos dados
# por cada unidad en el dado avanza una posicion en el tablero
# cuando llegue a 50 , gana
# mostrar cuantos turnos le tom
# llegar a la meta
def ludo():
    player1=input("Ingresa tu nombre: ")
    casilla=0
    turno=0
    while casilla<50:
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        time.sleep(1)
        print("Tiraste los dados")
        time.sleep(1)
        print(f"Resultado de los dados: {dado1} y {dado2}")
        casilla=casilla + dado1 + dado2
        if casilla>50:
            casilla=50
        time.sleep(1)
        print(f"Avanzas a la casilla {casilla}!")
        turno+=1
    print(f"Completaste el ludo en {turno} turnos!!")

# # 3 personas juegan golf
# # cada persona tiene la posibilidad de golpear
# # y la distancia varia ente 60 y 190 metros
# # mostrar al final, el golpe mas fuerte
def golf():
    metros=[]
    for i in range(3):
        tiro=random.randint(60,190)
        time.sleep(1)
        print(f"Persona {i+1} lanzó la pelota {tiro} metros!!")
        metros.append(tiro)
        tiro_mayor= max(metros)
        persona=metros.index(tiro_mayor)
        
    print(f"La distancia más lejana fue de {tiro_mayor} metros, por Persona {persona+1}")

# # generar 3 numeros entre 1 y 9
# # luego, tirar numeros al azar en ese rango 
# # Cuando todos los numeros coincidan con los primeros 3 
# # generados, debe poner "ganaste"
# # contar , cuantos numeros tuvo que tirar
# # para ganar la loteria .

def loteria():
    num1=random.randint(1,9)
    num2=random.randint(1,9)
    num3=random.randint(1,9)
    lista_ganadora=[num1,num2,num3]
    lista_generados=[]
    turno = 0
    print(f"Los números son {num1}, {num2}, {num3}")
    generar=input("Presione Enter para generar números")
    while sorted(lista_ganadora) != sorted(lista_generados):
        while len(lista_generados)<=2:
            turno += 1 
            num=random.randint(1,9)
            lista_generados.append(num)
            time.sleep(1)
            print(lista_generados)
        turno += 1
  
        num=random.randint(1,9)
        lista_generados.append(num)
        lista_generados.pop(0)
        time.sleep(1)
        print(lista_generados)
    print(f"Ganaste!!! (En el turno {turno})")

def profe():
    n1=random.randint(1,9)
    n3=random.randint(1,9)
    n2=random.randint(1,9)
    t1=False
    t2=False
    t3=False
    nums=0
    print(f"Los numeros generados son: {n1}, {n2} y {n3}")
    while not t1 or not t2 or not t3:
        numerito=random.randint(1,9)
        print("EL numero es", numerito)
        time.sleep(1)
        if numerito==n1:
            t1=True
        if numerito==n2:
            t2=True
        if numerito==n3:
            t3=True
        nums+=1
    print(f"GANASTE, en {nums} turnos")

# Fabrica de enlatados
# Se necesita hacer el algoritomo de productos enlatados
# Se debe consultar el peso del producto( en gramos) (solo valores positivos)
# El porcentaje de sodio en él (solo valores entre 1 y 100)
# y si se va a vender nacional o internacionalmente
# Considerar los criterios en la siguiente tabla
def enlatados():
    respuestas=["si", "sí", "no"]
    try:
        peso=int(input("Ingrese el peso del producto: "))
        sodio=int(input("Ingrese la cantidad de sodio: "))
    except ValueError:
        print("Error: tipo de dato inválido")
        return
    exportacion=input("¿Su producto es internacional? ").lower()
    if exportacion in respuestas:
        pass
    else:
        raise ValueError("Respuesta inválida")
        return
    if peso<500:
        lata="normal"
    elif peso>=500 and peso<=1500:
        lata="mediana"
    elif peso>1500:
        lata="grande"
    else:
        print("Peso inválido")
    if sodio<5:
        tipo=""
    elif sodio>=5 and sodio<=8:
        tipo="especial"
    elif sodio>8:
        tipo="acorazada"
    else:
        print("Cantidad de sodio inválida")
    if exportacion=="si" or exportacion=="sí":
        sello="con sticker de validación sanitaria"
    else:
        sello=""
    print(f"lata {lata} {tipo} {sello}")

def absoluto():
    num=random.randint(1,9)
    while abs(-3)!=num:
        print(num)
        time.sleep(1)
        num=random.randint(1,9)
    print("El numero es", num)
absoluto()
