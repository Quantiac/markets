

class Company:
    """Represents an individual company listed on our exchange"""

    def __init__(self, symbol, name, price) -> None:
        self.symbol = symbol
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """Generates format when calling the stock object as a string"""
        return f"{self.name} ({self.symbol}): ${self.price:.2f}"


class Portfolio:
    """All traders will have a portfolio that represents their net asset values."""

    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol] += quantity
        else:
            self.stocks[stock.symbol] = quantity

    def remove_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            if self.stocks[stock.symbol] >= quantity:
                self.stocks[stock.symbol] -= quantity

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.stocks.items():
            stock = stock_market.get_stock(symbol)
            if stock:
                total_value += stock.price * quantity
        return total_value


class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def get_stock(self, symbol):
        if symbol in self.stocks:
            return self.stocks[symbol]
        else:
            print(f"Stock with symbol {symbol} not found in the market.")


# Usage example
if __name__ == "__main__":
    stock_market = StockMarket()

    schwab = Company("SCHW", "Charles Schwab, Inc", 52.2)

    stock_market.add_stock(schwab)

    my_portfolio = Portfolio()
    my_portfolio.add_stock(schwab, 5)

    print(f"My Portfolio Value: ${my_portfolio.get_portfolio_value():.2f}")
