#!/usr/bin/env python3

from collections import defaultdict

# return the indices of the same element in the list ( [element,  [index1, index2]] )
def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ( (key,locs) for key,locs in tally.items() if len(locs)>1 )

