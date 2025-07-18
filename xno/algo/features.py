# Add ta-lib functions: https://ta-lib.org/functions/
from typing import Union

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
    ) -> np.ndarray:
        if series1 is None:
            series1 = self.df_ticker['High']
        if series2 is None:
            series2 = self.df_ticker['Low']
        if series3 is None:
            series3 = self.df_ticker['Close']

        return xts.ADX(series1, series2, series3, timeperiod)

    def sma(self, series: Union[np.array, pd.Series, None] = None, timeperiod=30) -> pd.Series:
        if series is None:
            series = self.df_ticker['Close']
        return xts.SMA(series, timeperiod)

    def macd(self, series: Union[np.array, pd.Series, None] = None, fastperiod=12, slowperiod=26, signalperiod=9) -> pd.Series:
        if series is None:
            series = self.df_ticker['Close']
        return xts.MACD(series, fastperiod, slowperiod, signalperiod)

    def roc(self, series: Union[np.array, pd.Series, None] = None, timeperiod=10) -> pd.Series:
        if series is None:
            series = self.df_ticker['Close']
        return xts.ROC(series, timeperiod)

    def lag(self, series: Union[np.array, pd.Series, None] = None, periods=1) -> pd.Series:
        if series is None:
            series = self.df_ticker['Close']
        return xts.LAG(series, periods)

    def rsi(self, series: Union[np.array, pd.Series, None] = None, timeperiod=14) -> pd.Series:
        if series is None:
            series = self.df_ticker['Close']
        return xts.RSI(series, timeperiod)

    def obv(self, series: Union[np.array, pd.Series, None] = None, series2: Union[np.array, pd.Series, None] = None) -> pd.Series:
        if series is None:
            series = self.df_ticker['Close']
        if series2 is None:
            series2 = self.df_ticker['Volume']
        return xts.OBV(series, series2)
