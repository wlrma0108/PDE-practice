import numpy as np

A = np.array([[4,3,0],[3,4,-1],[0,-1,4]], dtype=float)
b = np.array([24,30,-24], dtype=float)

def conjugate_gradient(A, b, tol=1e-6, max_iter=100):
    x = np.zeros_like(b)
    r = b - A.dot(x)
    p = r.copy()
    rs_old = r.dot(r)
    for k in range(max_iter):
        Ap = A.dot(p)
        alpha = rs_old / p.dot(Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rs_new = r.dot(r)
        if np.sqrt(rs_new) < tol:
            return x, k+1
        beta = rs_new / rs_old
        p = r + beta * p
        rs_old = rs_new
    return x, max_iter

x_cg, iter_cg = conjugate_gradient(A, b)
print("CG 반복 횟수:", iter_cg)
print("CG 최종 해:", x_cg)
