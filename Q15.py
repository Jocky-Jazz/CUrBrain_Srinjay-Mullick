def smallestAbs(testcases):
    res = testcases[0]
    for n in testcases:
        if (abs(n)<abs(res)):
            res = n
    return res

if (__name__=="__main__"):
    testcases = [[10,-5,-2,4,2], [-3,3], [0,-1,1], [7,-7,4], [5,-2,2,-1]]
    for t in testcases:
        print(smallestAbs(t))

