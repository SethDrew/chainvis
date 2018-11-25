import numpy as np
import collections

from itertools import groupby

from gerrychain.constraints.validity import Validator, single_flip_contiguous
from gerrychain.proposals import propose_random_flip
from gerrychain.accept import always_accept
from gerrychain.chain import MarkovChain
from gerrychain.defaults.grid import Grid


def get_flip_counts():
    # Make a 20x20 grid
    rows = 20
    cols = 20
    
    is_valid = Validator([single_flip_contiguous])
    
    grid = Grid((rows, cols))
    

    chain = MarkovChain(propose_random_flip, is_valid, always_accept, grid, total_steps=200)
    history = [state.flips for state in chain]
    history = [h for h in history if h is not None]

    flips = [k for item in history for k, v in item.items()]
    inds = [tuple_to_index(coord, rows) for coord in flips]
    keys = [i for i in range(rows * cols)]
    inds = inds + keys
    # base = collections.Counter(keys)
    inds = collections.Counter(inds)
    return dict(inds), { tuple_to_index(k, rows): v for k, v in grid.assignment.items() }

def get_partition():
    history = mk_grid()

def tuple_to_index(coord, rows):
    return coord[1] * rows + coord[0] 
