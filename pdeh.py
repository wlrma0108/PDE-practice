import numpy as np

def solve_bvp(h):
    """
    Solve the BVP y'' = y' + 2y + cos(x), 0<=x<=pi/2, y(0)=-0.3, y(pi/2)=-0.1
    using a linear finite‐difference method with step size h.
    Returns grid x and solution y_h at the grid points.
    """
    # Number of intervals
    N = int((np.pi/2) / h)
    # Grid points x0, x1, ..., xN with x0=0, xN=pi/2
    x = np.linspace(0, np.pi/2, N+1)
    # Number of interior unknowns
    n = N - 1

    A = np.zeros((n, n))
    b = np.zeros(n)

    alpha = 1/h**2 + 1/(2*h)
    beta  = -2/h**2 - 2
    gamma = 1/h**2 - 1/(2*h)

    y0, yN = -0.3, -0.1

    for i in range(n):
        A[i, i] = beta
        if i > 0:
            A[i, i-1] = alpha
        if i < n-1:
            A[i, i+1] = gamma

        b[i] = h**2 * np.cos(x[i+1])

        if i == 0:
            b[i] -= alpha * y0
        if i == n-1:
            b[i] -= gamma * yN

    w = np.linalg.solve(A, b)

    y_h = np.empty(N+1)
    y_h[0]   = y0
    y_h[1:-1] = w
    y_h[-1]  = yN

    return x, y_h

if __name__ == "__main__":
    h = np.pi/8
    x, y_h = solve_bvp(h)
    print("x =", x)
    print("y_h =", y_h)
