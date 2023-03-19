from .pitch import Pitch, Accidental, Octave
from .duration import Duration  # , CommonDuration


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
        pass
        # return Note(
        #     Pitch.A,
        #     Accidental.NATURAL,
        #     Octave.ONE_LINED,
        #     Duration(CommonDuration.QUARTER),
        # )

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
