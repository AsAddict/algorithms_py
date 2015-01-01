from graph import *


def read_graph(path, directed):
    ''' construct a graph from file
    '''
    g = Graph(directed)
    with open(path) as lines:
        for i, l in enumerate(lines):
            if i >= 2:
                g.add_edge(*list(map(int, (l[:-1].split(' ')))))

    return g
