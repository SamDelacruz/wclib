"""Wordcounting function library"""

import re

def str_map(string):
    """Return a list of (string, count) tuples for reducing"""
    words = sorted(sanitize(string).split())
    return [(w, 1) for w in words]

def reduce(data):
    """Reduce a list of (string, count) tuples

    Count is number of occurances of the string
    in given list
    """
    ret = []
    prev = ('', 0)

    for word, num in data:
        if prev[0] == '':
            prev = (word, num)
        elif word == prev[0]:
            prev = (word, num + prev[1])
        else:
            ret.append(prev)
            prev = (word, num)

    return ret

def sanitize(string):
    """Strip non-alpha chars from string"""
    return re.sub("[^a-zA-Z]+", " ", string).lower()

def word_count(string):
    """Return list of (word, count) in a given string"""
    return reduce(str_map(string))
