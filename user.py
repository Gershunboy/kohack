class User:
    def __init__(self, name, password, id):
        self.name = name
        self.password = password
        self.id = id
        self.money = 1000
        self.stocks = {}
    def buy_stock(self, stock, amt, price):
        cost = amt*price
        if cost <= self.money:
            self.money -= cost
            if stock in self.stocks:
                self.stocks[stock] += amt
            else:
                self.stocks.append(stock, amt)
            return (True)
        else:
            return(False)

    def sell_stock(self, stock, amt, price):
        if amt <= self.stocks[stock]:
            money = price*amt
            self.money += money
            if amt == self.stocks[stock]:
                self.stocks.pop[stock]
            else:
                self.stocks[stock] -= amt
            return True
        else:
            return False
    def name(self):
        return (self.name)
    def password(self):
        return (self.password)
    def id(self):
        return (self.id)