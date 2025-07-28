# List of TA & Functions

## Technical Indicators
### AD - A/D Line 
Calculates the Chaikin Accumulation/Distribution Line.

```
xno.TimeseriesFeatures.ad(high=None, low=None, close=None, volume=None)
```
or 
```python
xno.AD(high, low, close, volume)
```
- Example:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ad()
```
- Example:
```python
from xno import AD

f = AD(df['high'], df['low'], df['close'], df['volume'])
```
### ADOSC - A/D Oscillator
### ADX	- Average Directional Movement Index
### ADXR - Average Directional Movement Index Rating
### APO - Absolute Price Oscillator
### AROON - Aroon
### AROONOSC - Aroon Oscillator
### ATR	- Average True Range
### AVGPRICE - Average Price
### BBANDS	- Bollinger Bands
### BETA	- Beta
### BOP	- Balance Of Power
### CCI	- Commodity Channel Index
### CMO	- Chande Momentum Oscillator
### CORREL	- Pearson's Correlation Coefficient ®
### DEMA	- Double Exponential Moving Average
### DX	- Directional Movement Index
### EMA	- Exponential Moving Average
### DCPERIOD - Dominant Cycle Period
### DCPHASE - Dominant Cycle Phase
### PHASOR - Phasor Components
### SINE - SineWave
### TRENDLINE - Instantaneous Trendline
### TRENDMODE - Trend vs Cycle Mode
### KAMA	- Kaufman Adaptive Moving Average
### LINEARREG	- Linear Regression
### LINEARREG_ANGLE	- Linear Regression Angle
### LINEARREG_INTERCEPT	- Linear Regression Intercept
### LINEARREG_SLOPE	- Linear Regression Slope
### MA	- Moving Average
### MACD	- Moving Average Convergence/Divergence
### MACDEXT	- MACD with controllable MA type
### MACDFIX	- Moving Average Convergence/Divergence Fix 12/26
### MAMA	- MESA Adaptive Moving Average
### MAX	- Highest value over a specified period
### MAXINDEX	- Index of highest value over a specified period
### MEDPRICE	- Median Price
### MFI	- Money Flow Index
### MIDPOINT	- MidPoint over period
### MIDPRICE	- Midpoint Price over period
### MIN	- Lowest value over a specified period
### MININDEX	- Index of lowest value over a specified period
### MINMAX	- Lowest and highest values over a specified period
### MINMAXINDEX	- Indexes of lowest and highest values over a specified period
### MINUS_DI	- Minus Directional Indicator
### MINUS_DM	- Minus Directional Movement
### MOM	- Momentum
### NATR	- Normalized Average True Range
### OBV	- On Balance Volume
### PLUS_DI	- Plus Directional Indicator
### PLUS_DM	- Plus Directional Movement
### PPO	- Percentage Price Oscillator
### ROC	- Rate of change : ((price/prevPrice)-1)*100
### ROCP	- Rate of change Percentage: (price-prevPrice)/prevPrice
### ROCR	- Rate of change ratio: (price/prevPrice)
### ROCR100	- Rate of change ratio 100 scale: (price/prevPrice)*100
### RSI	- Relative Strength Index
### SAR	- Parabolic SAR
### SAREXT	- Parabolic SAR - Extended
### SMA	- Simple Moving Average
### STDDEV	- Standard Deviation
### STOCH	- Stochastic
### STOCHF	- Stochastic Fast
### STOCHRSI	- Stochastic Relative Strength Index
### SUM	- Summation
### T3	- Triple Exponential Moving Average (T3)
### TEMA	- Triple Exponential Moving Average
### TRANGE	- True Range
### TRIMA	- Triangular Moving Average
### TRIX	- 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
### TSF	- Time Series Forecast
### TYPPRICE	- Typical Price
### ULTOSC	- Ultimate Oscillator
### VAR	- Variance
### WCLPRICE	- Weighted Close Price
### WILLR	- Williams' %R
### WMA	- Weighted Moving Average

## Chart Patterns
### CDL2CROWS	- Two Crows
### CDL3BLACKCROWS	- Three Black Crows
### CDL3INSIDE	- Three Inside Up/Down
### CDL3LINESTRIKE	- Three Outside Up/Down
### CDL3STARSINSOUTH	- Three Stars In The South
### CDL3WHITESOLDIERS	- Three Advancing White Soldiers
### CDLABANDONEDBABY	- Abandoned Baby
### CDLADVANCEBLOCK	- Advance Block
### CDLBELTHOLD	- Belt-Hold
### CDLBREAKAWAY	- Breakaway
### CDLCLOSINGMARUBOZU	- Closing Marubozu
### CDLCONCEALBABYSWALL	- Concealing Baby Swallow
### CDLCOUNTERATTACK	- Counterattack
### CDLDARKCLOUDCOVER	- Dark Cloud Cover
### CDLDOJI	Doji
### CDLDOJISTAR	- Doji Star
### CDLDRAGONFLYDOJI	- Dragonfly Doji
### CDLENGULFING	- Engulfing Pattern
### CDLEVENINGDOJISTAR	- Evening Doji Star
### CDLEVENINGSTAR	- Evening Star
### CDLGAPSIDESIDEWHITE	- Up/Down-gap side-by-side white lines
### CDLGRAVESTONEDOJI	- Gravestone Doji
### CDLHAMMER	- Hammer
### CDLHANGINGMAN	- Hanging Man
### CDLHARAMI	- Harami Pattern
### CDLHARAMICROSS	- Harami Cross Pattern
### CDLHIGHWAVE	- High-Wave Candle
### CDLHIKKAKE	- Hikkake Pattern
### CDLHIKKAKEMOD	- Modified Hikkake Pattern
### CDLHOMINGPIGEON	- Homing Pigeon
### CDLIDENTICAL3CROWS	- Identical Three Crows
### CDLINNECK	- In-Neck Pattern
### CDLINVERTEDHAMMER	- Inverted Hammer
### CDLKICKING	- Kicking
### CDLKICKINGBYLENGTH	- Kicking - bull/bear determined by the longer marubozu
### CDLLADDERBOTTOM	- Ladder Bottom
### CDLLONGLEGGEDDOJI	- Long Legged Doji
### CDLLONGLINE - 	Long Line Candle
### CDLMARUBOZU	- Marubozu
### CDLMATCHINGLOW	- Matching Low
### CDLMATHOLD	- Mat Hold
### CDLMORNINGDOJISTAR	- Morning Doji Star
### CDLMORNINGSTAR	- Morning Star
### CDLONNECK	- On-Neck Pattern
### CDLPIERCING	- Piercing Pattern
### CDLRICKSHAWMAN	- Rickshaw Man
### CDLRISEFALL3METHODS	- Rising/Falling Three Methods
### CDLSEPARATINGLINES	- Separating Lines
### CDLSHOOTINGSTAR	- Shooting Star
### CDLSHORTLINE	- Short Line Candle
### CDLSPINNINGTOP	- Spinning Top
### CDLSTALLEDPATTERN	- Stalled Pattern
### CDLSTICKSANDWICH	- Stick Sandwich
### CDLTAKURI	- Takuri (Dragonfly Doji with very long lower shadow)
### CDLTASUKIGAP	- Tasuki Gap
### CDLTHRUSTING	- Thrusting Pattern
### CDLTRISTAR	- Tristar Pattern
### CDLUNIQUE3RIVER	- Unique 3 River
### CDLUPSIDEGAP2CROWS	- Upside Gap Two Crows
### CDLXSIDEGAP3METHODS	- Upside/Downside Gap Three Methods

## Math Functions
### ACOS         -        Vector Trigonometric ACos
### ADD          -        Vector Arithmetic Add
### ASIN         -        Vector Trigonometric ASin
### ATAN         -        Vector Trigonometric ATan
### CEIL         -        Vector Ceil
### COS          -        Vector Trigonometric Cos
### COSH         -        Vector Trigonometric Cosh
### DIV          -        Vector Arithmetic Div
### EXP          -        Vector Arithmetic Exp
### FLOOR        -        Vector Floor
### LN           -        Vector Log Natural
### LOG10        -        Vector Log10
### MAX          -        Highest value over a specified period
### MAXINDEX     -        Index of highest value over a specified period
### MIN          -        Lowest value over a specified period
### MININDEX     -        Index of lowest value over a specified period
### MINMAX       -        Lowest and highest values over a specified period
### MINMAXINDEX  -        Indexes of lowest and highest values over a specified period
### MULT         -        Vector Arithmetic Mult
### SUB          -        Vector Arithmetic Subtraction
### SUM          -        Summation
### SIN          -        Vector Trigonometric Sin
### SINH         -        Vector Trigonometric Sinh
### SQRT         -        Vector Square Root
### TAN          -        Vector Trigonometric Tan
### TANH         -        Vector Trigonometric Tanh


## Smart Money Concepts

## Rolling Window Functions

