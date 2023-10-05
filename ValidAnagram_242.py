def ValidAnagram(s,t) :
    hashmap1 = {}
    hashmap2 = {}
    if len(s) < len(t):
        return False 
    for i in s:
        if i in hashmap1:
            hashmap1[i] += 1

        else:
            hashmap1[i] = 1

    for i in t:
        if i in hashmap2:
            hashmap2[i] += 1
        else:
            hashmap2[i] = 1

    for k,v in hashmap2.items():
        if hashmap2.get(k,0) >= hashmap1[k]:

                print(hashmap2[k])
                return False
    return True
print(ValidAnagram("aabdm", "adme"))  
