import numpy as np
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
a2 = np.array(a)
b2 = np.array(b)

suma = a2 + b2
print(suma)
multi_a = a2 * 3
print(multi_a)
pot = b2 ** 2
print(pot)

x = [5, 8, 12, 20, 25, 30]
x2 = np.array(x)
print(x2[0])  # Primer elemento
print(x2[-1])  #Ultimo elemento
print(x2[1:4])  # Elementos del índice 1 al 3
print(x2[::2])  # Elementos con paso de 2
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]
matriz2 = np.array(matriz)
print(sum(matriz2))
suma_columnas = matriz2.sum(axis=1)
print(suma_columnas)