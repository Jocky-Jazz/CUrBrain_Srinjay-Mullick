def closestSum(arr, target):
    res = tuple()
    if len(arr)<=1: return res
    diff=0
    i, j = 0, len(arr)-1
    while i<j:
        if (arr[i]+arr[j]==target): return (arr[i],arr[j])
        else:
            h = abs(arr[i]+arr[j]-target)
            if (diff==0 or h<diff):
                diff, res = h, (arr[i],arr[j])
            if (arr[i]+arr[j]<target): i+=1
            else: j-=1
    return res


if __name__=="__main__":
    testcases=[([10,22,28,29,30,40],54), ([1,3,5,9],8), ([1,2],100), ([-4,-1,2,6],3), ([10,20,30],5)]
    for t in testcases:
        print(closestSum(*t))
