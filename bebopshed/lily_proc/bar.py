from fractions import Fraction

from .duration import CommonDuration, Duration


class Bar:
    def __init__(self, objects: list, duration=Duration(CommonDuration.WHOLE)):
        self._objects = objects
        self._duration = duration

    def duration_value(self) -> Fraction:
        if isinstance(self._duration, Duration):
            return self._duration.value()
        return self._duration

    def duration_check(self) -> bool:
        total_dur = Fraction()
        for obj in self._objects:
            dur = obj.duration_value()
            total_dur += dur
        return total_dur == self.duration_value()

    def to_lily(self):
        result = " ".join(obj.to_lily() for obj in self._objects)
        return result + " |"
