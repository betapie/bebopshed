import unittest
from lily_proc.note import Note
from lily_proc.pitch import Pitch, BasePitch, Accidental, Octave
from lily_proc.duration import Duration, CommonDuration


class TestNote(unittest.TestCase):
    CASES = [
        (
            Note(
                Pitch(BasePitch.C, Accidental.NATURAL, Octave.ONE_LINED),
                Duration(CommonDuration.QUARTER),
            ),
            "c'4",
        ),
        (
            Note(
                Pitch(BasePitch.C, Accidental.NATURAL, Octave.OCTAVE_4),
                Duration(CommonDuration.QUARTER),
            ),
            "c'4",
        ),
        (
            Note(
                Pitch(BasePitch.D, Accidental.FLAT, Octave.TWO_LINED),
                Duration(CommonDuration.EIGTH),
            ),
            "des''8",
        ),
        (
            Note(
                Pitch(BasePitch.D, Accidental.SHARP, Octave.SMALL),
                Duration(CommonDuration.EIGTH),
            ),
            "dis8",
        ),
        (
            Note(
                Pitch(BasePitch.E, Accidental.FLAT, Octave.GREAT),
                Duration(CommonDuration.EIGTH),
            ),
            "ees,8",
        ),
        (
            Note(
                Pitch(BasePitch.E, Accidental.DOUBLE_FLAT, Octave.GREAT),
                Duration(CommonDuration.EIGTH),
            ),
            "eeses,8",
        ),
        (
            Note(
                Pitch(BasePitch.A, Accidental.DOUBLE_FLAT, Octave.GREAT),
                Duration(CommonDuration.EIGTH),
            ),
            "aeses,8",
        ),
        (
            Note(
                Pitch(BasePitch.G, Accidental.SHARP, Octave.ONE_LINED),
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
