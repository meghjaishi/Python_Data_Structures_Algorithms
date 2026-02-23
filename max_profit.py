def max_profit(prices):
    """
    Given a list of stock prices, returns the maximum profit that can be achieved by buying and selling once.
    
    :param prices: List of stock prices where prices[i] is the price on day i.
    :return: Maximum profit that can be achieved.
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

if __name__ == "__main__":
    # Example usage
    stock_prices = [7, 1, 5, 3, 6, 4]
    print(f"Maximum profit: {max_profit(stock_prices)}")