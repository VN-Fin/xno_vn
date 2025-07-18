
import numpy as np
from numba.np.arrayobj import sliding_window_view
from scipy.stats import rankdata


__all__ = [
    'ROLLING_MEAN',
    'ROLLING_MAX',
    'ROLLING_MIN',
    'ROLLING_STD',
    'ROLLING_SUM',
    'ROLLING_PROD',
    'ROLLING_RANK',
    'ROLLING_CORRELATION',
    'ROLLING_COVARIANCE',
    'ROLLING_MEDIAN'
]

def rolling_apply(x, window, func, **kwargs):
    """
    Apply a function over a rolling window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
        func (callable): Function to apply over the rolling window.
        **kwargs: Additional keyword arguments to pass to the function.
    """
    x = np.asarray(x, dtype=float)
    n = len(x)
    if window > n or window < 1:
        return np.full_like(x, np.nan, dtype=float)

    view = sliding_window_view(x, window)
    result = np.array([func(window_slice, **kwargs) for window_slice in view], dtype=float)
    padded = np.full(n, np.nan, dtype=float)
    padded[window - 1:] = result
    return padded


def ROLLING_MEAN(x, window):
    """
    Apply a rolling mean function over a specified window.
    """
    return rolling_apply(x, window, np.mean)

def ROLLING_MAX(x, window):
    """
    Apply a rolling maximum function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, np.max)

def ROLLING_MIN(x, window):
    """
    Apply a rolling minimum function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, np.min)

def ROLLING_STD(x, window):
    """
    Apply a rolling standard deviation function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, np.std)

def ROLLING_SUM(x, window):
    """
    Apply a rolling sum function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, np.sum)

def ROLLING_PROD(x, window):
    """
    Apply a rolling product function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, np.prod)

def ROLLING_RANK(x, window):
    """
    Apply a rolling rank function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, rankdata)

def ROLLING_CORRELATION(x, y, window):
    """
    Calculate rolling correlation between two arrays over a specified window.
    Args:
        x (array-like): First input array.
        y (array-like): Second input array.
        window (int): Size of the rolling window.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if len(y) != n or window > n:
        raise ValueError("Mismatched input lengths or window too large.")

    x_view = sliding_window_view(x, window)
    y_view = sliding_window_view(y, window)
    corr = np.array([np.corrcoef(xv, yv)[0, 1] for xv, yv in zip(x_view, y_view)], dtype=float)

    result = np.full(n, np.nan, dtype=float)
    result[window - 1:] = corr
    return result

def ROLLING_COVARIANCE(x, y, window):
    """
    Calculate rolling covariance between two arrays over a specified window.
    Args:
        x (array-like): First input array.
        y (array-like): Second input array.
        window (int): Size of the rolling window.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if len(y) != n or window > n:
        raise ValueError("Mismatched input lengths or window too large.")

    x_view = sliding_window_view(x, window)
    y_view = sliding_window_view(y, window)
    cov = np.array([np.cov(xv, yv)[0, 1] for xv, yv in zip(x_view, y_view)], dtype=float)

    result = np.full(n, np.nan, dtype=float)
    result[window - 1:] = cov
    return result

def ROLLING_MEDIAN(x, window):
    """
    Apply a rolling median function over a specified window.
    Args:
        x (array-like): Input array.
        window (int): Size of the rolling window.
    """
    return rolling_apply(x, window, np.median)
