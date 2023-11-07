class Company:
    """Represents an individual company listed on our exchange"""

    def __init__(self, symbol, name, sector, description, market_cap, beta, volume, 
                 shares_outstanding, year_high, year_low, bid, ask, last_close_price, price,
                 open_interest, delta, gamma, theta, vega, rho) -> None:
        # Identifiers
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.description = description
        
        # Stock price related
        self.price = price
        self.market_cap = market_cap
        self.beta = beta
        self.volume = volume
        self.shares_outstanding = shares_outstanding
        self.year_high = year_high
        self.year_low = year_low
        self.bid = bid
        self.ask = ask
        self.last_close_price = last_close_price
        
        # Calculated properties
        self.bid_ask_spread = ask - bid
        
        # Greeks, for options related data
        self.open_interest = open_interest
        self.delta = delta
        self.gamma = gamma
        self.theta = theta
        self.vega = vega
        self.rho = rho

    def __str__(self) -> str:
        """Generates format when calling the stock object as a string"""
        return (f"{self.name} ({self.symbol}) - Sector: {self.sector}\n"
                f"Description: {self.description}\n"
                f"Market Cap: ${self.market_cap:.2f}, Beta: {self.beta}\n"
                f"Volume: {self.volume}, Shares Outstanding: {self.shares_outstanding}\n"
                f"52 Week High: ${self.year_high:.2f}, 52 Week Low: ${self.year_low:.2f}\n"
                f"Bid: ${self.bid:.2f}, Ask: ${self.ask:.2f}, Last Close Price: ${self.last_close_price:.2f}\n"
                f"Bid-Ask Spread: ${self.bid_ask_spread:.2f}\n"
                f"Greeks - Open Interest: {self.open_interest}, Delta: {self.delta}, "
                f"Gamma: {self.gamma}, Theta: {self.theta}, Vega: {self.vega}, Rho: {self.rho}")
