def highestfreq (sales):
    hashmap = {}
    maxfreq = 0
    winsale = 0
    for s in sales:
        if hashmap.get(s, 0)==0:
            hashmap[s]=1
        else:
            hashmap[s]+=1
    for s, f in hashmap.items():
        if maxfreq<f:
            winsale, maxfreq = s, f
        elif maxfreq==f:
            winsale = min(s, winsale)
    return winsale

if __name__=="__main__":
    testcases = [[101,103,101,102,103,105,101,103], [5,5,5,2,2,2,2], [99], [-2,-2,3,3,0], [4,1,4,1,7]]
    for t in testcases:
        print(highestfreq(t))