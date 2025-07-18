from .price import *
from .technicals.overlap import *
from .technicals.volume import *
from .technicals.momentum import *
from .technicals.volatility import *
from .technicals.cycle import *
from .pattern.candles import *
from .pattern.charts import *
from .statistical import *
from .math import *

from .smc import *
from .window import *

import numpy as np



def LAG(x, periods: int = 1):
    """
    shift time series data by a specified number of periods.
    Args:
        x (array-like): Input array to shift.
        periods (int): Number of periods to shift. Positive for backward shift, negative for forward shift.
    """
    x = np.asarray(x)

    # ----- handle scalars --------------------------------------------------
    if x.ndim == 0:          # constant value, nothing to shift
        return x

    # ----- handle vectors --------------------------------------------------
    if periods == 0:
        return x

    result = np.full_like(x, np.nan)
    if periods > 0:
        if periods < len(x):
            result[periods:] = x[:-periods]
    else:                    # periods < 0  ➜ shift forward
        if -periods < len(x):
            result[:periods] = x[-periods:]
    return result


def CROSS(a, b):
    """
    Detect crossover (AFL: Cross).
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return (a > b) & (LAG(a, 1) <= LAG(b, 1))

def ABOVE(a, b):
    """
    Check if array 'a' is above array 'b'.
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return a > b

def BELOW(a, b):
    """
    Check if array 'a' is below array 'b'.
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return a < b

def EQUAL(a, b):
    """
    Check if array 'a' is equal to array 'b'.
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return a == b

def NOT_EQUAL(a, b):
    """
    Check if array 'a' is not equal to array 'b'.
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return a != b

def AND(a, b):
    """
    Element-wise logical AND operation.
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return np.logical_and(a, b)

def OR(a, b):
    """
    Element-wise logical OR operation.
    Args:
        a (array-like): First input array.
        b (array-like): Second input array.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return np.logical_or(a, b)
