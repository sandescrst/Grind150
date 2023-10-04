def containDuplicate(nums):
    unique = {}
    c = 0
    d = 0
    for i in nums:
        if i in unique:
            unique[i] +=1
        else:
            unique[i] = 1
    print(unique)
    for k,v in unique.items():
        c +=1
        d +=v
    return True if d > c else False
## Using hashSet
    myset = set()

    for i in nums:
        if i in myset:
            return True
        myset.add(i)
    return False
print(containDuplicate([2,14,18,22]))
