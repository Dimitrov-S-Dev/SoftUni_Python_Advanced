class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type):
        try:
            decoration = next(filter(lambda d: d.__class__.__name__ == decoration_type, self.decorations))
            return decoration
        except StopIteration:
            return "None"
