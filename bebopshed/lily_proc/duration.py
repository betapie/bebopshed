from enum import Enum
import re


class CommonDuration(Enum):
    WHOLE = (1,)
    HALF = (2,)
    QUARTER = (4,)
    EIGTH = (8,)
    SIXTEENTH = (16,)
    THIRTYSECOND = (32,)


class Duration:
    def __init__(self, base_duration: CommonDuration, dots=0):
        self.base_duration = base_duration
        self.dots = dots

    def __eq__(self, other):
        return (
            self.base_duration == other.base_duration
            and self.dots == other.dots
        )

    def from_lily(string: str):
        if not string:
            return None
        reg_pattern = "^([0-9]+)(\\.*)$"
        match = re.match(reg_pattern, string)
        groups = match.groups()

        dots = len(groups[1])

        if groups[0] == "1":
            common_duration = CommonDuration.WHOLE
        elif groups[0] == "2":
            common_duration = CommonDuration.HALF
        elif groups[0] == "4":
            common_duration = CommonDuration.QUARTER
        elif groups[0] == "8":
            common_duration = CommonDuration.EIGTH
        elif groups[0] == "16":
            common_duration = CommonDuration.SIXTEENTH
        elif groups[0] == "32":
            common_duration = CommonDuration.THIRTYSECOND

        return Duration(common_duration, dots)

    def to_lily(self):
        result = ""
        result += str(self.base_duration.value[0])
        result += "." * self.dots
        return result
