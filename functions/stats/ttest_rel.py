import numpy as np
from scipy.stats import ttest_rel


name = 'ttest_rel'

info = {
    'function': 'ttest_rel',
    'method': 'POST',
    'docs': 'http://scipy.github.io/devdocs/generated/scipy.stats.ttest_rel.html#scipy.stats.ttest_rel',
    'params': {
        'a': 'array',
        'b': 'array'
    }
}


def fn(data):
    a = [int(x) for x in data.get('a')]
    b = [int(x) for x in data.get('b')]

    result = ttest_rel(a, b)

    return {'statistics': result.statistic, 'pvalue': result.pvalue}
