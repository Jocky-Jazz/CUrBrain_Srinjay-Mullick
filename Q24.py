def runningSum(arr, target):
    if not arr: return 0
    rSum=[]
    for j, n in enumerate(arr):
        for i in range(len(rSum)):
            if (rSum[i][0]==j-1):
                rSum.append((j,rSum[i][1]+n,rSum[i][2]+1))
        rSum.append((j,n,1))
    minim=(0,0,0)
    for n in rSum:
        minim = n if n[1]>=target and (minim[1]==0 or n[2]<minim[2]) else minim
    return minim[2]

if __name__=="__main__":
    testcases=[([2,3,1,2,4,3],7), ([1,1,1],10), ([5],5), ([1,2,3,4,5],11), ([],3)]
    for t in testcases:
        print(runningSum(*t))
