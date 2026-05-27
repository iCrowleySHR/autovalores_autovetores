# Um sistema de Inteligência Artificial utiliza uma matriz para representar a propagação de
# características em uma rede neural simplificada.
# A matriz do sistema é:
#  [4 2]
#  [1 3]
# Desenvolva um programa em Python para calcular os autovalores da matriz.

import numpy as np

A = np.array([[4, 2],
              [1, 3]])

autovalores, autovetores = np.linalg.eig(A)

print("Matriz A:")
print(A)
print("\nAutovalores:")
print(autovalores)
