import re
from enum import Enum

from .lily_error import LilyParseError


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
    SUB_CONTRA = 0
    CONTRA = 1
    GREAT = 2
    SMALL = 3
    ONE_LINED = 4
    TWO_LINED = 5
    THREE_LINED = 6
    FOUR_LINED = 7
    FIVE_LINED = 8
    SIX_LINED = 9


class Pitch:
    def __init__(self, pitch: BasePitch, accidental: Accidental, octave: Octave):
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
        return self.octave.value * 12 + self.base_pitch.value + self.accidental.value

    @staticmethod
    def from_lily(string: str):
        reg_pattern = "^([cdefgab])(is|isis|s|ses|es|eses)?(,*'*)$"
        match = re.match(reg_pattern, string)
        groups = match.groups()
        if not groups or len(groups) < 3:
            raise LilyParseError(f"Pitch.from_lily: invalid pattern: {string}")

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
        elif groups[1] in ["s", "es"]:
            accidental = Accidental.FLAT
        elif groups[1] in ["ses", "eses"]:
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

        if self.octave == Octave.SUB_CONTRA:
            result += ",,,"
        elif self.octave == Octave.CONTRA:
            result += ",,"
        elif self.octave == Octave.GREAT:
            result += ","
        elif self.octave == Octave.SMALL:
            pass
        elif self.octave == Octave.ONE_LINED:
            result += "'"
        elif self.octave == Octave.TWO_LINED:
            result += "''"
        elif self.octave == Octave.THREE_LINED:
            result += "'''"
        elif self.octave == Octave.FOUR_LINED:
            result += "''''"
        elif self.octave == Octave.FIVE_LINED:
            result += "'''''"
        elif self.octave == Octave.SIX_LINED:
            result += "''''''"

        return result


class Key:
    def __init__(self, pitch: BasePitch, accidental: Accidental):
        self.base_pitch = pitch
        self.accidental = accidental

    def __eq__(self, other):
        return (
            self.base_pitch == other.base_pitch and self.accidental == other.accidental
        )

    @staticmethod
    def from_lily(string: str):
        reg_pattern = "^([cdefgab])(is|isis|s|ses|es|eses)?$"
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
        elif groups[1] in ["s", "es"]:
            accidental = Accidental.FLAT
        elif groups[1] in ["ses", "eses"]:
            accidental = Accidental.DOUBLE_FLAT
        else:
            accidental = Accidental.NATURAL

        return Key(base_pitch, accidental)

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

        return result
