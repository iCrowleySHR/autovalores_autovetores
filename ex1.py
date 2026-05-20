import numpy as np

A = np.array(([2, 0],
              [0, 5]), dtype=float
            )

autovalores, autovetores = np.linalg.eig(A)

print("Matriz A: \n", A)
print("\n Autovalores", autovalores)