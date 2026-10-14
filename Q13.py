def runningSum(nums, k):
    k = k if k>=0 else -k
    runSum = 0
    for n in nums:
        runSum += n
        if (runSum%k == 0):
            return True
    return False

if (__name__=="__main__"):
    testcases = [([4,2,9], 3), ([1,2,4], 5), ([5], 5), ([0,1], 7), ([-2, 2, 1],3)]
    for t in testcases:
        print(runningSum(*t))

