def secLargest(testcases):
    a_set, b_set = False, False
    for n in testcases:
        if (not a_set):
            a, a_set = n, True
        else:
            if (n>a):
                b, a, b_set = a, n, True
            elif (a>n and ((not b_set) or n>b)):
                b, b_set = n, True
    return b if b_set else -1

if (__name__=="__main__"):
    testcases = [[50,40,50,30], [100,100,100], [], [10,20,30,40], [5,5,4,4,3]]
    for t in testcases:
        print(secLargest(t))

