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

# STATISTIC 

    def beta(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None, timeperiod=5) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.BETA(series1, series2, timeperiod)

    def correl(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.CORREL(series1, series2, timeperiod)

    def linearreg(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LINEARREG(series, timeperiod)

    def linearreg_angle(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LINEARREG_ANGLE(series, timeperiod)

    def linearreg_intercept(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LINEARREG_INTERCEPT(series, timeperiod)

    def linearreg_slope(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LINEARREG_SLOPE(series, timeperiod)

    def stddev(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=5, nbdev=1) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.STDDEV(series, timeperiod, nbdev)

    def tsf(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=14) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.TSF(series, timeperiod)

    def var(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=5, nbdev=1) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.VAR(series, timeperiod, nbdev)

# MATH TRANSFORM

    def acos(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ACOS(series)

    def asin(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ASIN(series)

    def atan(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ATAN(series)

    def ceil(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.CEIL(series)

    def cos(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.COS(series)

    def cosh(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.COSH(series)

    def exp(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.EXP(series)

    def floor(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.FLOOR(series)

    def ln(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LN(series)

    def log10(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.LOG10(series)

    def sin(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.SIN(series)

    def sinh(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.SINH(series)

    def sqrt(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.SQRT(series)

    def tan(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.TAN(series)

    def tanh(self, series: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.TANH(series)

 # MATH 

    def add(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.ADD(series1, series2)

    def div(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.DIV(series1, series2)

    def max(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MAX(series, timeperiod)

    def maxindex(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MAXINDEX(series, timeperiod)

    def min(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MIN(series, timeperiod)

    def minindex(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MININDEX(series, timeperiod)

    def minmax(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MINMAX(series, timeperiod)

    def minmaxindex(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[Tuple[np.ndarray, np.ndarray], None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.MINMAXINDEX(series, timeperiod)

    def mult(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.MULT(series1, series2)

    def sub(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.SUB(series1, series2)

    def sum(self, series: Union[np.ndarray, pd.Series, None] = None, timeperiod=30) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.SUM(series, timeperiod)

# UTILITY & COMPARISON 

    def cross(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.CROSS(series1, series2)

    def above(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.ABOVE(series1, series2)

    def below(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.BELOW(series1, series2)

    def equal(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.EQUAL(series1, series2)

    def not_equal(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.NOT_EQUAL(series1, series2)

    def and_op(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.AND(series1, series2)

    def or_op(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.OR(series1, series2)

# ROLLING WINDOW 

    def rolling_mean(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_MEAN(series, window)

    def rolling_max(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_MAX(series, window)

    def rolling_min(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_MIN(series, window)

    def rolling_std(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_STD(series, window)

    def rolling_sum(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_SUM(series, window)

    def rolling_prod(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_PROD(series, window)

    def rolling_rank(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_RANK(series, window)

    def rolling_correlation(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.ROLLING_CORRELATION(series1, series2, window)

    def rolling_covariance(self, series1: Union[np.ndarray, pd.Series, None] = None, series2: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series1 is None:
            series1 = self.df_ticker['High']  
        if series2 is None:
            series2 = self.df_ticker['Low']  
        return xts.ROLLING_COVARIANCE(series1, series2, window)

    def rolling_median(self, series: Union[np.ndarray, pd.Series, None] = None, window=20) -> Union[np.ndarray, None]:
        if series is None:
            series = self.df_ticker['Close']  
        return xts.ROLLING_MEDIAN(series, window)