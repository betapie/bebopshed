from .pitch import Pitch, Accidental, Octave
from .duration import Duration, CommonDuration
import re


class Note:
    def __init__(
        self,
        pitch: Pitch,
        accidental: Accidental,
        octave: Octave,
        duration: Duration,
    ):
        self.pitch = pitch
        self.accidental = accidental
        self.octave = octave
        self.duration = duration

    def from_str(string: str):
        reg_pattern = "^([cdefgab])(is|isis|es|eses)?(,*'*)([0-9]+)(\\.*)$"
        match = re.match(reg_pattern, string)
        groups = match.groups()

        if groups[0] == "c":
            pitch = Pitch.C
        elif groups[0] == "d":
            pitch = Pitch.D
        elif groups[0] == "e":
            pitch = Pitch.E
        elif groups[0] == "f":
            pitch = Pitch.F
        elif groups[0] == "g":
            pitch = Pitch.G
        elif groups[0] == "a":
            pitch = Pitch.A
        elif groups[0] == "b":
            pitch = Pitch.B

        if groups[1] == "is":
            accidental = Accidental.SHARP
        elif groups[1] == "isis":
            accidental = Accidental.DOUBLE_SHARP
        elif groups[1] == "es":
            accidental = Accidental.FLAT
        elif groups[1] == "eses":
            accidental = Accidental.DOUBLE_FLAT
        else:
            accidental = Accidental.NATURAL

        if groups[2] == ",,,":
            octave = Octave.SUB_CONTRA
        elif groups[2] == ",,":
            octave = Octave.CONTRA
        elif groups[2] == ",":
            octave = Octave.GREAT
        elif groups[2] == "'":
            octave = Octave.ONE_LINED
        elif groups[2] == "''":
            octave = Octave.TWO_LINED
        elif groups[2] == "'''":
            octave = Octave.THREE_LINED
        elif groups[2] == "''''":
            octave = Octave.FOUR_LINED
        elif groups[2] == "'''''":
            octave = Octave.FIVE_LINED
        elif groups[2] == "'''''":
            octave = Octave.SIX_LINED
        else:
            octave = Octave.SMALL

        dots = len(groups[4])

        if groups[3] == "1":
            duration = Duration(CommonDuration.WHOLE, dots)
        elif groups[3] == "2":
            duration = Duration(CommonDuration.HALF, dots)
        elif groups[3] == "4":
            duration = Duration(CommonDuration.QUARTER, dots)
        elif groups[3] == "8":
            duration = Duration(CommonDuration.EIGTH, dots)
        elif groups[3] == "16":
            duration = Duration(CommonDuration.SIXTEENTH, dots)

        return Note(pitch, accidental, octave, duration)

    def __str__(self):
        result = ""
        if self.pitch == Pitch.C:
            result += "c"
        elif self.pitch == Pitch.D:
            result += "d"
        elif self.pitch == Pitch.E:
            result += "e"
        elif self.pitch == Pitch.F:
            result += "f"
        elif self.pitch == Pitch.G:
            result += "g"
        elif self.pitch == Pitch.A:
            result += "a"
        elif self.pitch == Pitch.B:
            result += "b"

        if self.accidental == Accidental.SHARP:
            result += "is"
        elif self.accidental == Accidental.DOUBLE_SHARP:
            result += "isis"
        elif self.accidental == Accidental.FLAT:
            result += "es"
        elif self.accidental == Accidental.DOUBLE_FLAT:
            result += "eses"

        if self.octave in [Octave.OCTAVE_0, Octave.SUB_CONTRA]:
            result += ",,,"
        elif self.octave in [Octave.OCTAVE_1, Octave.CONTRA]:
            result += ",,"
        elif self.octave in [Octave.OCTAVE_2, Octave.GREAT]:
            result += ","
        elif self.octave in [Octave.OCTAVE_3, Octave.SMALL]:
            pass
        elif self.octave in [Octave.OCTAVE_4, Octave.ONE_LINED]:
            result += "'"
        elif self.octave in [Octave.OCTAVE_5, Octave.TWO_LINED]:
            result += "''"
        elif self.octave in [Octave.OCTAVE_6, Octave.THREE_LINED]:
            result += "'''"
        elif self.octave in [Octave.OCTAVE_7, Octave.FOUR_LINED]:
            result += "''''"
        elif self.octave in [Octave.OCTAVE_8, Octave.FIVE_LINED]:
            result += "'''''"
        elif self.octave in [Octave.OCTAVE_9, Octave.SIX_LINED]:
            result += "''''''"

        result += str(self.duration.base_duration.denominator)
        result += "." * self.duration.dots

        return result

    def __eq__(self, other):
        return (
            self.pitch == other.pitch
            and self.accidental == other.accidental
            and self.octave == other.octave
            and self.duration == other.duration
        )
