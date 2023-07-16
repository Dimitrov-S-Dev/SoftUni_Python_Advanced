class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.start = len(self.collection) - 1
        self.end = 0
        self.current = self.start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < self.end:
            self.current = len(self.collection)
            raise StopIteration
        return self.collection[self.current]

