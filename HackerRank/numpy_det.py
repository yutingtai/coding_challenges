import numpy as np


N = int(input())
arr = np.array([input().split() for i in range(N)], float)
print(round(np.linalg.det(arr),2))