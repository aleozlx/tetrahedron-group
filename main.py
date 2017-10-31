import os, sys
import numpy as np
from collections import deque, OrderedDict
import unittest, random, itertools

class TetrahedronOrientation(tuple):
    actions = OrderedDict([
        ('u', [0, 2, 3, 1]), ('u2', [0, 3, 1, 2]),
        ('v', [3, 1, 0, 2]), ('v2', [2, 1, 3, 0]),
        ('y', [1, 3, 2, 0]), ('y2', [3, 0, 2, 1]),
        ('z', [2, 0, 1, 3]), ('z2', [1, 2, 0, 3])
    ])

    def permutate(self, order):
        return TetrahedronOrientation(np.array(self)[order])
        
    def rotate(self, direction):
        return self.permutate(TetrahedronOrientation.actions[direction])
        
    def rotations(self):
        for action in TetrahedronOrientation.actions:
            yield self.rotate(action)

a = TetrahedronOrientation(np.arange(4))

def bfs_tetrahedron_symmetry(s):
    counter = itertools.count(1)
    visited = set()
    discover = dict()
    predecessor = dict()
    results = (discover, predecessor)

    queue = deque([s])
    discover[s] = next(counter)

    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.add(u)
            discovered = [[v, next(counter)] for v in u.rotations() if v not in visited]
            queue.extend(v for v,dv in discovered)
            discover.update({v:dv for v,dv in discovered})
            for v,dv in discovered:
                predecessor[v] = u

    return results

tetrahedron_symmetry_discovery, tetrahedron_symmetry_predecessor = bfs_tetrahedron_symmetry(a)
print(len(tetrahedron_symmetry_discovery))
