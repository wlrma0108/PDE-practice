import numpy as np

def solve_bvp(h):
    # 격자
    N = int((np.pi/2)/h)
    x = np.linspace(0, np.pi/2, N+1)
    # 행렬 A, 우변 b 설정
    n = N-1
    A = np.zeros((n,n))
    b = np.cos(x[1:-1])
    # 계수
    alpha = 1/h**2 + 1/(2*h)
    beta  = -2/h**2 - 2
    gamma = 1/h**2 - 1/(2*h)
    # 경계 y0, yN
    y0, yN = -0.3, -0.1
    for i in range(n):
        if i>0:   A[i,i-1] = alpha
        A[i,i]   = beta
        if i<n-1: A[i,i+1] = gamma
        # 경계 기여
        if i==0:      b[i] -= alpha*y0
        if i==n-1:    b[i] -= gamma*yN
    # 선형시스템 풀이
    w = np.linalg.solve(A, b)
    # 전체 해: 경계 포함
    yh = np.empty(N+1)
    yh[0], yh[-1] = y0, yN
    yh[1:-1] = w
    return x, yh

# 다양한 h에 대해 오차 계산
hs = [np.pi/4, np.pi/8, np.pi/16, np.pi/32, np.pi/64, np.pi/128]
errors = []
for h in hs:
    x, yh = solve_bvp(h)
    y_exact = -0.1*np.sin(x) - 0.3*np.cos(x)
    # 이산 L2 오차
    err = np.sqrt(h * np.sum((yh - y_exact)**2))
    errors.append(err)

# 결과 출력
print("   h       L2 Error    Ratio")
for i,h in enumerate(hs):
    ratio = errors[i-1]/errors[i] if i>0 else np.nan
    print(f"{h:8.5f}  {errors[i]:.2e}  {ratio:.2f}")
