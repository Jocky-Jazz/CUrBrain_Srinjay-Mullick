def delVal(arr, val):
    f=0
    if (len(arr)==0): return arr
    for i in range(len(arr)):
        if (f==0 and arr[i]==val): f=1
        elif (f==1): arr[i-1] = arr[i]
    return arr if f==0 else arr[:-1]

if __name__=="__main__":
    testcases=[([10, 20, 30, 20, 40],20), ([5,15],99), ([7],7), ([],3), ([4,4,4],4)]
    for t in testcases:
        print(delVal(*t))