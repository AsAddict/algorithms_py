class Stack(object):
    def __init__(self):
        self._data = list()

    def push(self, item):
        self._data.append(item)
        return item

    def __repr__(self):
        return repr(self._data)

    def pop(self):
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __getitem__(self, index):
        index = len(self._data) - 1 - index
        if index < 0: raise StopIteration
        return self._data[index] 

if __name__ == "__main__":            
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    for i in s:
        print(i)
