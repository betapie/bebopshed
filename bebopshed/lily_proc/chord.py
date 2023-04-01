from enum import Enum
from .pitch import Key
from .duration import Duration
from .note import Note


class Quality(Enum):
    MAJOR = 0
    MINOR = 1


class Chord:
    def __init__(
        self,
        key: Key,
        duration: Duration,
        quality: Quality,
        decorators: str
    ):
        self.key = key
        self.duration = duration
        self.quality = quality
        self.decorators = decorators

    def from_lily(string: str):
        colon_idx = string.index(":")
        note = Note.from_lily(string[:colon_idx])
        key = Key(note.pitch.base_pitch, note.pitch.accidental)
        if colon_idx + 1 < len(string) and string[colon_idx + 1] == "m":
            quality = Quality.MINOR
            decorators = string[colon_idx + 2:]
        else:
            quality = Quality.MAJOR
            decorators = string[colon_idx + 1:]

        return Chord(
            key,
            note.duration,
            quality,
            decorators
        )

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
