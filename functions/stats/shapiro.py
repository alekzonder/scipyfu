import numpy as np
from scipy.stats import shapiro

name = 'shapiro'

info = {
    'function': 'shapiro',
    'method': 'POST',
    'docs': 'http://scipy.github.io/devdocs/generated/scipy.stats.shapiro.html#scipy.stats.shapiro',
    'params': {
        'a': 'array'
    }
}


def fn(data):
    a = [float(x) for x in data.get('a')]

    raw_result = shapiro(a)

    return dict(
        result={'statistics': raw_result[0], 'pvalue': raw_result[1]},
        raw_result=raw_result
    )
