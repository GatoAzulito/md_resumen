import random, time
from colorama import init, Fore, Style
# num=random.randint(1,9)
# while abs(-3)!=num:
#     print(num)
#     time.sleep(1)
#     num=random.randint(1,9)
# n1=int(input("Ingrese valor limite inferior: "))
# n2=int(input("Ingrese valor limite superior: "))
# #VALIDAR QUE EL LIMITE SUPERIOR SEA MAYOR QUE EL LIMITE INFERIOR
# #HAY UN LIMITE QUE ROMPE EL DESEO  
# num=random.randint(n1,n2)
# print(num)
init()
#500 gramos lata normal
#501 a 1500 lata grande
#sodio entre 5 y 8 lata especial
#sodio mayor a 9 lata acorazada
#internacional sello validacion
def peces():
    total_peces=random.randint(10,20)
    lata=0
    plancha=0
    for i in range(total_peces):
        pez=random.randint(100, 3000)
        time.sleep(1)
        if pez<=800:
            print(f"El pez pesa: {pez} gramos")
            print("Pez enlatado")
            lata+=1
        elif pez>800 and pez<=3000:
            print(f"El pez pesa: {pez} gramos")
            print(Fore.RED + "Pez planchado" + Style.RESET_ALL)
            plancha+=1
    print("Total de peces enlatados: ",lata)
    print("Total de peces planchados: ",plancha)






def print_all(peso, sodio, export):
    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")

def tiene_sello(export):
    if export=="internacional":
        return True
    else:
        return False
    
def determina_tipo_lata(peso, sodio):
    if peso<=500:
        if sodio<5:
            return "Lata normal"
        elif sodio>=5 and sodio<=8:
            return "Lata especial"
        else:
            return "Lata acorazada"
    elif peso>500 and peso<=1500:
        if sodio<5:
            return "Lata mediana"
        elif sodio>=5 and sodio<=8:
            return "Lata mediana especial"
        else:
            return "Lata mediana acorazada"
    else:
        if sodio<5:
            return "Lata grande"
        elif sodio>=5 and sodio<=8:
            return "Lata grande especial"
        else:
            return "Lata grande acorazada"

def ejercicio2():
    exportacion= ["nacional", "internacional"]
    latas=random.randint(1,10)
    for _ in range(latas):
        peso = random.randint(100, 2000)
        sodio = random.randint(1, 12)
        export = random.choice(exportacion)
        time.sleep(1)
        tipo = determina_tipo_lata(peso, sodio)
        sello = "con sello" if tiene_sello(export) else "sin sello"
        print_all(peso, sodio, export)
        print(f"{tipo} {sello}")

ejercicio2()
