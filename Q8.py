import math
def kFactor(n, k):
    if (k>n): return -1
    st1=[]
    st2=[]
    count=0
    for f in range(1,int(math.sqrt(n)+1)):
        if (n%f==0):
            st1.append(f)
            st2.append(n//f)
            count += 2
    st2.reverse()
    return (st1+st2)[k-1] if (count>=k) else -1

if (__name__=="__main__"):
    testcases = [[12, 3] , [1, 1] , [12, 6] , [12, 7] , [36, 5]]
    for t in testcases:
        print(kFactor(t[0], t[1]))

