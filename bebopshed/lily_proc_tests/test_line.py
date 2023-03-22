import sys
import os
import unittest

# TODO: Maybe use setuptools instead?
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lily_proc.line import Line  # noqa: E402
from lily_proc.note import Note  # noqa: E402
from lily_proc.pitch import BasePitch, Accidental, Octave  # noqa: E402
from lily_proc.duration import Duration, CommonDuration  # noqa: E402


class TestLine(unittest.TestCase):
    def test_line(self):
        objects = [
            Note(
                BasePitch.C,
                Accidental.NATURAL,
                Octave.TWO_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.G,
                Accidental.NATURAL,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.E,
                Accidental.NATURAL,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.C,
                Accidental.NATURAL,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.B,
                Accidental.NATURAL,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.B,
                Accidental.FLAT,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.A,
                Accidental.NATURAL,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
            Note(
                BasePitch.A,
                Accidental.FLAT,
                Octave.ONE_LINED,
                Duration(CommonDuration.EIGTH),
            ),
        ]
        line = Line(objects)
        self.assertEqual(
            "c''8 g'8 e'8 c'8 b'8 bes'8 a'8 aes'8", line.to_lily()
        )


if __name__ == "__main__":
    unittest.main()
