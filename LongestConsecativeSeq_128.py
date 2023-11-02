def longSeq(nums):

    numSet = set(nums)
    longest = 0

    for i in nums:
        if i-1 not in numSet:
            curr = 0
            while (i+curr) in numSet:
                curr +=1

            longest = max(longest, curr)

    return longest

print(longSeq([100,4,200,1,3,2,5]))

