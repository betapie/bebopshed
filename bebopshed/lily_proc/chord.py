import copy
from enum import Enum
from typing import Optional

from .bar import Bar
from .duration import CommonDuration, Duration
from .note import Note
from .pitch import Key


class Quality(Enum):
    MAJOR = 0
    MINOR = 1


class Chord:
    def __init__(self, key: Key, duration: Duration, quality: Quality, decorators: str):
        self.key = key
        self.duration = duration
        self.quality = quality
        self.decorators = decorators

    @staticmethod
    def from_lily(string: str):
        colon_idx = None
        for idx, c in enumerate(string):
            if c == ":":
                colon_idx = idx

        if colon_idx is not None:
            note = Note.from_lily(string[:colon_idx])
            if colon_idx + 1 < len(string) and string[colon_idx + 1] == "m":
                quality = Quality.MINOR
                decorators = string[colon_idx + 2 :]
            else:
                quality = Quality.MAJOR
                decorators = string[colon_idx + 1 :]
        else:
            note = Note.from_lily(string)
            quality = Quality.MAJOR
            decorators = ""

        key = Key(note.pitch.base_pitch, note.pitch.accidental)
        duration = note.duration if note.duration else Duration(CommonDuration.WHOLE)

        return Chord(key, duration, quality, decorators)

    def to_lily(self):
        result = ""
        result += self.key.to_lily()
        result += self.duration.to_lily()
        result += ":"
        if self.quality == Quality.MINOR:
            result += "m"
        result += self.decorators
        return result

    def __eq__(self, other):
        return (
            self.key == other.key
            and self.duration == other.duration
            and self.quality == other.quality
            and self.decorators == other.decorators
        )


class Chords:
    def __init__(self, bars: list):
        self._bars = bars

    @staticmethod
    def from_lily(string: str):
        bars = []
        bar_strings = string.split("|")
        for bar_str in bar_strings:
            objects = []
            tokens = bar_str.split(" ")
            for token in tokens:
                if not token:
                    continue
                objects.append(Chord.from_lily(token))
            if not objects:
                continue
            bar = Bar(objects)
            bars.append(bar)

        return Chords(bars)

    def to_lily(self):
        result = ""
        for bar in self._bars[:-1]:
            result += bar.to_lily() + "\n"
        result += self._bars[-1].to_lily()
        return result

    def pad(self, length: Optional[int] = None):
        if not length:
            length = 1
            while length < len(self._bars):
                length *= 2
        to_append = max(length - len(self._bars), 0)
        to_cpy = self._bars[-1]
        for _ in range(to_append):
            self._bars.append(copy.deepcopy(to_cpy))
