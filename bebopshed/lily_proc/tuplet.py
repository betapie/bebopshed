from fractions import Fraction

from .music_object import MusicObject


class Tuplet(MusicObject):
    def __init__(self, rational: Fraction, objects: list):
        self._rational = rational
        self._objects = objects

    def to_lily(self):
        inner = "{ " + " ".join(obj.to_lily() for obj in self._objects) + " }"
        return f"\\tuplet {self._rational} {inner}"

    def duration_value(self) -> Fraction:
        result = Fraction()
        for obj in self._objects:
            result += obj.duration_value()
        return result / self._rational
