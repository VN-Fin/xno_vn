
# Example 1: Creating a Stock Trading Strategy with `xno-cli`

This tutorial demonstrates how to create a simple stock trading strategy using `xno-cli`. Make sure you have the `xno-cli` tool installed.

To bootstrap a sample strategy, open a terminal and run the following command:

```bash
xno-cli create \
    --type stock \
    --ticker SHB \
    --resolution D \
    --from 2020-01-01 \
    --to 2025-07-04 \
    --init-cash 500000000 \
    --slippage 0.05 \
    --name "My SHB Algorithm"
```

This command will create a new directory with the following structure:

```bash
├── strategies
│   └── my_shb_algorithm.py
```

The `my_shb_algorithm.py` file contains the basic structure of a stock trading algorithm. You can customize it to implement your own trading logic.

Here's an example of the generated strategy:

```python
# strategies/my_shb_algorithm.py
from xno.algo.st import StockAlgorithm

class MyAlgorithm(StockAlgorithm):
    def __setup__(self):
        self._name = "My SHB Algorithm"
        self._ticker = "SHB"
        self._resolution = "D"
        self._from_time = "2020-01-01"
        self._to_time = "2025-07-04"
        self._init_cash = 500_000_000
        self._slippage = 0.05

    def __algorithm__(self):
        # Indicators
        rsi = self._features.rsi()
        adx = self._features.adx()

        # Generate buy signal when RSI is rising and ADX is falling
        buy_signal = (self.current(rsi) > self.previous(rsi)) & \
                     (self.current(adx) < self.previous(adx))
        
        # Or using self.And instead of & conditional
        # Generate sell signal when RSI is falling and ADX is rising
        sell_signal = self.And(
            self.current(rsi) < self.previous(rsi),
            self.current(adx) > self.previous(adx)
        )

        self.buy(buy_signal, quantity=1)
        self.sell(sell_signal, quantity=1)

if __name__ == "__main__":
    algo = MyAlgorithm()
    algo.run()
    algo.visualize()
    print("Algorithm run completed.")
```

You can modify the `__algorithm__` method to implement your own strategy logic. In this example, RSI and ADX indicators are used to determine buy and sell signals.

Feel free to experiment and adapt the logic to fit your trading ideas.
