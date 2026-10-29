def revbyIndex(nums, start, end):
    if (start<0 or end >= len(nums)):
        print("ERROR")
        return nums
    while (start<end):
        nums[start], nums[end] = nums[end], nums[start]
        start +=1
        end -=1
    return nums

if __name__=="__main__":
    testcases=[([10,20,30,40,50,60], 1, 4), ([1,2,3,4], 0, 3), ([7], 0, 0), ([1,2,3,4,5], 2, 4), ([1,2,3,4,5], 0, 2)]
    for t in testcases:
        print(revbyIndex(*t))
