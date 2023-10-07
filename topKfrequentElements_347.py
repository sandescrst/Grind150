def topKfreqElement(nums, k):
    hashMap = {}
    index_counter = [[] for i in range(len(nums)+1)]
    

    for i in nums:
        hashMap[i] = 1+ hashMap.get(i,0)
    for k,v in hashMap.items():
        index_counter[v].append(k)
    # print(index_counter)
    res = []

    for i in range(len(index_counter)-1,0,-1):
        # print(i)
            for n in index_counter[i]:
                res.append(n)
            # print(res)
                if len(res) == k:
                  print(res)
                  return res
                # print(res)
                

    # return res
print(topKfreqElement([1,2,2,1,4,4,5],2))