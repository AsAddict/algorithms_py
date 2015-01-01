"""Graph Search In Application Of Finding Path

Algorithm 4.1(p536)
Algorithm 4.2(p540)
Algorithm 4.4(p571) not covered since they are analogous
problems

For represent the basic and simple algorithm here we
bring the limitation: The graph's vertexs must be all
numbers and start from zero to the graph.v()-1 if we
sort them. Bringing a node type to track the path could
solve the problem.
"""

from stack import * # for collect path
from queue import * # for bfs search

class GraphSearch:
    def __init__(self, graph, source, bfs=True):
        vertex_num = graph.v()
        self._marked = [False]*vertex_num
        self._source = source
        self._g = graph
        self._edge_to = [None]*vertex_num
        if bfs:
            self._bfs()
        else:
            self._marked[source] = True
            self._dfs(source)

    def count(self):
        '''get the number of vertexs connects to source
        '''
        return self._marked.count(True)

    def has_path_to(self, v):
        ''' check whether v connect to the source
        '''
        return self._marked[v]

    def path_to(self, v):
        path = Stack()
        to = v
        path.push(to)
        while to != self._source:
            to = self._edge_to[to]
            path.push(to)
        return path

    def _bfs(self):
        ''' private, bread first search from the source
        '''
        f, m, s = Queue(), self._marked, self._source
        self._edge_to[s] = s
        f.push(s)
        m[s] = True
        while not f.is_empty():
            v = f.pop()
            for w in self._g.adj(v):
                if not m[w]:
                    m[w] = True
                    f.push(w)
                    self._edge_to[w] = v

    def _dfs(self, v):
        ''' private, depth first search from the source
        '''
        for w in self._g.adj(v):
            if not self._marked[w]:
                self._marked[w] = True
                self._edge_to[w] = v
                self._dfs(w)

import util
def test_client():
    print('\nTest For Graph Search:\n')
    g = util.read_graph("./data/tinyCG.txt", False)
    source = 0
    bfs = False # assign search strategy here
    search = GraphSearch(g, source, not bfs)
    print('BFS' if not bfs else 'DFS', 'search strategy')
    for v in range(g.v()):
        print(source, 'to', v, ':  ', end='')
        if search.has_path_to(v):
            for i in search.path_to(v):
                if i != v:
                    print(i, '-> ', end='')
                else:
                    print(i)
    print(search.count(), 'vertexs connect to the source', search._source)

# simple test on graph search
test_client()
