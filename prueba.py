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

def ejercicio2():
    exportacion= ["nacional", "internacional"]
    latas=random.randint(1,10)
    for i in range(latas):
        peso=random.randint(100, 2000)
        sodio=random.randint(1, 12)
        export=random.choice(exportacion)
        time.sleep(1)
        if peso<=500:
            if sodio<5:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata normal sin sello")
            elif sodio>=5 and sodio<=8:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata especial sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata especial con sello")
            else:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata acorazada sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata acorazada con sello")
        elif peso>500 and peso<=1500:
            if sodio<5:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata mediana sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata mediana con sello")
            elif sodio>=5 and sodio<=8:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata mediana especial sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata mediana especial con sello")
            else:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata mediana acorazada sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata mediana acorazada con sello")
        else:
            if sodio<5:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata grande sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata grande con sello")
            elif sodio>=5 and sodio<=8:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata grande especial sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata grande especial con sello")
            else:
                if export=="nacional":
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata grande acorazada sin sello")
                else:
                    print(f"Peso: {peso} gramos, sodio: {sodio} mg, exportación: {export}")
                    print("Lata grande acorazada con sello")

ejercicio2()
#HOLA