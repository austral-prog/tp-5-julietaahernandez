def roots(a, b, c):
    discriminante = b ** 2 - 4 * a * c 
    r1 = (-b + (discriminante)**0.5)/ (2*a)
    r2 = (-b - (discriminante)**0.5)/ (2*a)
    if discriminante > 0:
        return f"{r1, r2}"
    elif discriminante == 0:
        r12 = (-b - (discriminante)**0.5)/ (2*a)
        return f"({r12})"
    else:
        return "( )"

def value_y(a, b, c, x):
    y = a * x ** 2 + b * x + c
    return y 

def to_string(a, b, c):  
    if a == 0 and b == 0 and c == 0:
        return "f(x) = 0" 
    elif a == 0 and b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"  
    elif a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}" 
    elif a == 0 and b == 0 and c != 0:
        return f"f(x) = {c}"
    elif a == 0 and b != 0 and c == 0:
        return f"f(x) = {b} * X" 
    elif a != 0 and b == 0 and c == 0:
        return f"f(x) = {a} * X^2" 
    elif a != 0 and b == 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}" 
    else:
        return f"f(x) = {a} * X^2 + {b} * X"  

    
def derivation(a, b, c):
    a2 = a*2
    if a == 0 and b == 0:
        return f"f'(x) = 0"
    elif a != 0 and b == 0:
        return f"f'(x) = {a2} * X"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    elif a != 0 and b != 0:
        return f"f'(x) = {a2} * X + {b}" 
