def f(x):
    return x**3 - 5*x + 1

def delta_f(x):
    return 3*x**2 - 5

tol = 1e-6



def bisection(a,b,f,tol,it):
    # a와 b 함수와 tol 값을 인수로 받는다. 
    if f(a)* f(b) > 0:
        return print("error")
    #부호가 같으면 근이 그 사이에 없다. 잘 선택해서 다시 하자.
    print("1차")
    it = 0
    tol_new = (b-a)/2 
    #b와 a사이의 거리가 tol보다 작아지면 탈출

    while tol_new > tol:
        tol_new = (b-a)/2 
        middle  = (a+b)/2

        tol_new = (b-a)/2
        it += 1
        print(it)
        print("a값은",a)
        
        ##오류가 발생하니 재조정
        if tol_new < tol:
            break
        if f(middle) * f(a) < 0 or f(middle) == 0:  
            b = middle
        else:  
            a = middle
    
        x=(a+b)/2
    ## middle 값을 f에 대입하여 f(a) , f(b)와 부호가 같은지 비교 다르다면 middle값 재조정정
    return print(f"bicep x= {x} , it ={it}")



def newton(x,f,delta_f, tol,it):
    ## x ==처음 시작값
    it = 0
    print("tol:", tol)
    while it <100:
        it +=1
        x = x - f(x) / delta_f(x)
        if abs(x) < tol:
            break
    return print(f"newton의 x={x} , it = {it}")


print("start")
bisection(-1,1,f,tol,0)
newton(1,f,delta_f,tol,0)
