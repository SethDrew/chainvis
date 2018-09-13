import numpy as np


def get_flip_totals():
    from itertools import groupby
    from collections import Counter

    flips = np.load("static/chainresults/flip_history.npy")

    flips = [tuple(x) for x in flips]
    return dict(Counter(flips))


