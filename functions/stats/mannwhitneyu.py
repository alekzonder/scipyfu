import numpy as np
from scipy.stats import mannwhitneyu

name = 'mannwhitneyu'
alias = 'mw'

info = {
    'alias': alias,
    'function': 'mannwhitneyu',
    'method': 'POST',
    'docs': 'http://scipy.github.io/devdocs/generated/scipy.stats.mannwhitneyu.html',
    'params': {
        'a': 'array',
        'b': 'array',
        'use_continuity': 'Bool',
        'alternative': 'String  "less", "two-sided", or "greater"'
    }
}


def fn(data):
    a = [float(x) for x in data.get('a')]
    b = [float(x) for x in data.get('b')]

    alternative = data.get('alternative', None)
    use_continuity = data.get('use_continuity', True)

    raw_result = mannwhitneyu(a, b, alternative=alternative, use_continuity=use_continuity)

    return dict(
        arguments=dict(
            alternative=alternative,
            use_continuity=use_continuity
        ),
        result={'statistics': raw_result[0], 'pvalue': raw_result[1]},
    )
