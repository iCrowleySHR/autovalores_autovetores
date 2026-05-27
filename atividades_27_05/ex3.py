# Um sistema mecânico possui três modos principais de vibração representados pela matriz:
#  [1 2 0]
#  [2 1 0]
#  [0 0 3]
# Desenvolva um programa em Python para calcular os autovalores da matriz.


import numpy as np
A = np.array([[1, 2, 0],
              [2, 1, 0],
              [0, 0, 3]])

autovalores, autovetores = np.linalg.eig(A)

print("Matriz A:")
print(A)
print("\nAutovalores:")
print(autovalores)