from fractions import Fraction
from typing import TypeVar, Optional, Type
from .duration import Duration

T = TypeVar("T", bound="MusicObject")

class MusicObject:
    @staticmethod
    def from_lily() -> Optional[T]:
        pass

    def to_lily(self) -> str:
        return ""

    def duration_value(self) -> Fraction:
        return Fraction()


class BarLine(MusicObject):
    def to_lily(self):
        return "|"


class Break(MusicObject):
    def to_lily(self):
        return " \\break "


class Tie(MusicObject):
    def to_lily(self):
        return "~"


class Rest(MusicObject):
    def __init__(self, duration: Duration):
        self.duration = duration

    @staticmethod
    def from_lily(lily_str: str) -> Optional["Rest"]:
        return Rest(Duration.from_lily(lily_str[1:]))

    def to_lily(self):
        return "r" + self.duration.to_lily()

    def duration_value(self):
        return self.duration.value()
