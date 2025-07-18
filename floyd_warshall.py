import numpy as np

def floyd_warshall(D):
    n = D.shape[0]
    pred = np.full((n, n), -1)

    for i in range(n):
        for j in range(n):
            if D[i][j] != np.inf and i != j:
                pred[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    pred[i][j] = pred[k][j]

    return D, pred
