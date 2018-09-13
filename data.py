import numpy as np


def get_flip_totals():
    from itertools import groupby
    from collections import Counter

    flips = np.load("static/chainresults/flip_history.npy")

    flips = [tuple(x) for x in flips]
    flips = dict(Counter(flips))

    index_flips = dict()

    for flip in flips.keys():
    	index_flips[tuple_to_index(flip)] = flips[flip]

    return index_flips


def tuple_to_index(coord):
	return coord[1]*10 + coord[0]


from itertools import groupby
from collections import Counter

flips = np.load("static/chainresults/flip_history.npy")

flips = [tuple(x) for x in flips]
flips = dict(Counter(flips))

index_flips = dict()

for flip in flips.keys():
	index_flips[tuple_to_index(flip)] = flips[flip]

