import unittest
from lily_proc.line import Line
from lily_proc.note import Note
from lily_proc.pitch import Pitch, BasePitch, Accidental, Octave
from lily_proc.duration import Duration, CommonDuration


class TestLine(unittest.TestCase):
    def test_line(self):
        objects = [
            Note(
                Pitch(
                    BasePitch.C,
                    Accidental.NATURAL,
                    Octave.TWO_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.G,
                    Accidental.NATURAL,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.E,
                    Accidental.NATURAL,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.C,
                    Accidental.NATURAL,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.B,
                    Accidental.NATURAL,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.B,
                    Accidental.FLAT,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.A,
                    Accidental.NATURAL,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                Pitch(
                    BasePitch.A,
                    Accidental.FLAT,
                    Octave.ONE_LINED,
                ),
                Duration(CommonDuration.EIGTH),
            ),
        ]
        line = Line(objects)
        self.assertEqual(
            "c''8 g'8 e'8 c'8 b'8 bes'8 a'8 aes'8", line.to_lily()
        )


if __name__ == "__main__":
    unittest.main()
