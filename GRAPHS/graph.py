from stack import *
from queue import *
class Graph(object):
    def __init__(self, directed = False, weighted = False):
        self._g = {}
        self._directed = directed
        self._weighted = weighted
        self._v = 0;

    
    def add_edge(self, f, e, w = 0):
        self._g.setdefault(f, {})[e] = w
        if self._directed:
            self._g.setdefault(e, {})
        else:
            self._g.setdefault(e, {})[f] = w


    def __repr__(self):
        return repr(self._g)


    def vertexs(self):
        froms = set(self._g.keys())
        if not self._directed:
            return froms
        for ends in self._g.values():            
            froms.update(ends.keys())
        return froms

    def is_directed(self):
        return self._directed

    def v(self):
        return len(self.vertexs())

    def adj(self, v):
        return self._g[v].keys()        
