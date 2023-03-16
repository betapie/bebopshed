from enum import Enum


class Pitch(Enum):
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
