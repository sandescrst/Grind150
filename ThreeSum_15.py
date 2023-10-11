def threeSum(nums):
    res = []
    i = 0
    nums.sort()
    if len(nums) ==3:
        res.append(nums)
        return nums
    if len(nums) <= 2:
        return res
    for a,i in enumerate(nums):
        if  a >0 and i == nums[a-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            if nums[i]+ nums[l] +nums[r] > 0:
                r -=1
            elif nums[i]+ nums[l] +nums[r] < 0:
                l +=1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l +=1
                while nums[l] == nums[l-1] and l <r:
                    l +=1
    return res

print(threeSum([-1,0,1,2,-1,-4]))