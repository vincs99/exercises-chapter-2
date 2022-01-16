import math
def isprime(n):
    m=2
    if n<2:
        return False
    else:
        while m <= math.sqrt(n) :
            if n % m == 0 :
                return False
            else:
                m=m+1
        return True
    

