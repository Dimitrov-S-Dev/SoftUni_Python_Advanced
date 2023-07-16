class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "o", "e", "i", "u", "y"]
        self.current_index = -1
        self.end = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index > self.end:
            raise StopIteration
        current_element = self.text[self.current_index].lower()
        if current_element in self.vowels:
            return self.text[self.current_index]
        return self.__next__()
