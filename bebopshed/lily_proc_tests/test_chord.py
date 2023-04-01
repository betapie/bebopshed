import unittest
from lily_proc.chord import Chord, Quality
from lily_proc.pitch import Key, BasePitch, Accidental
from lily_proc.duration import Duration, CommonDuration


class TestChord(unittest.TestCase):
    CASES = [
        (
            "aes2:7",
            Chord(
                Key(BasePitch.A, Accidental.FLAT),
                Duration(CommonDuration.HALF),
                Quality.MAJOR,
                "7",
            ),
        ),
        (
            "d1:m7",
            Chord(
                Key(BasePitch.D, Accidental.NATURAL),
                Duration(CommonDuration.WHOLE),
                Quality.MINOR,
                "7",
            ),
        ),
        (
            "e2:m7-5",
            Chord(
                Key(BasePitch.E, Accidental.NATURAL),
                Duration(CommonDuration.HALF),
                Quality.MINOR,
                "7-5",
            ),
        ),
        (
            "des1:7+",
            Chord(
                Key(BasePitch.D, Accidental.FLAT),
                Duration(CommonDuration.WHOLE),
                Quality.MAJOR,
                "7+",
            ),
        ),
    ]

    def test_from_lily(self):
        for lily_str, chord in self.CASES:
            self.assertEqual(Chord.from_lily(lily_str), chord)

    def test_to_lily(self):
        for lily_str, chord in self.CASES:
            self.assertEqual(lily_str, chord.to_lily())

    def test_from_lily_to_lily(self):
        for lily_str, _ in self.CASES:
            self.assertEqual(lily_str, Chord.from_lily(lily_str).to_lily())

    def test_to_lily_from_lily(self):
        for _, chord in self.CASES:
            self.assertEqual(chord, Chord.from_lily(chord.to_lily()))
