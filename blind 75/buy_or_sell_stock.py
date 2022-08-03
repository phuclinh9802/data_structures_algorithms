def buy_sell(prices):
    res = 0
    buy, sell = 0, 1

    while sell < len(prices):
        # get current profit
        tmp = prices[sell] - prices[buy]

        if prices[sell] > prices[buy]:
            # update result max
            res = max(res, tmp)

        # if it's a loss
        if prices[sell] < prices[buy]:
            # update buy price = sell price
            buy = sell

        sell += 1

    return res