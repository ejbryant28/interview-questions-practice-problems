
def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    
    fact = factorial(n)
    zs = zeros(fact)
    
    return zs
    


def factorial(n):
    
    if n < 1:
        
        return 0
    
    elif n == 1:
        
        return 1
    
    else:
        
        return factorial(n-1) * n

    
def zeros(f, z=0):
    
    if f % 10 == 0:

        new = int(f/10)
        
        return zeros(new, z + 1)
    
    return z


print(trailingZeroes(3))
print(trailingZeroes(5))
