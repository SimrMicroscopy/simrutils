import numpy as np

def normalize(data, axis=None, min=0, max=1):
    if axis:
        dmin = data.min(axis=axis, keepdims=True)
        dmax = data.max(axis=axis, keepdims=True)

        normed = (data - dmin)/(dmax - dmin)
        return normed
