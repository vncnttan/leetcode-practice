def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    buy_price = 0
    sell_price = 0
    idx = 0

    while idx < len(prices)-1:
        if prices[idx] < prices[idx+1]:
            # Nice time to buy
            buy_price = prices[idx]
            print(f"Buying {buy_price}")
            idx += 1

            while idx < len(prices)-1 and prices[idx] < prices[idx+1]:
                idx += 1

            # Nice time to sell
            sell_price = prices[idx]
            print(f"Selling {sell_price}")
            max_profit += sell_price - buy_price
            idx -= 1

        idx += 1
    return max_profit

prices = [7,6,4,3,1]
out = maxProfit(prices)
print(out)