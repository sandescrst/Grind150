def trapWater(height):
    l,r = 0, len(height)-1
    res = 0
    leftMax, rightMax = height[l], height[r]
    # temp = 0

    while l < r:
        if leftMax <= rightMax:
            l +=1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
            # print(res)
        else:
            r -=1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]


    return res

print(trapWater([0,1,0,2,1,0,1,3,2,1,2,1]))