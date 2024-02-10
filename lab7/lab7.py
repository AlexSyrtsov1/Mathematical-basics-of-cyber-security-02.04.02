
def euclid_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = euclid_extended(b, a%b)
        x = yy 
        y = xx - (a // b) * yy
        return d, x, y

def inverse(a, n):
    return (euclid_extended(a, n)[1])

def xab(x, a, b, x_swap):
    (G, H, P, Q) = x_swap
    sub = x % 3
    if sub == 0:
        x = x*x_swap[0] % x_swap[2]
        a = (a+1) % Q
    if sub == 1:
        x = x * x_swap[1] % x_swap[2]
        b = (b + 1) % x_swap[2]
    if sub == 2:
        x = x*x % x_swap[2]
        a = a*2 % x_swap[3]
        b = b*2 % x_swap[3]
    return x, a, b

def pollard(G, H, P):
    Q = int((P - 1) // 2)
    x = G*H
    a = 1
    b = 1
    X = x
    A = a
    B = b
    for i in range(1, P):
        x, a, b = xab(x, a, b, (G, H, P, Q))
        X, A, B = xab(X, A, B, (G, H, P, Q))
        X, A, B = xab(X, A, B, (G, H, P, Q))
        if x == X:
            break
    nom = a-A
    denom = B-b
    res = (inverse(denom, Q) * nom) % Q
    if verify(G, H, P, res):
        return res
    return res + Q

def verify(g, h, p, x):
    return pow(g, x, p) == h

args = [(10, 64, 107)]

for arg in args:
    res = pollard(*arg)
    print(arg, ':    x =', res)
    print("Верификация: ", verify(arg[0], arg[1], arg[2], res))
    print()