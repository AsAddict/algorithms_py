class Bag(object):
    def __init__(self):
        self.items = list()
        self._N = 0

    def is_empty(self):
        return self._N == 0

    def size(self):
        return self._N

    def add(self, item):
        self._items.append(item)
        self._N += 1

    def __repr__(self):        
        return repr(self._items)
    
    def __iter__(self):
        return iter(self._items)
