# examples/strategy.py
from xno.algo.st import StockAlgorithm


class MyAlgorithm(StockAlgorithm):
    def __setup__(self):
        self.name = "My SHB Algorithm"
        self.ticker = "SHB"
        self.resolution = "D"
        self.from_time = "2020-01-01"
        self.to_time = "2025-07-04"
        self.init_cash = 500_000_000

    def __algorithm__(self):
        # Indicators
        rsi = self.features.rsi()
        adx = self.features.adx()

        # The logical AND operator can be used directly by using `&` or `self.And()`
        buy_signal = (self.current(rsi) > self.previous(rsi)) & (self.current(adx) < self.previous(adx))

        # you can also use `self.And()` for logical AND
        sell_signal = self.And(self.current(rsi) < self.previous(rsi), self.current(adx) > self.previous(adx))

        # Set the buy and sell signals
        self.buy(buy_signal, 1)
        self.sell(sell_signal, 1)

if __name__ == "__main__":
    algo = MyAlgorithm()
    algo.run()
    algo.visualize()
    print("Algorithm run completed.")
