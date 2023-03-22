from enum import Enum
import re


class BasePitch(Enum):
    C = 0
    D = 2
    E = 4
    F = 5
    G = 7
    A = 9
    B = 11


class Accidental(Enum):
    NATURAL = 0
    FLAT = -1
    SHARP = 1
    DOUBLE_FLAT = -2
    DOUBLE_SHARP = 2


class Octave(Enum):
    OCTAVE_0 = 0
    SUB_CONTRA = 0
    OCTAVE_1 = 1
    CONTRA = 1
    OCTAVE_2 = 2
    GREAT = 2
    OCTAVE_3 = 3
    SMALL = 3
    OCTAVE_4 = 4
    ONE_LINED = 4
    OCTAVE_5 = 5
    TWO_LINED = 5
    OCTAVE_6 = 6
    THREE_LINED = 6
    OCTAVE_7 = 7
    FOUR_LINED = 7
    OCTAVE_8 = 8
    FIVE_LINED = 8
    OCTAVE_9 = 9
    SIX_LINED = 9


class Pitch:
    def __init__(
        self, pitch: BasePitch, accidental: Accidental, octave: Octave
    ):
        self.base_pitch = pitch
        self.accidental = accidental
        self.octave = octave

    def __eq__(self, other):
        return (
            self.base_pitch == other.base_pitch
            and self.accidental == other.accidental
            and self.octave == other.octave
        )

    def absolute_pitch(self) -> int:
        return (
            self.octave.value[0] * 12
            + self.base_pitch.value[0]
            + self.accidental.value[0]
        )

    def from_lily(string: str):
        reg_pattern = "^([cdefgab])(is|isis|es|eses)?(,*'*)$"
        match = re.match(reg_pattern, string)
        groups = match.groups()

        if groups[0] == "c":
            base_pitch = BasePitch.C
        elif groups[0] == "d":
            base_pitch = BasePitch.D
        elif groups[0] == "e":
            base_pitch = BasePitch.E
        elif groups[0] == "f":
            base_pitch = BasePitch.F
        elif groups[0] == "g":
            base_pitch = BasePitch.G
        elif groups[0] == "a":
            base_pitch = BasePitch.A
        elif groups[0] == "b":
            base_pitch = BasePitch.B

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

        return Pitch(base_pitch, accidental, octave)

    def to_lily(self):
        result = ""
        if self.base_pitch == BasePitch.C:
            result += "c"
        elif self.base_pitch == BasePitch.D:
            result += "d"
        elif self.base_pitch == BasePitch.E:
            result += "e"
        elif self.base_pitch == BasePitch.F:
            result += "f"
        elif self.base_pitch == BasePitch.G:
            result += "g"
        elif self.base_pitch == BasePitch.A:
            result += "a"
        elif self.base_pitch == BasePitch.B:
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

        return result
