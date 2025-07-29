## Chart Patterns
### TWO_CROWS	- Two Crows
Identifies the Two Crows candlestick pattern.

```python
xno.TimeseriesFeatures.two_crows(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.timeseries.TWO_CROWS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno.algo.features import TimeseriesFeatures

ta = TimeseriesFeatures(df)
result = ta.two_crows()
```
- Example XNO's TA usage:
```python
import xno.timeseries as xts

result = xts.TWO_CROWS(df['Open'], df['High'], df['Low'], df['Close'])
```
### THREE_BLACK_CROWS	- Three Black Crows
Identifies the Three Black Crows candlestick pattern.

```python
xno.TimeseriesFeatures.three_black_crows(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.timeseries.THREE_BLACK_CROWS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno.algo.features import TimeseriesFeatures

ta = TimeseriesFeatures(df)
result = ta.three_black_crows()
```
- Example XNO's TA usage:
```python
import xno.timeseries as xts

result = xts.THREE_BLACK_CROWS(df['Open'], df['High'], df['Low'], df['Close'])
```
### CDL3INSIDE	- Three Inside Up/Down
Identifies the Three Inside Up/Down candlestick pattern.

```python
xno.TimeseriesFeatures.three_inside_up_down(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDL3INSIDE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.three_inside_up_down()
```
- Example XNO's TA usage:
```python
from xno import CDL3INSIDE

f = CDL3INSIDE(df['open'], df['high'], df['low'], df['close'])
```
### CDL3LINESTRIKE	- Three Outside Up/Down
Identifies the Three Line Strike candlestick pattern.

```python
xno.TimeseriesFeatures.cdl3linestrike(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDL3LINESTRIKE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdl3linestrike()
```
- Example XNO's TA usage:
```python
from xno import CDL3LINESTRIKE

f = CDL3LINESTRIKE(df['open'], df['high'], df['low'], df['close'])
```
### CDL3STARSINSOUTH	- Three Stars In The South
Identifies the Three Stars In The South candlestick pattern.

```python
xno.TimeseriesFeatures.cdl3starsinsouth(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDL3STARSINSOUTH(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdl3starsinsouth()
```
- Example XNO's TA usage:
```python
from xno import CDL3STARSINSOUTH

f = CDL3STARSINSOUTH(df['open'], df['high'], df['low'], df['close'])
```
### CDL3WHITESOLDIERS	- Three Advancing White Soldiers
Identifies the Three Advancing White Soldiers candlestick pattern.

```python
xno.TimeseriesFeatures.cdl3whitesoldiers(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDL3WHITESOLDIERS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdl3whitesoldiers()
```
- Example XNO's TA usage:
```python
from xno import CDL3WHITESOLDIERS

f = CDL3WHITESOLDIERS(df['open'], df['high'], df['low'], df['close'])
```
### CDLABANDONEDBABY	- Abandoned Baby
Identifies the Abandoned Baby candlestick pattern.

```python
xno.TimeseriesFeatures.cdlabandonedbaby(open_=None, high=None, low=None, close=None, penetration=0.3)
```
or 
```python
xno.CDLABANDONEDBABY(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlabandonedbaby()
```
- Example XNO's TA usage:
```python
from xno import CDLABANDONEDBABY

f = CDLABANDONEDBABY(df['open'], df['high'], df['low'], df['close'], 0.3)
```
### CDLADVANCEBLOCK	- Advance Block
Identifies the Advance Block candlestick pattern.

```python
xno.TimeseriesFeatures.cdladvanceblock(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLADVANCEBLOCK(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdladvanceblock()
```
- Example XNO's TA usage:
```python
from xno import CDLADVANCEBLOCK

f = CDLADVANCEBLOCK(df['open'], df['high'], df['low'], df['close'])
```
### CDLBELTHOLD	- Belt-Hold
Identifies the Belt-Hold candlestick pattern.

```python
xno.TimeseriesFeatures.cdlbelthold(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLBELTHOLD(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlbelthold()
```
- Example XNO's TA usage:
```python
from xno import CDLBELTHOLD

f = CDLBELTHOLD(df['open'], df['high'], df['low'], df['close'])
```
### CDLBREAKAWAY	- Breakaway
Identifies the Breakaway candlestick pattern.

```python
xno.TimeseriesFeatures.cdlbreakaway(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLBREAKAWAY(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlbreakaway()
```
- Example XNO's TA usage:
```python
from xno import CDLBREAKAWAY

f = CDLBREAKAWAY(df['open'], df['high'], df['low'], df['close'])
```
### CDLCLOSINGMARUBOZU	- Closing Marubozu
Identifies the Closing Marubozu candlestick pattern.

```python
xno.TimeseriesFeatures.cdlclosingmarubozu(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLCLOSINGMARUBOZU(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlclosingmarubozu()
```
- Example XNO's TA usage:
```python
from xno import CDLCLOSINGMARUBOZU

f = CDLCLOSINGMARUBOZU(df['open'], df['high'], df['low'], df['close'])
```
### CDLCONCEALBABYSWALL	- Concealing Baby Swallow
Identifies the Concealing Baby Swallow candlestick pattern.

```python
xno.TimeseriesFeatures.cdlconcealbabyswall(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLCONCEALBABYSWALL(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlconcealbabyswall()
```
- Example XNO's TA usage:
```python
from xno import CDLCONCEALBABYSWALL

f = CDLCONCEALBABYSWALL(df['open'], df['high'], df['low'], df['close'])
```
### CDLCOUNTERATTACK	- Counterattack
Identifies the Counterattack candlestick pattern.

```python
xno.TimeseriesFeatures.cdlcounterattack(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLCOUNTERATTACK(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlcounterattack()
```
- Example XNO's TA usage:
```python
from xno import CDLCOUNTERATTACK

f = CDLCOUNTERATTACK(df['open'], df['high'], df['low'], df['close'])
```
### CDLDARKCLOUDCOVER	- Dark Cloud Cover
Identifies the Dark Cloud Cover candlestick pattern.

```python
xno.TimeseriesFeatures.cdldarkcloudcover(open_=None, high=None, low=None, close=None, penetration=0.5)
```
or 
```python
xno.CDLDARKCLOUDCOVER(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdldarkcloudcover()
```
- Example XNO's TA usage:
```python
from xno import CDLDARKCLOUDCOVER

f = CDLDARKCLOUDCOVER(df['open'], df['high'], df['low'], df['close'], 0.5)
```
### CDLDOJI	Doji
Identifies the Doji candlestick pattern.

```python
xno.TimeseriesFeatures.cdldoji(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLDOJI(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdldoji()
```
- Example XNO's TA usage:
```python
from xno import CDLDOJI

f = CDLDOJI(df['open'], df['high'], df['low'], df['close'])
```
### CDLDOJISTAR	- Doji Star
Identifies the Doji Star candlestick pattern.

```python
xno.TimeseriesFeatures.cdldojistar(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLDOJISTAR(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdldojistar()
```
- Example XNO's TA usage:
```python
from xno import CDLDOJISTAR

f = CDLDOJISTAR(df['open'], df['high'], df['low'], df['close'])
```
### CDLDRAGONFLYDOJI	- Dragonfly Doji
Identifies the Dragonfly Doji candlestick pattern.

```python
xno.TimeseriesFeatures.cdldragonflydoji(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLDRAGONFLYDOJI(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdldragonflydoji()
```
- Example XNO's TA usage:
```python
from xno import CDLDRAGONFLYDOJI

f = CDLDRAGONFLYDOJI(df['open'], df['high'], df['low'], df['close'])
```
### CDLENGULFING	- Engulfing Pattern
Identifies the Engulfing Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlengulfing(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLENGULFING(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlengulfing()
```
- Example XNO's TA usage:
```python
from xno import CDLENGULFING

f = CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
```
### CDLEVENINGDOJISTAR	- Evening Doji Star
Identifies the Evening Doji Star candlestick pattern.

```python
xno.TimeseriesFeatures.cdleveningdojistar(open_=None, high=None, low=None, close=None, penetration=0.3)
```
or 
```python
xno.CDLEVENINGDOJISTAR(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdleveningdojistar()
```
- Example XNO's TA usage:
```python
from xno import CDLEVENINGDOJISTAR

f = CDLEVENINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], 0.3)
```
### CDLEVENINGSTAR	- Evening Star
Identifies the Evening Star candlestick pattern.

```python
xno.TimeseriesFeatures.cdleveningstar(open_=None, high=None, low=None, close=None, penetration=0.3)
```
or 
```python
xno.CDLEVENINGSTAR(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdleveningstar()
```
- Example XNO's TA usage:
```python
from xno import CDLEVENINGSTAR

f = CDLEVENINGSTAR(df['open'], df['high'], df['low'], df['close'], 0.3)
```
### CDLGAPSIDESIDEWHITE	- Up/Down-gap side-by-side white lines
Identifies the Up/Down-gap side-by-side white lines candlestick pattern.

```python
xno.TimeseriesFeatures.cdlgapsidesidewhite(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLGAPSIDESIDEWHITE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlgapsidesidewhite()
```
- Example XNO's TA usage:
```python
from xno import CDLGAPSIDESIDEWHITE

f = CDLGAPSIDESIDEWHITE(df['open'], df['high'], df['low'], df['close'])
```
### CDLGRAVESTONEDOJI	- Gravestone Doji
Identifies the Gravestone Doji candlestick pattern.

```python
xno.TimeseriesFeatures.cdlgravestonedoji(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLGRAVESTONEDOJI(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlgravestonedoji()
```
- Example XNO's TA usage:
```python
from xno import CDLGRAVESTONEDOJI

f = CDLGRAVESTONEDOJI(df['open'], df['high'], df['low'], df['close'])
```
### CDLHAMMER	- Hammer
Identifies the Hammer candlestick pattern.

```python
xno.TimeseriesFeatures.cdlhammer(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHAMMER(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlhammer()
```
- Example XNO's TA usage:
```python
from xno import CDLHAMMER

f = CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
```
### CDLHANGINGMAN	- Hanging Man
Identifies the Hanging Man candlestick pattern.

```python
xno.TimeseriesFeatures.cdlhangingman(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHANGINGMAN(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlhangingman()
```
- Example XNO's TA usage:
```python
from xno import CDLHANGINGMAN

f = CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])
```
### CDLHARAMI	- Harami Pattern
Identifies the Harami Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlharami(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHARAMI(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlharami()
```
- Example XNO's TA usage:
```python
from xno import CDLHARAMI

f = CDLHARAMI(df['open'], df['high'], df['low'], df['close'])
```
### CDLHARAMICROSS	- Harami Cross Pattern
Identifies the Harami Cross Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlharamicross(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHARAMICROSS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlharamicross()
```
- Example XNO's TA usage:
```python
from xno import CDLHARAMICROSS

f = CDLHARAMICROSS(df['open'], df['high'], df['low'], df['close'])
```
### CDLHIGHWAVE	- High-Wave Candle
Identifies the High-Wave Candle candlestick pattern.

```python
xno.TimeseriesFeatures.cdlhighwave(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHIGHWAVE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlhighwave()
```
- Example XNO's TA usage:
```python
from xno import CDLHIGHWAVE

f = CDLHIGHWAVE(df['open'], df['high'], df['low'], df['close'])
```
### CDLHIKKAKE	- Hikkake Pattern
Identifies the Hikkake Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlhikkake(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHIKKAKE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlhikkake()
```
- Example XNO's TA usage:
```python
from xno import CDLHIKKAKE

f = CDLHIKKAKE(df['open'], df['high'], df['low'], df['close'])
```
### CDLHIKKAKEMOD	- Modified Hikkake Pattern
Identifies the Modified Hikkake Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlhikkakemod(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHIKKAKEMOD(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlhikkakemod()
```
- Example XNO's TA usage:
```python
from xno import CDLHIKKAKEMOD

f = CDLHIKKAKEMOD(df['open'], df['high'], df['low'], df['close'])
```
### CDLHOMINGPIGEON	- Homing Pigeon
Identifies the Homing Pigeon candlestick pattern.

```python
xno.TimeseriesFeatures.cdlhomingpigeon(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLHOMINGPIGEON(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlhomingpigeon()
```
- Example XNO's TA usage:
```python
from xno import CDLHOMINGPIGEON

f = CDLHOMINGPIGEON(df['open'], df['high'], df['low'], df['close'])
```
### CDLIDENTICAL3CROWS	- Identical Three Crows
Identifies the Identical Three Crows candlestick pattern.

```python
xno.TimeseriesFeatures.cdlidentical3crows(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLIDENTICAL3CROWS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlidentical3crows()
```
- Example XNO's TA usage:
```python
from xno import CDLIDENTICAL3CROWS

f = CDLIDENTICAL3CROWS(df['open'], df['high'], df['low'], df['close'])
```
### CDLINNECK	- In-Neck Pattern
Identifies the In-Neck Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlinneck(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLINNECK(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlinneck()
```
- Example XNO's TA usage:
```python
from xno import CDLINNECK

f = CDLINNECK(df['open'], df['high'], df['low'], df['close'])
```
### CDLINVERTEDHAMMER	- Inverted Hammer
Identifies the Inverted Hammer candlestick pattern.

```python
xno.TimeseriesFeatures.cdlinvertedhammer(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLINVERTEDHAMMER(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlinvertedhammer()
```
- Example XNO's TA usage:
```python
from xno import CDLINVERTEDHAMMER

f = CDLINVERTEDHAMMER(df['open'], df['high'], df['low'], df['close'])
```
### CDLKICKING	- Kicking
Identifies the Kicking candlestick pattern.

```python
xno.TimeseriesFeatures.cdlkicking(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLKICKING(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlkicking()
```
- Example XNO's TA usage:
```python
from xno import CDLKICKING

f = CDLKICKING(df['open'], df['high'], df['low'], df['close'])
```
### CDLKICKINGBYLENGTH	- Kicking - bull/bear determined by the longer marubozu
Identifies the Kicking by Length candlestick pattern.

```python
xno.TimeseriesFeatures.cdlkickingbylength(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLKICKINGBYLENGTH(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlkickingbylength()
```
- Example XNO's TA usage:
```python
from xno import CDLKICKINGBYLENGTH

f = CDLKICKINGBYLENGTH(df['open'], df['high'], df['low'], df['close'])
```
### CDLLADDERBOTTOM	- Ladder Bottom
Identifies the Ladder Bottom candlestick pattern.

```python
xno.TimeseriesFeatures.cdlladderbottom(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLLADDERBOTTOM(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlladderbottom()
```
- Example XNO's TA usage:
```python
from xno import CDLLADDERBOTTOM

f = CDLLADDERBOTTOM(df['open'], df['high'], df['low'], df['close'])
```
### CDLLONGLEGGEDDOJI	- Long Legged Doji
Identifies the Long Legged Doji candlestick pattern.

```python
xno.TimeseriesFeatures.cdllongleggeddoji(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLLONGLEGGEDDOJI(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdllongleggeddoji()
```
- Example XNO's TA usage:
```python
from xno import CDLLONGLEGGEDDOJI

f = CDLLONGLEGGEDDOJI(df['open'], df['high'], df['low'], df['close'])
```
### CDLLONGLINE - 	Long Line Candle
Identifies the Long Line Candle candlestick pattern.

```python
xno.TimeseriesFeatures.cdllongline(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLLONGLINE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdllongline()
```
- Example XNO's TA usage:
```python
from xno import CDLLONGLINE

f = CDLLONGLINE(df['open'], df['high'], df['low'], df['close'])
```
### CDLMARUBOZU	- Marubozu
Identifies the Marubozu candlestick pattern.

```python
xno.TimeseriesFeatures.cdlmarubozu(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLMARUBOZU(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlmarubozu()
```
- Example XNO's TA usage:
```python
from xno import CDLMARUBOZU

f = CDLMARUBOZU(df['open'], df['high'], df['low'], df['close'])
```
### CDLMATCHINGLOW	- Matching Low
Identifies the Matching Low candlestick pattern.

```python
xno.TimeseriesFeatures.cdlmatchinglow(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLMATCHINGLOW(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlmatchinglow()
```
- Example XNO's TA usage:
```python
from xno import CDLMATCHINGLOW

f = CDLMATCHINGLOW(df['open'], df['high'], df['low'], df['close'])
```
### CDLMATHOLD	- Mat Hold
Identifies the Mat Hold candlestick pattern.

```python
xno.TimeseriesFeatures.cdlmathold(open_=None, high=None, low=None, close=None, penetration=0.5)
```
or 
```python
xno.CDLMATHOLD(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlmathold()
```
- Example XNO's TA usage:
```python
from xno import CDLMATHOLD

f = CDLMATHOLD(df['open'], df['high'], df['low'], df['close'], 0.5)
```
### CDLMORNINGDOJISTAR	- Morning Doji Star
Identifies the Morning Doji Star candlestick pattern.

```python
xno.TimeseriesFeatures.cdlmorningdojistar(open_=None, high=None, low=None, close=None, penetration=0.3)
```
or 
```python
xno.CDLMORNINGDOJISTAR(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlmorningdojistar()
```
- Example XNO's TA usage:
```python
from xno import CDLMORNINGDOJISTAR

f = CDLMORNINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], 0.3)
```
### CDLMORNINGSTAR	- Morning Star
Identifies the Morning Star candlestick pattern.

```python
xno.TimeseriesFeatures.cdlmorningstar(open_=None, high=None, low=None, close=None, penetration=0.3)
```
or 
```python
xno.CDLMORNINGSTAR(open_, high, low, close, penetration)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlmorningstar()
```
- Example XNO's TA usage:
```python
from xno import CDLMORNINGSTAR

f = CDLMORNINGSTAR(df['open'], df['high'], df['low'], df['close'], 0.3)
```
### CDLONNECK	- On-Neck Pattern
Identifies the On-Neck Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlonneck(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLONNECK(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlonneck()
```
- Example XNO's TA usage:
```python
from xno import CDLONNECK

f = CDLONNECK(df['open'], df['high'], df['low'], df['close'])
```
### CDLPIERCING	- Piercing Pattern
Identifies the Piercing Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlpiercing(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLPIERCING(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlpiercing()
```
- Example XNO's TA usage:
```python
from xno import CDLPIERCING

f = CDLPIERCING(df['open'], df['high'], df['low'], df['close'])
```
### CDLRICKSHAWMAN	- Rickshaw Man
Identifies the Rickshaw Man candlestick pattern.

```python
xno.TimeseriesFeatures.cdlrickshawman(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLRICKSHAWMAN(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlrickshawman()
```
- Example XNO's TA usage:
```python
from xno import CDLRICKSHAWMAN

f = CDLRICKSHAWMAN(df['open'], df['high'], df['low'], df['close'])
```
### CDLRISEFALL3METHODS	- Rising/Falling Three Methods
Identifies the Rising/Falling Three Methods candlestick pattern.

```python
xno.TimeseriesFeatures.cdlrisefall3methods(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLRISEFALL3METHODS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlrisefall3methods()
```
- Example XNO's TA usage:
```python
from xno import CDLRISEFALL3METHODS

f = CDLRISEFALL3METHODS(df['open'], df['high'], df['low'], df['close'])
```
### CDLSEPARATINGLINES	- Separating Lines
Identifies the Separating Lines candlestick pattern.

```python
xno.TimeseriesFeatures.cdlseparatinglines(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLSEPARATINGLINES(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlseparatinglines()
```
- Example XNO's TA usage:
```python
from xno import CDLSEPARATINGLINES

f = CDLSEPARATINGLINES(df['open'], df['high'], df['low'], df['close'])
```
### CDLSHOOTINGSTAR	- Shooting Star
Identifies the Shooting Star candlestick pattern.

```python
xno.TimeseriesFeatures.cdlshootingstar(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLSHOOTINGSTAR(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlshootingstar()
```
- Example XNO's TA usage:
```python
from xno import CDLSHOOTINGSTAR

f = CDLSHOOTINGSTAR(df['open'], df['high'], df['low'], df['close'])
```
### CDLSHORTLINE	- Short Line Candle
Identifies the Short Line Candle candlestick pattern.

```python
xno.TimeseriesFeatures.cdlshortline(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLSHORTLINE(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlshortline()
```
- Example XNO's TA usage:
```python
from xno import CDLSHORTLINE

f = CDLSHORTLINE(df['open'], df['high'], df['low'], df['close'])
```
### CDLSPINNINGTOP	- Spinning Top
Identifies the Spinning Top candlestick pattern.

```python
xno.TimeseriesFeatures.cdlspinningtop(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLSPINNINGTOP(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlspinningtop()
```
- Example XNO's TA usage:
```python
from xno import CDLSPINNINGTOP

f = CDLSPINNINGTOP(df['open'], df['high'], df['low'], df['close'])
```
### CDLSTALLEDPATTERN	- Stalled Pattern
Identifies the Stalled Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlstalledpattern(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLSTALLEDPATTERN(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlstalledpattern()
```
- Example XNO's TA usage:
```python
from xno import CDLSTALLEDPATTERN

f = CDLSTALLEDPATTERN(df['open'], df['high'], df['low'], df['close'])
```
### CDLSTICKSANDWICH	- Stick Sandwich
Identifies the Stick Sandwich candlestick pattern.

```python
xno.TimeseriesFeatures.cdlsticksandwich(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLSTICKSANDWICH(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlsticksandwich()
```
- Example XNO's TA usage:
```python
from xno import CDLSTICKSANDWICH

f = CDLSTICKSANDWICH(df['open'], df['high'], df['low'], df['close'])
```
### CDLTAKURI	- Takuri (Dragonfly Doji with very long lower shadow)
Identifies the Takuri candlestick pattern.

```python
xno.TimeseriesFeatures.cdltakuri(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLTAKURI(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdltakuri()
```
- Example XNO's TA usage:
```python
from xno import CDLTAKURI

f = CDLTAKURI(df['open'], df['high'], df['low'], df['close'])
```
### CDLTASUKIGAP	- Tasuki Gap
Identifies the Tasuki Gap candlestick pattern.

```python
xno.TimeseriesFeatures.cdltasukigap(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLTASUKIGAP(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdltasukigap()
```
- Example XNO's TA usage:
```python
from xno import CDLTASUKIGAP

f = CDLTASUKIGAP(df['open'], df['high'], df['low'], df['close'])
```
### CDLTHRUSTING	- Thrusting Pattern
Identifies the Thrusting Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdlthrusting(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLTHRUSTING(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlthrusting()
```
- Example XNO's TA usage:
```python
from xno import CDLTHRUSTING

f = CDLTHRUSTING(df['open'], df['high'], df['low'], df['close'])
```
### CDLTRISTAR	- Tristar Pattern
Identifies the Tristar Pattern candlestick pattern.

```python
xno.TimeseriesFeatures.cdltristar(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLTRISTAR(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdltristar()
```
- Example XNO's TA usage:
```python
from xno import CDLTRISTAR

f = CDLTRISTAR(df['open'], df['high'], df['low'], df['close'])
```
### CDLUNIQUE3RIVER	- Unique 3 River
Identifies the Unique 3 River candlestick pattern.

```python
xno.TimeseriesFeatures.cdlunique3river(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLUNIQUE3RIVER(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlunique3river()
```
- Example XNO's TA usage:
```python
from xno import CDLUNIQUE3RIVER

f = CDLUNIQUE3RIVER(df['open'], df['high'], df['low'], df['close'])
```
### CDLUPSIDEGAP2CROWS	- Upside Gap Two Crows
Identifies the Upside Gap Two Crows candlestick pattern.

```python
xno.TimeseriesFeatures.cdlupsidegap2crows(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLUPSIDEGAP2CROWS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlupsidegap2crows()
```
- Example XNO's TA usage:
```python
from xno import CDLUPSIDEGAP2CROWS

f = CDLUPSIDEGAP2CROWS(df['open'], df['high'], df['low'], df['close'])
```
### CDLXSIDEGAP3METHODS	- Upside/Downside Gap Three Methods
Identifies the Upside/Downside Gap Three Methods candlestick pattern.

```python
xno.TimeseriesFeatures.cdlxsidegap3methods(open_=None, high=None, low=None, close=None)
```
or 
```python
xno.CDLXSIDEGAP3METHODS(open_, high, low, close)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cdlxsidegap3methods()
```
- Example XNO's TA usage:
```python
from xno import CDLXSIDEGAP3METHODS

f = CDLXSIDEGAP3METHODS(df['open'], df['high'], df['low'], df['close'])
```