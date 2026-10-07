import math
def isPrime(n):
    if (n==1): return False
    for f in range(2, int(math.sqrt(n)+1)):
        if (n%f==0):
            return False
    return True

def nextPrime(n):
    k=n+1
    while (not isPrime(k)):
        k += 1
    return k

if (__name__=="__main__"):
    testcases = [14, 0, 1, 2, 17]
    for t in testcases:
        print(nextPrime(t))

