prices = [7, 1, 5, 3, 6, 4]

min_price = prices[0]
global_max = 0

for i in range(len(prices)):
    curr_profit = prices[i] - min_price
    global_max = max(global_max, curr_profit)
    min_price = min(min_price, prices[i])

print(global_max)