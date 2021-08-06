class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    
    def add_money(self, deposit_dollars, deposit_cents):    
        self.dollars = self.dollars + deposit_dollars
        self.cents = self.cents + deposit_cents
        if self.cents == 100:
            self.dollars += 1
            self.cents = 0
        elif self.cents > 100:
            self.dollars = self.dollars + self.cents // 100
            self.cents = self.cents % 100
