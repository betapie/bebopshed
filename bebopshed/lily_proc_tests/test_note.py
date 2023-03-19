import sys
import os
import unittest
from fractions import Fraction

# TODO: Maybe use setuptools instead?
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lily_proc.note import Note  # noqa: E402
from lily_proc.pitch import Pitch, Accidental, Octave  # noqa: E402
from lily_proc.duration import Duration, CommonDuration  # noqa: E402


class TestNote(unittest.TestCase):
    def test_str(self):
        cases = [
            (
                Note(
                    Pitch.C,
                    Accidental.NATURAL,
                    Octave.ONE_LINED,
                    Duration(CommonDuration.QUARTER),
                ),
                "c'4",
            ),
            (
                Note(
                    Pitch.C,
                    Accidental.NATURAL,
                    Octave.OCTAVE_4,
                    Duration(Fraction(1, 4)),
                ),
                "c'4",
            ),
            (
                Note(
                    Pitch.D,
                    Accidental.FLAT,
                    Octave.TWO_LINED,
                    Duration(Fraction(1, 8)),
                ),
                "des''8",
            ),
            (
                Note(
                    Pitch.D,
                    Accidental.SHARP,
                    Octave.SMALL,
                    Duration(Fraction(1, 8)),
                ),
                "dis8",
            ),
            (
                Note(
                    Pitch.E,
                    Accidental.FLAT,
                    Octave.GREAT,
                    Duration(Fraction(1, 8)),
                ),
                "ees,8",
            ),
            (
                Note(
                    Pitch.E,
                    Accidental.DOUBLE_FLAT,
                    Octave.GREAT,
                    Duration(CommonDuration.EIGTH),
                ),
                "eeses,8",
            ),
            (
                Note(
                    Pitch.A,
                    Accidental.DOUBLE_FLAT,
                    Octave.GREAT,
                    Duration(Fraction(1, 8)),
                ),
                "aeses,8",
            ),
            (
                Note(
                    Pitch.G,
                    Accidental.SHARP,
                    Octave.ONE_LINED,
                    Duration(Fraction(1, 4), dots=2),
                ),
                "gis'4..",
            ),
        ]

        for note, string in cases:
            self.assertEqual(str(note), string)


if __name__ == "__main__":
    unittest.main()
