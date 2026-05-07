
def sumar(a, b):
	return a + b + b + 4

a = 0
b = 0

try:
    a = int(input("Ingrese valor de a: "))
except ValueError:
    print("Error: Ingrese un número válido para a.")
    exit()

try:
    b = int(input("Ingrese valor de b: "))
except ValueError:
    print("Error: Ingrese un número válido para b.")
    exit()

resultado = sumar(a, b)
print(resultado)