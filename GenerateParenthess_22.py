def generateParenthess(n):
    # always start with open parenthesis and end with close parenthesis
    #count of the open parenthesis should always be greater than close parenthesis
    #return if open parenthesis== close parenthesis== n

    stack = []
    res = []

    def backtracking(openP, closedP):

        if openP == closedP == n:
            print("Final",stack)
            res.append("".join(stack))
            return res
        if openP > closedP:
            stack.append(")")
            # print(stack)
            backtracking(openP, closedP+1)
            stack.pop()
            
        if  openP <n:
            stack.append("(")
            backtracking(openP+1, closedP)
            stack.pop()

    backtracking(0,0)
    return res


print(generateParenthess(3))