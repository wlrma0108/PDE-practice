import numpy as np

A = np.array([[4,3,0],[3,4,-1],[0,-1,4]], dtype=float)
b = np.array([24,30,-24], dtype=float)

def steepest_descent(A, b, tol=1e-6, max_iter=10000):
    x = np.zeros_like(b)
    for k in range(max_iter):
        r = b - A.dot(x)
        if np.linalg.norm(r) < tol:
            return x, k+1
        alpha = r.dot(r) / r.dot(A.dot(r))
        x = x + alpha * r
    return x, max_iter

x_final, iterations = steepest_descent(A, b)
print("반복 횟수:", iterations)
print("최종 해:", x_final)
