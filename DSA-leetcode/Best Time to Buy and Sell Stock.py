def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))


####################################################################

def best_time_to_buy_and_sell(prices):
    if not prices:
        return 0, -1, -1  # No prices

    min_price = prices[0]
    min_day = 0
    max_profit = 0
    buy_day = sell_day = 0

    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            buy_day = min_day
            sell_day = i

        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i

    if max_profit == 0:
        print("No profit can be made.")
    else:
        print(f"Buy on day {buy_day} at price {prices[buy_day]}")
        print(f"Sell on day {sell_day} at price {prices[sell_day]}")
        print(f"Maximum Profit = {max_profit}")
        
    return max_profit, buy_day, sell_day

# Example
prices = [7, 1, 5, 3, 6, 4]
best_time_to_buy_and_sell(prices)
