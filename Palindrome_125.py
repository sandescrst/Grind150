def Palindrome(s):
    l,r = 0, len(s)-1

    while l<r:
        while l <r and not checkAlpanum(s[l]):
            l = l+1
        while r>l and not checkAlpanum(s[r]):
            r = r -1
        if s[l].lower() != s[r].lower():
            return False
        l,r = l+1, r-1
    return True

def checkAlpanum(c):
    return (ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9") or ord("a") <= ord(c) <= ord("z"))



print(Palindrome("A man, a plan, a canal: Panama"))