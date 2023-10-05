def twoSum(nums, target):
    s = 0
    hashMap = {} 
    for i, n in enumerate(nums):
        s = target - n
        print(s)
        if s not in hashMap:
            hashMap[n] = i
        else:
            return [i, hashMap[s]]
print(twoSum([2,7,11,15],9))