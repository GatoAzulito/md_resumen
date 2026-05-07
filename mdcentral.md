# Guía básica de Python para nivel JUNIOR

Esta guía está pensada para empezar desde cero, con ejemplos simples y lenguaje claro.

---

## 1) Variables


Una **variable** es una “caja” donde guardas un valor.

```||||python
nombre = "Ana"
edad = 20
altura = 1.65
es_estudiante = True
```

Tipos básicos más comunes:
- `str`: texto
- `int`: enteros
- `float`: decimales
- `bool`: `True` o `False`

---

## 2) Input / Output

### Output (`print`)
Sirve para mostrar información en pantalla.

```python
print("Hola mundo")
print("Tu nombre es", nombre)
```

### Input (`input`)
Sirve para pedir datos al usuario.

```python
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
```

⚠️ `input()` siempre devuelve texto (`str`).

```python
edad = int(input("¿Qué edad tienes? "))
```

---

## 3) Operadores

### Aritméticos
- `+` suma
- `-` resta
- `*` multiplicación
- `/` división
- `//` división entera
- `%` módulo (resto)
- `**` potencia

```python
print(10 + 2)   # 12
print(10 // 3)  # 3
print(10 % 3)   # 1
```

### Comparación
- `==`, `!=`, `>`, `<`, `>=`, `<=`

### Lógicos
- `and`, `or`, `not`

```python
edad = 18
print(edad >= 18 and edad < 65)
```

---

## 4) if / else

Permite tomar decisiones.

```python
edad = 16

if edad >= 18:
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")
```

Con varios casos: `elif`

```python
nota = 7

if nota >= 9:
	print("Excelente")
elif nota >= 6:
	print("Aprobado")
else:
	print("Reprobado")
```

---

## 5) while / for

### `while`
Repite mientras una condición sea verdadera.

```python
contador = 1
while contador <= 3:
	print(contador)
	contador += 1
```

### `for`
Recorre elementos o rangos.

```python
for i in range(1, 4):
	print(i)
```

---

## 6) break / continue

- `break`: corta el bucle por completo.
- `continue`: salta a la siguiente vuelta.

```python
for i in range(1, 6):
	if i == 3:
		continue
	if i == 5:
		break
	print(i)
```

---

## 7) Listas

Una lista guarda varios elementos y se puede modificar.

```python
frutas = ["manzana", "banana", "pera"]
print(frutas[0])

frutas.append("uva")
frutas.remove("banana")
print(frutas)
```

Métodos útiles:
- `append()` agregar al final
- `remove()` eliminar por valor
- `pop()` eliminar por índice
- `len()` cantidad de elementos

---

## 8) Diccionarios

Guardan pares `clave: valor`.

```python
persona = {
	"nombre": "Luis",
	"edad": 25,
	"ciudad": "Madrid"
}

print(persona["nombre"])
persona["edad"] = 26
```

Métodos útiles:
- `keys()` claves
- `values()` valores
- `items()` clave y valor
- `get("clave")` evita error si no existe

---

## 9) Tuplas y Sets

### Tuplas (`tuple`)
Parecidas a listas, pero **inmutables**.

```python
vacia=()
conunelemento = (10,)
coordenada = (10, 20)
coordenadas2 = (10, 20, 30, 25)
cesta = ("manzana", "pera", "PALTA")
mixta = ("gato", 20, "perro", 35, 1.89)
print(coordenada[0])
print(colores[0:2])  # ('rojo', 'verde')
puntos=((1, 2), (3, 4), (5, 6))
print(puntos[1][0] #3)
```

### Desempaquetado
```python
persona = ("Luis", 30, "México")
nombre, edad, pais = persona
# nombre="Luis", edad=30, pais="México"
```

### Sets (`set`)
Colección sin orden y sin duplicados.

```python
numeros = {1, 2, 2, 3}
print(numeros)  # {1, 2, 3}
```

Útil para quitar repetidos:

```python
lista = [1, 1, 2, 3, 3]
sin_repetidos = list(set(lista))
```

---

## 10) Funciones

Una función agrupa código reutilizable.

```python
def saludar(nombre):
	return f"Hola, {nombre}"

mensaje = saludar("Ana")
print(mensaje)
```

Con valor por defecto:

```python
def saludar(nombre="invitado"):
	print("Hola", nombre)
```

---

## 11) return

`return` se usa dentro de una función para **devolver un valor**.

Cuando Python ejecuta `return`:
- termina la función en ese momento
- envía el valor al lugar donde se llamó la función

```python
def sumar(a, b):
	return a + b

resultado = sumar(3, 4)
print(resultado)  # 7
```

Sin `return`, la función devuelve `None` por defecto.

```python
def mostrar_mensaje():
	print("Hola")

valor = mostrar_mensaje()
print(valor)  # None
```

`return` también permite cortar antes según una condición:

```python
def dividir(a, b):
	if b == 0:
		return "No se puede dividir entre cero"
	return a / b

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # No se puede dividir entre cero
```

---

## 12) try / except

Sirve para manejar errores sin romper el programa.

```python
try:
	numero = int(input("Escribe un número: "))
	print(10 / numero)
except ValueError:
	print("Debes escribir un número válido")
except ZeroDivisionError:
	print("No puedes dividir entre cero")
```
otros except:
```
TypeError: Datos incorrectos (Ej Sumar número con texto)
IndexError: Index inexistente 
KeyError: Claves inexistentes
NameError: Variables no definidas
AttributeError: Atributos inexistente de objeto
FileNotFoundError: Archivo inexistente en ruta
RuttimeError: Errores genéricos
```

---

## 13) raise

`raise` permite lanzar un error manualmente.

```python
edad = -2

if edad < 0:
	raise ValueError("La edad no puede ser negativa")
```

---

## 14) Clases

Una clase es una **plantilla** para crear objetos.

- La clase define atributos (datos) y métodos (acciones).
- Un objeto es una instancia concreta de esa clase.
- `self` representa al objeto actual.

Ejemplo básico:

```python
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def saludar(self):
		print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

p1 = Persona("Marta", 30)
p1.saludar()
```

### Atributos y métodos

- **Atributos**: variables que pertenecen al objeto (`self.nombre`).
- **Métodos**: funciones dentro de la clase (`saludar`).

```python
class Coche:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.encendido = False

	def encender(self):
		self.encendido = True

	def estado(self):
		return "encendido" if self.encendido else "apagado"

mi_coche = Coche("Toyota", "Corolla")
print(mi_coche.estado())  # apagado
mi_coche.encender()
print(mi_coche.estado())  # encendido
```

### Constructor `__init__`

`__init__` se ejecuta automáticamente al crear el objeto y se usa para inicializar sus valores.

```python
class Producto:
	def __init__(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

pan = Producto("Pan", 1.2)
print(pan.nombre, pan.precio)
```

---

## 15) Herencia

Una clase hija hereda de una clase padre.

```python
class Animal:
	def hablar(self):
		print("Sonido")

class Perro(Animal):
	pass

mi_perro = Perro()
mi_perro.hablar()
```

---

## 16) Polimorfismo

Distintas clases pueden usar el mismo método con comportamiento distinto.

```python
class Gato:
	def hablar(self):
		print("Miau")

class Vaca:
	def hablar(self):
		print("Muuu")

for animal in [Gato(), Vaca()]:
	animal.hablar()
```

---

## 17) Archivos

Leer y escribir archivos con `open`.

### Escribir
```python
with open("datos.txt", "w", encoding="utf-8") as archivo:
	archivo.write("Hola archivo")
```

### Leer
```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
	contenido = archivo.read()
	print(contenido)
```

Modos comunes:
- `"r"`: leer
- `"w"`: escribir (sobrescribe)
- `"a"`: agregar al final

---

## 18) Lambdas

Una `lambda` es una función pequeña en una sola línea.

```python
def doble(X): #Version como función
	return x * 2
doble = lambda x: x * 2 #Version lambda
#Las dos multiplican el dato por 2
```

Muy usadas con `map`, `filter`, `sorted`.

```python
numeros = [1, 2, 3]
resultado = list(map(lambda n: n * 2, numeros)) #Map recorre 1 a 1 multiplicando por 2
print(resultado)
```

---

## 19) Librerías

Las librerías te dan funciones ya hechas para no empezar de cero.

### Librerías estándar (ya vienen con Python)
- `math, random, datetime, nunpy, time`

```python
import math
print(math.sqrt(16)) #Calcula raiz cuadrada
```

### Librerías externas
Se instalan con `pip`.

```bash
pip install requests
```

```python
import requests
respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)
```

---
