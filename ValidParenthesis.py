def valid(s):
    hashMap = {")": "(", "}":"{", "]": "["}
    mystack = []

    for i in s:
        if i in hashMap:
            if mystack and  hashMap[i] == mystack[-1]:
                print(mystack)
                mystack.pop()
            else:
                return False
        else:
            mystack.append(i)
    return True if len(mystack) == 0 else False

print(valid("({[]})"))

# a = {1:3, 4:8}
a = [1,2,3]
b= a.remove(a[-1])
print(a)