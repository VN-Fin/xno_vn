## Technical Indicators
### AD - A/D Line 
Calculates the Chaikin Accumulation/Distribution Line.

```python
xno.TimeseriesFeatures.ad(high=None, low=None, close=None, volume=None)
```
or 
```python
xno.AD(high, low, close, volume)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ad()
```
- Example XNO's TA usage:
```python
from xno import AD

f = AD(df['high'], df['low'], df['close'], df['volume'])
```
### ADOSC - A/D Oscillator
Calculates the Chaikin A/D Oscillator.

```python
xno.TimeseriesFeatures.adosc(high=None, low=None, close=None, volume=None, fastperiod=3, slowperiod=10)
```
or 
```python
xno.ADOSC(high, low, close, volume, fastperiod, slowperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.adosc()
```
- Example XNO's TA usage:
```python
from xno import ADOSC

f = ADOSC(df['high'], df['low'], df['close'], df['volume'], 3, 10)
```
### ADX	- Average Directional Movement Index
Calculates the Average Directional Movement Index.

```python
xno.TimeseriesFeatures.adx(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.ADX(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.adx()
```
- Example XNO's TA usage:
```python
from xno import ADX

f = ADX(df['high'], df['low'], df['close'], 14)
```
### ADXR - Average Directional Movement Index Rating
Calculates the Average Directional Movement Index Rating.

```python
xno.TimeseriesFeatures.adxr(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.ADXR(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.adxr()
```
- Example XNO's TA usage:
```python
from xno import ADXR

f = ADXR(df['high'], df['low'], df['close'], 14)
```
### APO - Absolute Price Oscillator
Calculates the Absolute Price Oscillator.

```python
xno.TimeseriesFeatures.apo(series=None, fastperiod=12, slowperiod=26, matype=0)
```
or 
```python
xno.APO(series, fastperiod, slowperiod, matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.apo()
```
- Example XNO's TA usage:
```python
from xno import APO

f = APO(df['close'], 12, 26, 0)
```
### AROON - Aroon
Calculates the Aroon oscillator.

```python
xno.TimeseriesFeatures.aroon(high=None, low=None, timeperiod=14)
```
or 
```python
xno.AROON(high, low, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
aroondown, aroonup = f.aroon()
```
- Example XNO's TA usage:
```python
from xno import AROON

aroondown, aroonup = AROON(df['high'], df['low'], 14)
```
### AROONOSC - Aroon Oscillator
Calculates the Aroon Oscillator.

```python
xno.TimeseriesFeatures.aroonosc(high=None, low=None, timeperiod=14)
```
or 
```python
xno.AROONOSC(high, low, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.aroonosc()
```
- Example XNO's TA usage:
```python
from xno import AROONOSC

f = AROONOSC(df['high'], df['low'], 14)
```
### ATR	- Average True Range
Calculates the Average True Range.

```python
xno.TimeseriesFeatures.atr(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.ATR(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.atr()
```
- Example XNO's TA usage:
```python
from xno import ATR

f = ATR(df['high'], df['low'], df['close'], 14)
```
### AVGPRICE - Average Price
Calculates the Average Price.

```python
xno.TimeseriesFeatures.avgprice(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.AVGPRICE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.avgprice()
```
- Example XNO's TA usage:
```python
from xno import AVGPRICE

f = AVGPRICE(df['open'], df['high'], df['low'], df['close'])
```
### BBANDS	- Bollinger Bands
Calculates the Bollinger Bands.

```python
xno.TimeseriesFeatures.bbands(close=None, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
```
or 
```python
xno.BBANDS(close, timeperiod, nbdevup, nbdevdn, matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
upperband, middleband, lowerband = f.bbands()
```
- Example XNO's TA usage:
```python
from xno import BBANDS

upperband, middleband, lowerband = BBANDS(df['close'], 5, 2, 2, 0)
```
### BETA	- Beta
Calculates the Beta.

```python
xno.TimeseriesFeatures.beta(s1, s2, timeperiod=5)
```
or 
```python
xno.BETA(s1, s2, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.beta(df['close'], df['benchmark'], 5)
```
- Example XNO's TA usage:
```python
from xno import BETA

f = BETA(df['close'], df['benchmark'], 5)
```
### BOP	- Balance Of Power
Calculates the Balance Of Power.

```python
xno.TimeseriesFeatures.bop(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.BOP(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.bop()
```
- Example XNO's TA usage:
```python
from xno import BOP

f = BOP(df['open'], df['high'], df['low'], df['close'])
```
### CCI	- Commodity Channel Index
Calculates the Commodity Channel Index.

```python
xno.TimeseriesFeatures.cci(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.CCI(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cci()
```
- Example XNO's TA usage:
```python
from xno import CCI

f = CCI(df['high'], df['low'], df['close'], 14)
```
### CMO	- Chande Momentum Oscillator
Calculates the Chande Momentum Oscillator.

```python
xno.TimeseriesFeatures.cmo(series=None, timeperiod=14)
```
or 
```python
xno.CMO(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cmo()
```
- Example XNO's TA usage:
```python
from xno import CMO

f = CMO(df['close'], 14)
```
### CORREL	- Pearson's Correlation Coefficient ®
Calculates the Pearson's Correlation Coefficient.

```python
xno.TimeseriesFeatures.correl(s1, s2, timeperiod=30)
```
or 
```python
xno.CORREL(s1, s2, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.correl(df['close'], df['volume'], 30)
```
- Example XNO's TA usage:
```python
from xno import CORREL

f = CORREL(df['close'], df['volume'], 30)
```
### DEMA	- Double Exponential Moving Average
Calculates the Double Exponential Moving Average.

```python
xno.TimeseriesFeatures.dema(series=None, timeperiod=30)
```
or 
```python
xno.DEMA(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.dema()
```
- Example XNO's TA usage:
```python
from xno import DEMA

f = DEMA(df['close'], 30)
```
### DX	- Directional Movement Index
Calculates the Directional Movement Index.

```python
xno.TimeseriesFeatures.dx(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.DX(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.dx()
```
- Example XNO's TA usage:
```python
from xno import DX

f = DX(df['high'], df['low'], df['close'], 14)
```
### EMA	- Exponential Moving Average
Calculates the Exponential Moving Average.

```python
xno.TimeseriesFeatures.ema(series=None, timeperiod=30)
```
or 
```python
xno.EMA(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ema()
```
- Example XNO's TA usage:
```python
from xno import EMA

f = EMA(df['close'], 30)
```
### DCPERIOD - Dominant Cycle Period
Calculates the Dominant Cycle Period.

```python
xno.TimeseriesFeatures.dcperiod(close=None)
```
or 
```python
xno.DCPERIOD(close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.dcperiod()
```
- Example XNO's TA usage:
```python
from xno import DCPERIOD

f = DCPERIOD(df['close'])
```
### DCPHASE - Dominant Cycle Phase
Calculates the Dominant Cycle Phase.

```python
xno.TimeseriesFeatures.dcphase(close=None)
```
or 
```python
xno.DCPHASE(close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.dcphase()
```
- Example XNO's TA usage:
```python
from xno import DCPHASE

f = DCPHASE(df['close'])
```
### PHASOR - Phasor Components
Calculates the Phasor Components.

```python
xno.TimeseriesFeatures.phasor(close=None)
```
or 
```python
xno.PHASOR(close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
inphase, quadrature = f.phasor()
```
- Example XNO's TA usage:
```python
from xno import PHASOR

inphase, quadrature = PHASOR(df['close'])
```
### SINE - SineWave
Calculates the SineWave.

```python
xno.TimeseriesFeatures.sine(close)
```
or 
```python
xno.SINE(close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
sine, leadsine = f.sine()
```
- Example XNO's TA usage:
```python
from xno import SINE

sine, leadsine = SINE(df['close'])
```
### TRENDLINE - Instantaneous Trendline
Calculates the Instantaneous Trendline.

```python
xno.TimeseriesFeatures.ht_trendline(series=None)
```
or 
```python
xno.TRENDLINE(series)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ht_trendline()
```
- Example XNO's TA usage:
```python
from xno import TRENDLINE

f = TRENDLINE(df['close'])
```
### TRENDMODE - Trend vs Cycle Mode
Calculates the Trend vs Cycle Mode.

```python
xno.TimeseriesFeatures.trendmode(close=None)
```
or 
```python
xno.TRENDMODE(close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.trendmode()
```
- Example XNO's TA usage:
```python
from xno import TRENDMODE

f = TRENDMODE(df['close'])
```
### KAMA	- Kaufman Adaptive Moving Average
Calculates the Kaufman Adaptive Moving Average.

```python
xno.TimeseriesFeatures.kama(series=None, timeperiod=30)
```
or 
```python
xno.KAMA(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.kama()
```
- Example XNO's TA usage:
```python
from xno import KAMA

f = KAMA(df['close'], 30)
```
### LINEARREG	- Linear Regression
Calculates the Linear Regression.

```python
xno.TimeseriesFeatures.linearreg(s1, timeperiod=14)
```
or 
```python
xno.LINEARREG(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.linearreg(df['close'], 14)
```
- Example XNO's TA usage:
```python
from xno import LINEARREG

f = LINEARREG(df['close'], 14)
```
### LINEARREG_ANGLE	- Linear Regression Angle
Calculates the Linear Regression Angle.

```python
xno.TimeseriesFeatures.linearreg_angle(s1, timeperiod=14)
```
or 
```python
xno.LINEARREG_ANGLE(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.linearreg_angle(df['close'], 14)
```
- Example XNO's TA usage:
```python
from xno import LINEARREG_ANGLE

f = LINEARREG_ANGLE(df['close'], 14)
```
### LINEARREG_INTERCEPT	- Linear Regression Intercept
Calculates the Linear Regression Intercept.

```python
xno.TimeseriesFeatures.linearreg_intercept(s1, timeperiod=14)
```
or 
```python
xno.LINEARREG_INTERCEPT(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.linearreg_intercept(df['close'], 14)
```
- Example XNO's TA usage:
```python
from xno import LINEARREG_INTERCEPT

f = LINEARREG_INTERCEPT(df['close'], 14)
```
### LINEARREG_SLOPE	- Linear Regression Slope
Calculates the Linear Regression Slope.

```python
xno.TimeseriesFeatures.linearreg_slope(s1, timeperiod=14)
```
or 
```python
xno.LINEARREG_SLOPE(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.linearreg_slope(df['close'], 14)
```
- Example XNO's TA usage:
```python
from xno import LINEARREG_SLOPE

f = LINEARREG_SLOPE(df['close'], 14)
```
### MA	- Moving Average
Calculates the Moving Average.

```python
xno.TimeseriesFeatures.ma(series=None, timeperiod=30, matype=0)
```
or 
```python
xno.MA(series, timeperiod, matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ma()
```
- Example XNO's TA usage:
```python
from xno import MA

f = MA(df['close'], 30, 0)
```
### MACD	- Moving Average Convergence/Divergence
Calculates the Moving Average Convergence/Divergence.

```python
xno.TimeseriesFeatures.macd(close=None, fastperiod=12, slowperiod=26, signalperiod=9)
```
or 
```python
xno.MACD(close, fastperiod, slowperiod, signalperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
macd, signal, hist = f.macd()
```
- Example XNO's TA usage:
```python
from xno import MACD

macd, signal, hist = MACD(df['close'], 12, 26, 9)
```
### MACDEXT	- MACD with controllable MA type
Calculates the MACD with controllable MA type.

```python
xno.TimeseriesFeatures.macdext(series=None, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
```
or 
```python
xno.MACDEXT(series, fastperiod, fastmatype, slowperiod, slowmatype, signalperiod, signalmatype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
macd, macdsignal, macdhist = f.macdext()
```
- Example XNO's TA usage:
```python
from xno import MACDEXT

macd, macdsignal, macdhist = MACDEXT(df['close'], 12, 0, 26, 0, 9, 0)
```
### MACDFIX	- Moving Average Convergence/Divergence Fix 12/26
Calculates the Moving Average Convergence/Divergence Fix 12/26.

```python
xno.TimeseriesFeatures.macdfix(series=None, signalperiod=9)
```
or 
```python
xno.MACDFIX(series, signalperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
macd, macdsignal, macdhist = f.macdfix()
```
- Example XNO's TA usage:
```python
from xno import MACDFIX

macd, macdsignal, macdhist = MACDFIX(df['close'], 9)
```
### MAMA	- MESA Adaptive Moving Average
Calculates the MESA Adaptive Moving Average.

```python
xno.TimeseriesFeatures.mama(series=None, fastlimit=0, slowlimit=0)
```
or 
```python
xno.MAMA(series, fastlimit, slowlimit)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
mama, fama = f.mama()
```
- Example XNO's TA usage:
```python
from xno import MAMA

mama, fama = MAMA(df['close'], 0, 0)
```
### MAX	- Highest value over a specified period
Calculates the Highest value over a specified period.

```python
xno.TimeseriesFeatures.max(s1, timeperiod=30)
```
or 
```python
xno.MAX(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.max(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import MAX

f = MAX(df['close'], 30)
```
### MAXINDEX	- Index of highest value over a specified period
Calculates the Index of highest value over a specified period.

```python
xno.TimeseriesFeatures.maxindex(s1, timeperiod=30)
```
or 
```python
xno.MAXINDEX(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.maxindex(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import MAXINDEX

f = MAXINDEX(df['close'], 30)
```
### MEDPRICE	- Median Price
Calculates the Median Price.

```python
xno.TimeseriesFeatures.medprice(high=None, low=None)
```
or 
```python
xno.MEDPRICE(high, low)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.medprice()
```
- Example XNO's TA usage:
```python
from xno import MEDPRICE

f = MEDPRICE(df['high'], df['low'])
```
### MFI	- Money Flow Index
Calculates the Money Flow Index.

```python
xno.TimeseriesFeatures.mfi(high=None, low=None, close=None, volume=None, timeperiod=14)
```
or 
```python
xno.MFI(high, low, close, volume, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.mfi()
```
- Example XNO's TA usage:
```python
from xno import MFI

f = MFI(df['high'], df['low'], df['close'], df['volume'], 14)
```
### MIDPOINT	- MidPoint over period
Calculates the MidPoint over period.

```python
xno.TimeseriesFeatures.midpoint(series=None, timeperiod=14)
```
or 
```python
xno.MIDPOINT(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.midpoint()
```
- Example XNO's TA usage:
```python
from xno import MIDPOINT

f = MIDPOINT(df['close'], 14)
```
### MIDPRICE	- Midpoint Price over period
Calculates the Midpoint Price over period.

```python
xno.TimeseriesFeatures.midprice(high=None, low=None, timeperiod=14)
```
or 
```python
xno.MIDPRICE(high, low, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.midprice()
```
- Example XNO's TA usage:
```python
from xno import MIDPRICE

f = MIDPRICE(df['high'], df['low'], 14)
```
### MIN	- Lowest value over a specified period
Calculates the Lowest value over a specified period.

```python
xno.TimeseriesFeatures.min(s1, timeperiod=30)
```
or 
```python
xno.MIN(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.min(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import MIN

f = MIN(df['close'], 30)
```
### MININDEX	- Index of lowest value over a specified period
Calculates the Index of lowest value over a specified period.

```python
xno.TimeseriesFeatures.minindex(s1, timeperiod=30)
```
or 
```python
xno.MININDEX(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.minindex(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import MININDEX

f = MININDEX(df['close'], 30)
```
### MINMAX	- Lowest and highest values over a specified period
Calculates the Lowest and highest values over a specified period.

```python
xno.TimeseriesFeatures.minmax(s1, timeperiod=30)
```
or 
```python
xno.MINMAX(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
min_val, max_val = f.minmax(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import MINMAX

min_val, max_val = MINMAX(df['close'], 30)
```
### MINMAXINDEX	- Indexes of lowest and highest values over a specified period
Calculates the Indexes of lowest and highest values over a specified period.

```python
xno.TimeseriesFeatures.minmaxindex(s1, timeperiod=30)
```
or 
```python
xno.MINMAXINDEX(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.minmaxindex(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import MINMAXINDEX

f = MINMAXINDEX(df['close'], 30)
```
### MINUS_DI	- Minus Directional Indicator
Calculates the Minus Directional Indicator.

```python
xno.TimeseriesFeatures.minus_di(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.MINUS_DI(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.minus_di()
```
- Example XNO's TA usage:
```python
from xno import MINUS_DI

f = MINUS_DI(df['high'], df['low'], df['close'], 14)
```
### MINUS_DM	- Minus Directional Movement
Calculates the Minus Directional Movement.

```python
xno.TimeseriesFeatures.minus_dm(high=None, low=None, timeperiod=14)
```
or 
```python
xno.MINUS_DM(high, low, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.minus_dm()
```
- Example XNO's TA usage:
```python
from xno import MINUS_DM

f = MINUS_DM(df['high'], df['low'], 14)
```
### MOM	- Momentum
Calculates the Momentum.

```python
xno.TimeseriesFeatures.mom(series=None, timeperiod=10)
```
or 
```python
xno.MOM(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.mom()
```
- Example XNO's TA usage:
```python
from xno import MOM

f = MOM(df['close'], 10)
```
### NATR	- Normalized Average True Range
Calculates the Normalized Average True Range.

```python
xno.TimeseriesFeatures.natr(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.NATR(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.natr()
```
- Example XNO's TA usage:
```python
from xno import NATR

f = NATR(df['high'], df['low'], df['close'], 14)
```
### OBV	- On Balance Volume
Calculates the On Balance Volume.

```python
xno.TimeseriesFeatures.obv(close=None, volume=None)
```
or 
```python
xno.OBV(close, volume)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.obv()
```
- Example XNO's TA usage:
```python
from xno import OBV

f = OBV(df['close'], df['volume'])
```
### PLUS_DI	- Plus Directional Indicator
Calculates the Plus Directional Indicator.

```python
xno.TimeseriesFeatures.plus_di(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.PLUS_DI(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.plus_di()
```
- Example XNO's TA usage:
```python
from xno import PLUS_DI

f = PLUS_DI(df['high'], df['low'], df['close'], 14)
```
### PLUS_DM	- Plus Directional Movement
Calculates the Plus Directional Movement.

```python
xno.TimeseriesFeatures.plus_dm(high=None, low=None, timeperiod=14)
```
or 
```python
xno.PLUS_DM(high, low, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.plus_dm()
```
- Example XNO's TA usage:
```python
from xno import PLUS_DM

f = PLUS_DM(df['high'], df['low'], 14)
```
### PPO	- Percentage Price Oscillator
Calculates the Percentage Price Oscillator.

```python
xno.TimeseriesFeatures.ppo(series=None, fastperiod=12, slowperiod=26, matype=0)
```
or 
```python
xno.PPO(series, fastperiod, slowperiod, matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ppo()
```
- Example XNO's TA usage:
```python
from xno import PPO

f = PPO(df['close'], 12, 26, 0)
```
### ROC	- Rate of change : ((price/prevPrice)-1)*100
Calculates the Rate of change : ((price/prevPrice)-1)*100.

```python
xno.TimeseriesFeatures.roc(close=None, timeperiod=10)
```
or 
```python
xno.ROC(close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.roc()
```
- Example XNO's TA usage:
```python
from xno import ROC

f = ROC(df['close'], 10)
```
### ROCP	- Rate of change Percentage: (price-prevPrice)/prevPrice
Calculates the Rate of change Percentage: (price-prevPrice)/prevPrice.

```python
xno.TimeseriesFeatures.rocp(series=None, timeperiod=10)
```
or 
```python
xno.ROCP(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.rocp()
```
- Example XNO's TA usage:
```python
from xno import ROCP

f = ROCP(df['close'], 10)
```
### ROCR	- Rate of change ratio: (price/prevPrice)
Calculates the Rate of change ratio: (price/prevPrice).

```python
xno.TimeseriesFeatures.rocr(series=None, timeperiod=10)
```
or 
```python
xno.ROCR(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.rocr()
```
- Example XNO's TA usage:
```python
from xno import ROCR

f = ROCR(df['close'], 10)
```
### ROCR100	- Rate of change ratio 100 scale: (price/prevPrice)*100
Calculates the Rate of change ratio 100 scale: (price/prevPrice)*100.

```python
xno.TimeseriesFeatures.rocr100(series=None, timeperiod=10)
```
or 
```python
xno.ROCR100(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.rocr100()
```
- Example XNO's TA usage:
```python
from xno import ROCR100

f = ROCR100(df['close'], 10)
```
### RSI	- Relative Strength Index
Calculates the Relative Strength Index.

```python
xno.TimeseriesFeatures.rsi(close=None, timeperiod=14)
```
or 
```python
xno.RSI(close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.rsi()
```
- Example XNO's TA usage:
```python
from xno import RSI

f = RSI(df['close'], 14)
```
### SAR	- Parabolic SAR
Calculates the Parabolic SAR.

```python
xno.TimeseriesFeatures.sar(high=None, low=None, acceleration=0, maximum=0)
```
or 
```python
xno.SAR(high, low, acceleration, maximum)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sar()
```
- Example XNO's TA usage:
```python
from xno import SAR

f = SAR(df['high'], df['low'], 0, 0)
```
### SAREXT	- Parabolic SAR - Extended
Calculates the Parabolic SAR - Extended.

```python
xno.TimeseriesFeatures.sarext(high=None, low=None, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
```
or 
```python
xno.SAREXT(high, low, startvalue, offsetonreverse, accelerationinitlong, accelerationlong, accelerationmaxlong, accelerationinitshort, accelerationshort, accelerationmaxshort)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sarext()
```
- Example XNO's TA usage:
```python
from xno import SAREXT

f = SAREXT(df['high'], df['low'], 0, 0, 0, 0, 0, 0, 0, 0)
```
### SMA	- Simple Moving Average
Calculates the Simple Moving Average.

```python
xno.TimeseriesFeatures.sma(Close=None, timeperiod=30)
```
or 
```python
xno.SMA(Close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sma()
```
- Example XNO's TA usage:
```python
from xno import SMA

f = SMA(df['close'], 30)
```
### STDDEV	- Standard Deviation
Calculates the Standard Deviation.

```python
xno.TimeseriesFeatures.stddev(s1, timeperiod=5, nbdev=1)
```
or 
```python
xno.STDDEV(s1, timeperiod, nbdev)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.stddev(df['close'], 5, 1)
```
- Example XNO's TA usage:
```python
from xno import STDDEV

f = STDDEV(df['close'], 5, 1)
```
### STOCH	- Stochastic
Calculates the Stochastic.

```python
xno.TimeseriesFeatures.stoch(high=None, low=None, close=None, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
```
or 
```python
xno.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
slowk, slowd = f.stoch()
```
- Example XNO's TA usage:
```python
from xno import STOCH

slowk, slowd = STOCH(df['high'], df['low'], df['close'], 5, 3, 0, 3, 0)
```
### STOCHF	- Stochastic Fast
Calculates the Stochastic Fast.

```python
xno.TimeseriesFeatures.stochf(high=None, low=None, close=None, fastk_period=5, fastd_period=3, fastd_matype=0)
```
or 
```python
xno.STOCHF(high, low, close, fastk_period, fastd_period, fastd_matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
fastk, fastd = f.stochf()
```
- Example XNO's TA usage:
```python
from xno import STOCHF

fastk, fastd = STOCHF(df['high'], df['low'], df['close'], 5, 3, 0)
```
### STOCHRSI	- Stochastic Relative Strength Index
Calculates the Stochastic Relative Strength Index.

```python
xno.TimeseriesFeatures.stochrsi(series=None, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
```
or 
```python
xno.STOCHRSI(series, timeperiod, fastk_period, fastd_period, fastd_matype)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
fastk, fastd = f.stochrsi()
```
- Example XNO's TA usage:
```python
from xno import STOCHRSI

fastk, fastd = STOCHRSI(df['close'], 14, 5, 3, 0)
```
### SUM	- Summation
Calculates the Summation.

```python
xno.TimeseriesFeatures.sum(s1, timeperiod=30)
```
or 
```python
xno.SUM(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sum(df['close'], 30)
```
- Example XNO's TA usage:
```python
from xno import SUM

f = SUM(df['close'], 30)
```
### T3	- Triple Exponential Moving Average (T3)
Calculates the Triple Exponential Moving Average (T3).

```python
xno.TimeseriesFeatures.t3(series=None, timeperiod=5, vfactor=0)
```
or 
```python
xno.T3(series, timeperiod, vfactor)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.t3()
```
- Example XNO's TA usage:
```python
from xno import T3

f = T3(df['close'], 5, 0)
```
### TEMA	- Triple Exponential Moving Average
Calculates the Triple Exponential Moving Average.

```python
xno.TimeseriesFeatures.tema(series=None, timeperiod=30)
```
or 
```python
xno.TEMA(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.tema()
```
- Example XNO's TA usage:
```python
from xno import TEMA

f = TEMA(df['close'], 30)
```
### TRANGE	- True Range
Calculates the True Range.

```python
xno.TimeseriesFeatures.trange(high=None, low=None, close=None)
```
or 
```python
xno.TRANGE(high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.trange()
```
- Example XNO's TA usage:
```python
from xno import TRANGE

f = TRANGE(df['high'], df['low'], df['close'])
```
### TRIMA	- Triangular Moving Average
Calculates the Triangular Moving Average.

```python
xno.TimeseriesFeatures.trima(series=None, timeperiod=30)
```
or 
```python
xno.TRIMA(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.trima()
```
- Example XNO's TA usage:
```python
from xno import TRIMA

f = TRIMA(df['close'], 30)
```
### TRIX	- 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
Calculates the 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA.

```python
xno.TimeseriesFeatures.trix(close=None, timeperiod=30)
```
or 
```python
xno.TRIX(close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.trix()
```
- Example XNO's TA usage:
```python
from xno import TRIX

f = TRIX(df['close'], 30)
```
### TSF	- Time Series Forecast
Calculates the Time Series Forecast.

```python
xno.TimeseriesFeatures.tsf(s1, timeperiod=14)
```
or 
```python
xno.TSF(s1, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.tsf(df['close'], 14)
```
- Example XNO's TA usage:
```python
from xno import TSF

f = TSF(df['close'], 14)
```
### TYPPRICE	- Typical Price
Calculates the Typical Price.

```python
xno.TimeseriesFeatures.typprice(high=None, low=None, close=None)
```
or 
```python
xno.TYPPRICE(high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.typprice()
```
- Example XNO's TA usage:
```python
from xno import TYPPRICE

f = TYPPRICE(df['high'], df['low'], df['close'])
```
### ULTOSC	- Ultimate Oscillator
Calculates the Ultimate Oscillator.

```python
xno.TimeseriesFeatures.ultosc(high=None, low=None, close=None, timeperiod1=7, timeperiod2=14, timeperiod3=28)
```
or 
```python
xno.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ultosc()
```
- Example XNO's TA usage:
```python
from xno import ULTOSC

f = ULTOSC(df['high'], df['low'], df['close'], 7, 14, 28)
```
### VAR	- Variance
Calculates the Variance.

```python
xno.TimeseriesFeatures.var(s1, timeperiod=5, nbdev=1)
```
or 
```python
xno.VAR(s1, timeperiod, nbdev)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.var(df['close'], 5, 1)
```
- Example XNO's TA usage:
```python
from xno import VAR

f = VAR(df['close'], 5, 1)
```
### WCLPRICE	- Weighted Close Price
Calculates the Weighted Close Price.

```python
xno.TimeseriesFeatures.wclprice(high=None, low=None, close=None)
```
or 
```python
xno.WCLPRICE(high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.wclprice()
```
- Example XNO's TA usage:
```python
from xno import WCLPRICE

f = WCLPRICE(df['high'], df['low'], df['close'])
```
### WILLR	- Williams' %R
Calculates the Williams' %R.

```python
xno.TimeseriesFeatures.willr(high=None, low=None, close=None, timeperiod=14)
```
or 
```python
xno.WILLR(high, low, close, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.willr()
```
- Example XNO's TA usage:
```python
from xno import WILLR

f = WILLR(df['high'], df['low'], df['close'], 14)
```
### WMA	- Weighted Moving Average
Calculates the Weighted Moving Average.

```python
xno.TimeseriesFeatures.wma(series=None, timeperiod=30)
```
or 
```python
xno.WMA(series, timeperiod)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.wma()
```
- Example XNO's TA usage:
```python
from xno import WMA

f = WMA(df['close'], 30)
```

