from .music_token import BarLine


class Line:
    def __init__(self, objects: list):
        self._objects = objects

    def to_lily(self):
        result = ""
        for obj in self._objects[:-1]:
            result += obj.to_lily()
            if isinstance(obj, BarLine):
                result += '\n'
            else:
                result += ' '
        result += self._objects[-1].to_lily()
        return result
