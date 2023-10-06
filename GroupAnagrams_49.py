from collections import defaultdict


def groupAnagram(strs):
    res = defaultdict(list)
    print(res)
    for i in strs:
        count = [0] * 26 
        for j in i:
            print(j)
            count[ord(j) - ord("a")] += 1
            print(count)
        res[tuple(count)].append(i)
        print(res)
    return res.values()
print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))