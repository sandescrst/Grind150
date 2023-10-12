def mostWater(height):

    l,r = 0, len(height)-1
    max_area = 0
    while l<r:
        ar = min(height[l], height[r]) * (r-l)
        max_area = max(max_area, ar)
        if height[l] >= height[r]:
            r -= 1
        
        else:
            l +=1
    return max_area

print(mostWater([1,8,6,2,5,4,8,3,7]))