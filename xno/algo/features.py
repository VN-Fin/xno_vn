# Add ta-lib functions: https://ta-lib.org/functions/
from typing import Union, Tuple

import numpy as np
import pandas as pd
import xno.timeseries as xts

class TimeseriesFeature:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the feature with the provided data.
        """
        self.df_ticker = df

    def adx(
            self,
            series1: Union[np.ndarray, pd.Series, None] = None,
            series2: Union[np.ndarray, pd.Series, None] = None,
            series3: Union[np.ndarray, pd.Series, None] = None,
            timeperiod=14
    ) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']
        if series2 is None:
            series2 = self.df_ticker['Low']  
        if series3 is None:
            series3 = self.df_ticker['Close']  

        return xts.ADX(series1, series2, series3, timeperiod)

    def sma(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.SMA(series, timeperiod)

    def macd(self, series: Union[np.ndarray, pd.Series, None] = None, fastperiod=12, slowperiod=26, signalperiod=9) -> Union[tuple, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MACD(series, fastperiod, slowperiod, signalperiod)

    def roc(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=10) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROC(series, timeperiod)

    def lag(self, series: Union[np.ndarray, pd.Series, None] = None, periods=1) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LAG(series, periods)

    def rsi(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.RSI(series, timeperiod)

    def obv(self, series: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        if series2 is None:
            series2 = self.df_ticker['Volume']  
        return xts.OBV(series, series2)

# OVERLAP 

    def bbands(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0) -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.BBANDS(series, timeperiod, nbdevup, nbdevdn, matype)

    def dema(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.DEMA(series, timeperiod)

    def ema(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.EMA(series, timeperiod)

    def ht_trendline(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.HT_TRENDLINE(series)

    def kama(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.KAMA(series, timeperiod)

    def ma(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30, matype=0) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MA(series, timeperiod, matype)

    def mama(self, series: Union[np.ndarray, pd.Series, None] = None, fastlimit=0, slowlimit=0) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MAMA(series, fastlimit, slowlimit)

    def mavp(self, series: Union[np.ndarray, pd.Series, None] = None, periods: Union[np.ndarray, pd.Series, None] = None, minperiod=2, maxperiod=30, matype=0) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        if periods is None:
            periods = np.full(len(series), 14)  
        return xts.MAVP(series, periods, minperiod, maxperiod, matype)

    def midpoint(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MIDPOINT(series, timeperiod)

    def midprice(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.MIDPRICE(high, low, timeperiod)

    def sar(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, acceleration=0, maximum=0) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.SAR(high, low, acceleration, maximum)

    def sarext(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.SAREXT(high, low, startvalue, offsetonreverse, accelerationinitlong, accelerationlong, accelerationmaxlong, accelerationinitshort, accelerationshort, accelerationmaxshort)

    def t3(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=5, vfactor=0) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.T3(series, timeperiod, vfactor)

    def tema(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.TEMA(series, timeperiod)

    def trima(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.TRIMA(series, timeperiod)

    def wma(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.WMA(series, timeperiod)

# MOMENTUM 

    def adxr(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.ADXR(high, low, close, timeperiod)

    def apo(self, series: Union[np.ndarray, pd.Series, None] = None, fastperiod=12, slowperiod=26, matype=0) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.APO(series, fastperiod, slowperiod, matype)

    def aroon(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.AROON(high, low, timeperiod)

    def aroonosc(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.AROONOSC(high, low, timeperiod)

    def bop(self, open_: Union[np.ndarray, pd.Series, None] = None, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if open_ is None:
            open_ = self.df_ticker['Open']  
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.BOP(open_, high, low, close)

    def cci(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.CCI(high, low, close, timeperiod)

    def cmo(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.CMO(series, timeperiod)

    def dx(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.DX(high, low, close, timeperiod)

    def macdext(self, series: Union[np.ndarray, pd.Series, None] = None, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0) -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MACDEXT(series, fastperiod, fastmatype, slowperiod, slowmatype, signalperiod, signalmatype)

    def macdfix(self, series: Union[np.ndarray, pd.Series, None] = None, signalperiod=9) -> Union[Tuple[np.ndarray, np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MACDFIX(series, signalperiod)

    def mfi(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, volume: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        if volume is None:
            volume = self.df_ticker['Volume']  
        return xts.MFI(high, low, close, volume, timeperiod)

    def minus_di(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.MINUS_DI(high, low, close, timeperiod)

    def minus_dm(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.MINUS_DM(high, low, timeperiod)

    def mom(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=10) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MOM(series, timeperiod)

    def plus_di(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.PLUS_DI(high, low, close, timeperiod)

    def plus_dm(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.PLUS_DM(high, low, timeperiod)

    def ppo(self, series: Union[np.ndarray, pd.Series, None] = None, fastperiod=12, slowperiod=26, matype=0) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.PPO(series, fastperiod, slowperiod, matype)

    def rocp(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=10) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROCP(series, timeperiod)

    def rocr(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=10) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROCR(series, timeperiod)

    def rocr100(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=10) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROCR100(series, timeperiod)

    def stoch(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.STOCH(high, low, close, fastk_period, slowk_period, slowk_matype, slowd_period, slowd_matype)

    def stochf(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, fastk_period=5, fastd_period=3, fastd_matype=0) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.STOCHF(high, low, close, fastk_period, fastd_period, fastd_matype)

    def stochrsi(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.STOCHRSI(series, timeperiod, fastk_period, fastd_period, fastd_matype)

    def trix(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.TRIX(series, timeperiod)

    def ultosc(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod1=7, timeperiod2=14, timeperiod3=28) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.ULTOSC(high, low, close, timeperiod1, timeperiod2, timeperiod3)

    def willr(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.WILLR(high, low, close, timeperiod)

# VOLUME 

    def ad(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, volume: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        if volume is None:
            volume = self.df_ticker['Volume']  
        return xts.AD(high, low, close, volume)

    def adosc(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, volume: Union[np.ndarray, pd.Series, None] = None, fastperiod=3, slowperiod=10) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        if volume is None:
            volume = self.df_ticker['Volume']  
        return xts.ADOSC(high, low, close, volume, fastperiod, slowperiod)

# VOLATILITY 

    def atr(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.ATR(high, low, close, timeperiod)

    def natr(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.NATR(high, low, close, timeperiod)

    def trange(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.TRANGE(high, low, close)

# CYCLE 

    def ht_dcperiod(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.HT_DCPERIOD(series)

    def ht_dcphase(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.HT_DCPHASE(series)

    def ht_phasor(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.HT_PHASOR(series)

    def ht_sine(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.HT_SINE(series)

    def ht_trendmode(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.HT_TRENDMODE(series)

# PRICE 

    def avgprice(self, open_: Union[np.ndarray, pd.Series, None] = None, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if open_ is None:
            open_ = self.df_ticker['Open']  
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.AVGPRICE(open_, high, low, close)

    def medprice(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        return xts.MEDPRICE(high, low)

    def typprice(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.TYPPRICE(high, low, close)

    def wclprice(self, high: Union[np.ndarray, pd.Series, None] = None, low: Union[np.ndarray, pd.Series, None] = None, close: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if high is None:
            high = self.df_ticker['High']  
        if low is None:
            low = self.df_ticker['Low']  
        if close is None:
            close = self.df_ticker['Close']  
        return xts.WCLPRICE(high, low, close)

