# List of TA Functions

| TA Function          | Name                                      | Prototype                                                                          | Return Type                      |
| -------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------- |----------------------------------|
| AD                   | Chaikin A/D Line                          | `ad(high=None, low=None, close=None, volume=None)`                                 | Array                            |
| ADOSC                | Chaikin A/D Oscillator                    | `adosc(high=None, low=None, close=None, volume=None, fastperiod=3, slowperiod=10)` | Array                            |
| ADX                  | Average Directional Movement Index        | `adx(high=None, low=None, close=None, timeperiod=14)`                              | Array                            |
| ADXR                 | Average Directional Movement Rating       | `adxr(high=None, low=None, close=None, timeperiod=14)`                             | Array                            |
| APO                  | Absolute Price Oscillator                 | `apo(series=None, fastperiod=12, slowperiod=26, matype=0)`                         | Array                            |
| AROON                | Aroon                                     | `aroon(high=None, low=None, timeperiod=14)`                                        | aroondown, aroonup               |
| AROONOSC             | Aroon Oscillator                          | `aroonosc(high=None, low=None, timeperiod=14)`                                     | Array                            |
| ATR                  | Average True Range                        | `atr(high=None, low=None, close=None, timeperiod=14)`                              | Array                            |
| AVGPRICE             | Average Price                             | `avgprice(open_=None, high=None, low=None, close=None)`                            | Array                            |
| BBANDS               | Bollinger Bands                           | `bbands(close=None, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)`                 | upperband, middleband, lowerband |
| BETA                 | Beta                                      | `beta(s1, s2, timeperiod=5)`                                                       | Array                            |
| BOP                  | Balance of Power                          | `bop(open_=None, high=None, low=None, close=None)`                                 | Array                            |
| CCI                  | Commodity Channel Index                   | `cci(high=None, low=None, close=None, timeperiod=14)`                              | Array                            |
| CMO                  | Chande Momentum Oscillator                | `cmo(series=None, timeperiod=14)`                                                  | Array                            |
| CORREL               | Pearson Correlation Coefficient           | `correl(s1, s2, timeperiod=30)`                                                    | Array                            |
| DEMA                 | Double Exponential Moving Average         | `dema(series=None, timeperiod=30)`                                                 | Array                            |
| DIV                  | Division                                  | `div(s1, s2)`                                                                      | Array                            |
| DX                   | Directional Movement Index                | `dx(high=None, low=None, close=None, timeperiod=14)`                               | Array                            |
| EMA                  | Exponential Moving Average                | `ema(series=None, timeperiod=30)`                                                  | Array                            |
| HT\_DCPERIOD         | Hilbert Transform - Dominant Cycle Period | `ht_dcperiod(close=None)`                                                          | Array                            |
| HT\_DCPHASE          | Hilbert Transform - Dominant Cycle Phase  | `ht_dcphase(close=None)`                                                           | Array                            |
| HT\_PHASOR           | Hilbert Transform - Phasor Components     | `ht_phasor(close=None)`                                                            | inphase, quadrature              |
| HT\_SINE             | Hilbert Transform - SineWave              | `ht_sine(close=None)`                                                              | sine, leadsine                   |
| HT\_TRENDLINE        | Hilbert Transform - Trendline             | `ht_trendline(series=None)`                                                        | Array                            |
| HT\_TRENDMODE        | Hilbert Transform - Trend vs Cycle Mode   | `ht_trendmode(close=None)`                                                         | Array                            |
| KAMA                 | Kaufman Adaptive Moving Average           | `kama(series=None, timeperiod=30)`                                                 | Array                            |
| LAG                  | Lag (Shifted Series)                      | `lag(close=None, periods=1)`                                                       | Array                            |
| LINEARREG            | Linear Regression                         | `linearreg(s1, timeperiod=14)`                                                     | Array                            |
| LINEARREG\_ANGLE     | Linear Regression Angle                   | `linearreg_angle(s1, timeperiod=14)`                                               | Array                            |
| LINEARREG\_INTERCEPT | Linear Regression Intercept               | `linearreg_intercept(s1, timeperiod=14)`                                           | Array                            |
| LINEARREG\_SLOPE     | Linear Regression Slope                   | `linearreg_slope(s1, timeperiod=14)`                                               | Array                            |
| MACD                 | Moving Average Convergence/Divergence     | `macd(close=None, fastperiod=12, slowperiod=26, signalperiod=9)`                   | macd, signal, hist               |
| MACDEXT              | MACD with type options                    | `macdext(series=None, ...)`                                                        | macd, signal, hist               |
| MACDFIX              | MACD Fix Mode                             | `macdfix(series=None, signalperiod=9)`                                             | macd, signal, hist               |
| MA                   | Moving Average                            | `ma(series=None, timeperiod=30, matype=0)`                                         | Array                            |
| MAMA                 | MESA Adaptive Moving Average              | `mama(series=None, fastlimit=0, slowlimit=0)`                                      | mama, fama                       |
| MAVP                 | Moving Average with Variable Period       | `mavp(series=None, periods=None, minperiod=2, maxperiod=30, matype=0)`             | Array                            |
| MAX                  | Max over Period                           | `max(s1, timeperiod=30)`                                                           | Array                            |
| MAXINDEX             | Index of Max over Period                  | `maxindex(s1, timeperiod=30)`                                                      | Array                            |
| MEDPRICE             | Median Price                              | `medprice(high=None, low=None)`                                                    | Array                            |
| MFI                  | Money Flow Index                          | `mfi(high, low, close, volume, timeperiod=14)`                                     | Array                            |
| MIN                  | Min over Period                           | `min(s1, timeperiod=30)`                                                           | Array                            |
| MININDEX             | Index of Min over Period                  | `minindex(s1, timeperiod=30)`                                                      | Array                            |
| MINMAX               | Min and Max over Period                   | `minmax(s1, timeperiod=30)`                                                        | min, max                         |
| MINMAXINDEX          | Index of Min and Max                      | `minmaxindex(s1, timeperiod=30)`                                                   | Array                            |
| MINUS\_DI            | Minus Directional Indicator               | `minus_di(high, low, close, timeperiod=14)`                                        | Array                            |
| MINUS\_DM            | Minus Directional Movement                | `minus_dm(high, low, timeperiod=14)`                                               | Array                            |
| MOM                  | Momentum                                  | `mom(series=None, timeperiod=10)`                                                  | Array                            |
| OBV                  | On Balance Volume                         | `obv(close=None, volume=None)`                                                     | Array                            |
| PLUS\_DI             | Plus Directional Indicator                | `plus_di(high, low, close, timeperiod=14)`                                         | Array                            |
| PLUS\_DM             | Plus Directional Movement                 | `plus_dm(high, low, timeperiod=14)`                                                | Array                            |
| PPO                  | Percentage Price Oscillator               | `ppo(series=None, fastperiod=12, slowperiod=26, matype=0)`                         | Array                            |
| ROC                  | Rate of Change                            | `roc(close=None, timeperiod=10)`                                                   | Array                            |
| ROCP                 | Rate of Change Percentage                 | `rocp(series=None, timeperiod=10)`                                                 | Array                            |
| ROCR                 | Rate of Change Ratio                      | `rocr(series=None, timeperiod=10)`                                                 | Array                            |
| ROCR100              | Rate of Change Ratio 100 Scale            | `rocr100(series=None, timeperiod=10)`                                              | Array                            |
| RSI                  | Relative Strength Index                   | `rsi(close=None, timeperiod=14)`                                                   | Array                            |
| SAR                  | Parabolic SAR                             | `sar(high=None, low=None, acceleration=0, maximum=0)`                              | Array                            |
| SAREXT               | SAR - Extended Parameters                 | `sarext(...)`                                                                      | Array                            |
| SMA                  | Simple Moving Average                     | `sma(Close=None, timeperiod=30)`                                                   | Array                            |
| STOCH                | Stochastic Oscillator                     | `stoch(...)`                                                                       | slowk, slowd                     |
| STOCHF               | Stochastic Fast                           | `stochf(...)`                                                                      | fastk, fastd                     |
| STOCHRSI             | Stochastic RSI                            | `stochrsi(...)`                                                                    | fastk, fastd                   |
| SUM                  | Rolling Sum                               | `sum(s1, timeperiod=30)`                                                           | Array                            |
| T3                   | T3 Moving Average                         | `t3(series=None, timeperiod=5, vfactor=0)`                                         | Array                            |
| TEMA                 | Triple Exponential Moving Average         | `tema(series=None, timeperiod=30)`                                                 | Array                            |
| TRANGE               | True Range                                | `trange(high=None, low=None, close=None)`                                          | Array                            |
| TRIMA                | Triangular Moving Average                 | `trima(series=None, timeperiod=30)`                                                | Array                            |
| TRIX                 | TRIX Indicator                            | `trix(close=None, timeperiod=30)`                                                  | Array                            |
| TSF                  | Time Series Forecast                      | `tsf(s1, timeperiod=14)`                                                           | Array                            |
| TYPPRICE             | Typical Price                             | `typprice(high=None, low=None, close=None)`                                        | Array                            |
| ULTOSC               | Ultimate Oscillator                       | `ultosc(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)`          | Array                            |
| VAR                  | Variance                                  | `var(s1, timeperiod=5, nbdev=1)`                                                   | Array                            |
| VWAP                 | Volume Weighted Average Price             | `vwap(high, low, close, volume)`                                                   | Array                            |
| ROLLING\_VWAP        | Rolling VWAP                              | `rolling_vwap(high, low, close, volume, window=20)`                                | Array                            |
| WCLPRICE             | Weighted Close Price                      | `wclprice(high=None, low=None, close=None)`                                        | Array                            |
| WMA                  | Weighted Moving Average                   | `wma(series=None, timeperiod=30)`                                                  | Array                            |

