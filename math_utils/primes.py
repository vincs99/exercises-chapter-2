import math
def isprime(n):
    k=2
    if n<2:
        return False
    else:
        while k <= math.sqrt(n) :
            if n % k == 0 :
                return False
            else:
                k=k+1
        return True
    

