

class Line:
    def __init__(self, objects: list):
        self._objects = []

    def to_lily(self):
        return " ".join(obj.to_lily for obj in self._objects)
