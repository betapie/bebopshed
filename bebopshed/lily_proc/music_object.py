from .duration import Duration


class MusicObject:
    def from_lily():
        pass

    def to_lily():
        pass


class BarLine(MusicObject):
    def to_lily(self):
        return "|"


class Tie(MusicObject):
    def to_lily(self):
        return "~"


class Rest(MusicObject):
    def __init__(self, duration: Duration):
        self.duration = duration

    def from_lily(lily_str: str):
        return Rest(Duration.from_lily(lily_str[1:]))

    def to_lily(self):
        return "r" + self.duration.to_lily()
