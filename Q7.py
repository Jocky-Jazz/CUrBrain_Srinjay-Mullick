def gcd(q:int, d:int) -> int:
    while (q!=0):
        d, q = q, d%q
    return d

def gcdAll(testcase):
    res=testcase[0]
    for n in testcase:
        res = gcd(res, n)
    return res

if (__name__=="__main__"):
    testcases = [[24, 36, 48] , [33, 44, 55, 66] , [17] , [12, 18, 24, 30] , [1, 7, 14, 28]]
    for t in testcases:
        print(gcdAll(t))
