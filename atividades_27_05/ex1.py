# Uma empresa de desenvolvimento de jogos digitais precisa aplicar uma transformação
# geométrica em objetos 2D para aumentar o tamanho das imagens na tela sem alterar sua direção
# original.
# A transformação é representada pela matriz:
#  [2 0]
#  [0 5]
# Desenvolva um programa em Python para calcular os autovalores dessa matriz e interpretar o
# efeito da transformação nos eixos x e y

import numpy as np
A = np.array([[2, 0],
              [0, 5]])
autovalores, autovetores = np.linalg.eig(A)

print("Matriz A:")
print(A)
print("\nAutovalores:")
print(autovalores)