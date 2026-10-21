def tFilter(sales, threshold):
    return [n for n in sales if n>=threshold]

if (__name__=="__main__"):
    testcases = [([150,80,200,90,300], 100), ([100, 50, 100], 100), ([], 50), ([10,20,30], 40), ([75,75,75], 75)]
    for t in testcases:
        print(tFilter(*t))

