

import math
def sumArr(testcase):
    s = 0
    div = 10**9+7
    for n in testcase:
        s = (s+n%div)%div
    return s

if (__name__=="__main__"):
    testcases = [[1000000000, 1000000000, 1000000000] , [1, 2, 3, 4] , [] , [1000000007] , [0, 0, 0]]
    for t in testcases:
        print(sumArr(t))

