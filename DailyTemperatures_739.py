#In this problem we use MONOtonic decreasing order Stack

def dailyTemp(temperatures):
    res = [0] * len(temperatures)
    stack = [] #[index, temp]

    for i,t in enumerate(temperatures):
        while stack and t> stack[-1][1]:
            stackI, stackT= stack.pop()
            res[stackI] = (i-stackI)
            # print(stack)
        stack.append([i,t])
        # print(stack)

    return res

print(dailyTemp([73,74,75,71,69,72,76,73]))