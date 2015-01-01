class Queue:    
    def __init__(self):
        self._data = list()
        self.push = self.enqueue
        self.pop = self.dequeue

    def enqueue(self, item):
        self._data.insert(0, item)
        return item

    def dequeue(self):
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0
