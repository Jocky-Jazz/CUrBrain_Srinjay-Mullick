def replace_dig(n):
    res = []
    if (n<0):
        print("Invalid input: negative integers.")
        return 0
    while (n>0):
        res.append(0 if n%2==0 else n%10)
        n//=10
    res.reverse()
    return res

if (__name__=="__main__"):
    testcases = [258, 12345, 2468, 13579, 1002]
    for t in testcases:
        print(replace_dig(t));

