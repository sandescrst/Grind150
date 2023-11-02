def minimum(nums):
    l,r = 0, len(nums)-1
    res = nums[l]
    if nums[l] <= nums[r]:
        res = min(res, nums[l])
        return res

    while l <= r:
        mid = (l+r)//2
        print(mid)
        res = min(res, nums[mid])

        if nums[r] <= nums[mid]:
            l = mid+1
        else:
            r = mid -1
    return res

print(minimum([4,5,6,7,0,1,2,3]))