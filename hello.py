def add(x,y):
    return x+y

def larger(x,y):
    if (x>y):
        return x
    else:
        return y

def xor(a,b):
    return ((a and not b) or (b and not a))

def hello(n):
    for i in range(n):
        print("hello")

def fraction(n):
    for i in range(1,n+1):
        print(float(1/i))
    
fraction(5)