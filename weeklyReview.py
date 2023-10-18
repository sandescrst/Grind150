def duplicate(nums):
    hashSet = set()

    for i in nums:
        if i  not in hashSet:
            hashSet.add(i)
        else:
            return True
    return False

# print(duplicate([1,3,4,5]))

