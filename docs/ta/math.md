

## Math Functions
### ACOS         -        Vector Trigonometric ACos
Calculates the Vector Trigonometric ACos.

```python
xno.TimeseriesFeatures.acos(s1)
```
or 
```python
xno.ACOS(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.acos(df['close'])
```
- Example XNO's TA usage:
```python
from xno import ACOS

f = ACOS(df['close'])
```
### ADD          -        Vector Arithmetic Add
Calculates the Vector Arithmetic Add.

```python
xno.TimeseriesFeatures.add(s1, s2)
```
or 
```python
xno.ADD(s1, s2)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.add(df['close'], df['volume'])
```
- Example XNO's TA usage:
```python
from xno import ADD

f = ADD(df['close'], df['volume'])
```
### ASIN         -        Vector Trigonometric ASin
Calculates the Vector Trigonometric ASin.

```python
xno.TimeseriesFeatures.asin(s1)
```
or 
```python
xno.ASIN(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.asin(df['close'])
```
- Example XNO's TA usage:
```python
from xno import ASIN

f = ASIN(df['close'])
```
### ATAN         -        Vector Trigonometric ATan
Calculates the Vector Trigonometric ATan.

```python
xno.TimeseriesFeatures.atan(s1)
```
or 
```python
xno.ATAN(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.atan(df['close'])
```
- Example XNO's TA usage:
```python
from xno import ATAN

f = ATAN(df['close'])
```
### CEIL         -        Vector Ceil
Calculates the Vector Ceil.

```python
xno.TimeseriesFeatures.ceil(s1)
```
or 
```python
xno.CEIL(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ceil(df['close'])
```
- Example XNO's TA usage:
```python
from xno import CEIL

f = CEIL(df['close'])
```
### COS          -        Vector Trigonometric Cos
Calculates the Vector Trigonometric Cos.

```python
xno.TimeseriesFeatures.cos(s1)
```
or 
```python
xno.COS(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cos(df['close'])
```
- Example XNO's TA usage:
```python
from xno import COS

f = COS(df['close'])
```
### COSH         -        Vector Trigonometric Cosh
Calculates the Vector Trigonometric Cosh.

```python
xno.TimeseriesFeatures.cosh(s1)
```
or 
```python
xno.COSH(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.cosh(df['close'])
```
- Example XNO's TA usage:
```python
from xno import COSH

f = COSH(df['close'])
```
### DIV          -        Vector Arithmetic Div
Calculates the Vector Arithmetic Div.

```python
xno.TimeseriesFeatures.div(s1, s2)
```
or 
```python
xno.DIV(s1, s2)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.div(df['close'], df['volume'])
```
- Example XNO's TA usage:
```python
from xno import DIV

f = DIV(df['close'], df['volume'])
```
### EXP          -        Vector Arithmetic Exp
Calculates the Vector Arithmetic Exp.

```python
xno.TimeseriesFeatures.exp(s1)
```
or 
```python
xno.EXP(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.exp(df['close'])
```
- Example XNO's TA usage:
```python
from xno import EXP

f = EXP(df['close'])
```
### FLOOR        -        Vector Floor
Calculates the Vector Floor.

```python
xno.TimeseriesFeatures.floor(s1)
```
or 
```python
xno.FLOOR(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.floor(df['close'])
```
- Example XNO's TA usage:
```python
from xno import FLOOR

f = FLOOR(df['close'])
```
### LN           -        Vector Log Natural
Calculates the Vector Log Natural.

```python
xno.TimeseriesFeatures.ln(s1)
```
or 
```python
xno.LN(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.ln(df['close'])
```
- Example XNO's TA usage:
```python
from xno import LN

f = LN(df['close'])
```
### LOG10        -        Vector Log10
Calculates the Vector Log10.

```python
xno.TimeseriesFeatures.log10(s1)
```
or 
```python
xno.LOG10(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.log10(df['close'])
```
- Example XNO's TA usage:
```python
from xno import LOG10

f = LOG10(df['close'])
```
### MAX          -        Highest value over a specified period
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
### MAXINDEX     -        Index of highest value over a specified period
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
### MIN          -        Lowest value over a specified period
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
### MININDEX     -        Index of lowest value over a specified period
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
### MINMAX       -        Lowest and highest values over a specified period
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
### MINMAXINDEX  -        Indexes of lowest and highest values over a specified period
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
### MULT         -        Vector Arithmetic Mult
Calculates the Vector Arithmetic Mult.

```python
xno.TimeseriesFeatures.mult(s1, s2)
```
or 
```python
xno.MULT(s1, s2)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.mult(df['close'], df['volume'])
```
- Example XNO's TA usage:
```python
from xno import MULT

f = MULT(df['close'], df['volume'])
```
### SUB          -        Vector Arithmetic Subtraction
Calculates the Vector Arithmetic Subtraction.

```python
xno.TimeseriesFeatures.sub(s1, s2)
```
or 
```python
xno.SUB(s1, s2)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sub(df['close'], df['volume'])
```
- Example XNO's TA usage:
```python
from xno import SUB

f = SUB(df['close'], df['volume'])
```
### SUM          -        Summation
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
### SIN          -        Vector Trigonometric Sin
Calculates the Vector Trigonometric Sin.

```python
xno.TimeseriesFeatures.sin(s1)
```
or 
```python
xno.SIN(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sin(df['close'])
```
- Example XNO's TA usage:
```python
from xno import SIN

f = SIN(df['close'])
```
### SINH         -        Vector Trigonometric Sinh
Calculates the Vector Trigonometric Sinh.

```python
xno.TimeseriesFeatures.sinh(s1)
```
or 
```python
xno.SINH(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sinh(df['close'])
```
- Example XNO's TA usage:
```python
from xno import SINH

f = SINH(df['close'])
```
### SQRT         -        Vector Square Root
Calculates the Vector Square Root.

```python
xno.TimeseriesFeatures.sqrt(s1)
```
or 
```python
xno.SQRT(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.sqrt(df['close'])
```
- Example XNO's TA usage:
```python
from xno import SQRT

f = SQRT(df['close'])
```
### TAN          -        Vector Trigonometric Tan
Calculates the Vector Trigonometric Tan.

```python
xno.TimeseriesFeatures.tan(s1)
```
or 
```python
xno.TAN(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.tan(df['close'])
```
- Example XNO's TA usage:
```python
from xno import TAN

f = TAN(df['close'])
```
### TANH         -        Vector Trigonometric Tanh
Calculates the Vector Trigonometric Tanh.

```python
xno.TimeseriesFeatures.tanh(s1)
```
or 
```python
xno.TANH(s1)
```
- Example TimeseriesFeatures usage:
```python
from xno import TimeseriesFeatures

f = TimeseriesFeatures(df)
f.tanh(df['close'])
```
- Example XNO's TA usage:
```python
from xno import TANH

f = TANH(df['close'])
```