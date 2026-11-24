def runningSum(arr):
    rSum=[]
    for j, n in enumerate(arr):
        for i in range(len(rSum)):
            if (rSum[i][0]==j-1):
                rSum.append((j,rSum[i][1]+n))
        rSum.append((j,n))
    minim=rSum[0][1]
    for n in rSum:
        minim = n[1] if n[1]<minim else minim
    return minim

if __name__=="__main__":
    testcases=[[3,-4,2,-3,5], [1,2,3], [-1,-2,-3], [5], [4,-1,-2,1,-5,3]]
    for t in testcases:
        print(runningSum(t))
