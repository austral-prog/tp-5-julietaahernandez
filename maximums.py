def max_of_two(x, y):
    if x > y: 
        return x
    else: 
        return y 

def max_of_three(x, y, z):
    if x > y > z:
        return x 
    elif x < y < z:
        return z
    elif x > y < z:
        return z 
    else:
        return y 
