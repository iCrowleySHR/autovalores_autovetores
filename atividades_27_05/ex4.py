# Uma aplicação de Ciência de Dados recebe informações organizadas em uma matriz 2x2
# representando correlação entre variáveis.
# Desenvolva um programa em Python que:
# • capture os elementos da matriz via teclado;
# • monte a matriz utilizando NumPy;
# • calcule os autovalores;
# • exiba os resultados encontrados

import numpy as np

print("Digite os elementos da matriz 2x2")

a11 = float(input("a11: "))
a12 = float(input("a12: "))
a21 = float(input("a21: "))
a22 = float(input("a22: "))

A = np.array([[a11, a12],
              [a21, a22]])

autovalores, autovetores = np.linalg.eig(A)

print("\nMatriz A:")
print(A)
print("\nAutovalores:")
print(autovalores)