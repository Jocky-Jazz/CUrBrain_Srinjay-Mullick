def merge(nums1, nums2):
    n = len(nums2)
    m = len(nums1)-n
    p1, p2, x = m-1, n-1, m+n-1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[x] = nums1[p1]
            p1 = p1 - 1
        else:
            nums1[x] = nums2[p2]
            p2 = p2 - 1
        x = x - 1
    while p2 >= 0:
        nums1[x] = nums2[p2]
        p2 = p2 - 1
        x  = x - 1
    return nums1

if __name__=="__main__":
    print(merge([1,2,3,0,0,0], [2,5,6]))
    print(merge([0],[1]))
    print(merge([1],[]))
    print(merge([4,5,6,0,0,0],[1,2,3]))
    print(merge([1,3,5,0,0],[2,4]))
