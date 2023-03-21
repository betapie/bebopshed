import sys
import os
import unittest

# TODO: Maybe use setuptools instead?
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lily_proc.note import Note  # noqa: E402
from lily_proc.pitch import Pitch, Accidental, Octave  # noqa: E402
from lily_proc.duration import Duration, CommonDuration  # noqa: E402


class TestNote(unittest.TestCase):
    CASES = [
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
                Duration(CommonDuration.QUARTER),
            ),
            "c'4",
        ),
        (
            Note(
                Pitch.D,
                Accidental.FLAT,
                Octave.TWO_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            "des''8",
        ),
        (
            Note(
                Pitch.D,
                Accidental.SHARP,
                Octave.SMALL,
                Duration(CommonDuration.EIGTH),
            ),
            "dis8",
        ),
        (
            Note(
                Pitch.E,
                Accidental.FLAT,
                Octave.GREAT,
                Duration(CommonDuration.EIGTH),
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
                Duration(CommonDuration.EIGTH),
            ),
            "aeses,8",
        ),
        (
            Note(
                Pitch.G,
                Accidental.SHARP,
                Octave.ONE_LINED,
                Duration(CommonDuration.QUARTER, dots=2),
            ),
            "gis'4..",
        ),
    ]

    def test_to_str(self):
        for note, string in self.CASES:
            self.assertEqual(note.to_lily(), string)

    def test_from_str(self):
        for note, string in self.CASES:
            self.assertEqual(note, Note.from_lily(string))

    def test_from_str_to_str(self):
        for _, string in self.CASES:
            self.assertEqual(string, Note.from_lily(string).to_lily())

    def test_to_str_from_str(self):
        for note, _ in self.CASES:
            self.assertEqual(note, Note.from_lily(note.to_lily()))


if __name__ == "__main__":
    unittest.main()
