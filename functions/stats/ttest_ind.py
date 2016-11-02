import numpy as np
from scipy.stats import ttest_ind

name = 'ttest_ind'

info = {
    'function': 'ttest_ind',
    'docs': 'http://scipy.github.io/devdocs/generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind',
    'params': {
        'a': 'array',
        'b': 'array'
    }
}


def fn(data):
    a = [int(x) for x in data.get('a')]
    b = [int(x) for x in data.get('b')]
    result = ttest_ind(a, b)
    return {'statistics': result.statistic, 'pvalue': result.pvalue}
