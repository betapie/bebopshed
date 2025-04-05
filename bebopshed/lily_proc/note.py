from fractions import Fraction

from .duration import Duration
from .music_object import MusicObject
from .pitch import Pitch


class Note(MusicObject):
    def __init__(
        self,
        pitch: Pitch,
        duration: Duration,
    ):
        self.pitch = pitch
        self.duration = duration

    def absolute_pitch(self) -> int:
        return self.pitch.absolute_pitch()

    @staticmethod
    def from_lily(string: str):
        sep = 0
        while sep < len(string) and string[sep] not in [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
        ]:
            sep += 1

        pitch_str = string[:sep]
        duration_str = string[sep:]

        pitch = Pitch.from_lily(pitch_str)
        duration = Duration.from_lily(duration_str)

        return Note(pitch, duration)

    def to_lily(self):
        return self.pitch.to_lily() + self.duration.to_lily()

    def duration_value(self) -> Fraction:
        return self.duration.value()

    def __eq__(self, other):
        return self.pitch == other.pitch and self.duration == other.duration
