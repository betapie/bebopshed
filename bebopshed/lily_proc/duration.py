from enum import Enum


class CommonDuration(Enum):
    WHOLE = (1,)
    HALF = (2,)
    QUARTER = (4,)
    EIGTH = (8,)
    SIXTEENTH = (16,)


class Duration:
    def __init__(self, base_duration: CommonDuration, dots=0):
        self.base_duration = base_duration
        self.dots = dots

    def __eq__(self, other):
        return (
            self.base_duration == other.base_duration
            and self.dots == other.dots
        )
