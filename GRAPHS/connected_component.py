''' Finding connected components in a undirected graph
Algorithm 4.3(p544) in Algs4

basic idea we have is iterate vertexs by dfs search
'''

class CC:
    def __init__(self, g):
        if g.is_directed():
            raise Exception("Error: Undirected Graph Only!")
        v_num = g.v()
        self._id = [None] * v_num
        self._marked = [None] * v_num
        self._count = 0
        for v in range(v_num):
            if not self._marked[v]:
                self._dfs(g, v)
                self._count += 1

    def _dfs(self, g, v):
        self._marked[v] = True
        self._id[v] = self._count
        for i in g.adj(v):
            if not self._marked[i]:
                self._dfs(g, i)

    def connected(self, v, w):
        self._id[v] == self._id[w]

    def id(self, v):
        return self._id[v]

    def count(self):
        return self._count

from util import *

def test_client():
    print('\nTest For Connected Component:')
    g = read_graph("./data/tinyG.txt", False)
    cc = CC(g)
    num = cc.count() # size component
    print(num, 'components here.')
    components = [[] for i in range(num)]
    for v in range(g.v()):
        components[cc.id(v)].append(v)
    for c in range(num):
        print(c, "component has vertexs: ", *components[c])

test_client()
