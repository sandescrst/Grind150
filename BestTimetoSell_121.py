def bestTime(prices):

    i,j = 0,1  # i = buy, j = sell

    profit = 0

    while j <len(prices) :
        if prices[i] > prices[j]:
            i = j
            # print(i)
        else:
            # print(prices[j] - prices[i])
            profit = max(profit, prices[j]- prices[i])
            # print(profit)
        j +=1
    return profit

print(bestTime([7,1,5,3,6,4]))