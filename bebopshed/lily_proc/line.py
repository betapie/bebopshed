from .music_object import BarLine, Rest
from .duration import Duration, CommonDuration


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

    def pad(self):
        bars = sum(isinstance(obj, BarLine) for obj in self._objects)
        power = 1
        while power < bars:
            power *= 2
        to_append = power - bars
        print(f"bars: {bars}, power: {power}, to_append: {to_append}")
        for _ in range(to_append):
            self._objects.extend(
                [Rest(Duration(CommonDuration.WHOLE)), BarLine()]
            )
