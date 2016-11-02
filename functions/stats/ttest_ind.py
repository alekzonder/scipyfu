import numpy as np
from scipy.stats import ttest_ind

name = 'ttest_ind'

info = {
    'function': 'ttest_ind',
    'method': 'POST',
    'docs': 'http://scipy.github.io/devdocs/generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind',
    'params': {
        'a': 'array',
        'b': 'array',
        'equal_var': 'Bool'
    }
}


def fn(data):
    a = [float(x) for x in data.get('a')]
    b = [float(x) for x in data.get('b')]

    equal_var = True

    if len(a) != len(b):
        equal_var = False

    result = ttest_ind(a, b, equal_var=equal_var)

    return dict(
        arguments=dict(equal_var=equal_var),
        result={'statistics': result.statistic, 'pvalue': result.pvalue}
    )
