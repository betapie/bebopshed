import sys
import os
import unittest

# # TODO: Maybe use setuptools instead?
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lily_proc.line_parser import LineParser  # noqa: E402

# from lily_proc.pitch import Pitch, Accidental, Octave  # noqa: E402
# from lily_proc.duration import Duration, CommonDuration  # noqa: E402


class TestNote(unittest.TestCase):
    def test_parse(self):
        # parser = LineParser()
        # lily_str = "d'8b8\\tuplet 3/2{c'8 e'8 g'8}b'4d''8e'8~|"
        # sanitized = parser.sanitize(lily_str)
        # parsed = parser.parse(sanitized)
        pass

    def test_sanitize(self):
        cases = [
            (
                "b'8 a'8 as'8 b8 d'8 f'8 e'8 e'16 es'16 |",
                "b'8 a'8 as'8 b8 d'8 f'8 e'8 e'16 es'16 |\n",
            ),
            (
                "b'8a'8as'8b8d'8f'8e'8e'16es'16|",
                "b'8 a'8 as'8 b8 d'8 f'8 e'8 e'16 es'16 |\n",
            ),
            (
                "d'8 b8 \\tuplet 3/2 {c'8 e'8 g'8} b'4 d''8 e'8 ~ |",
                "d'8 b8 \\tuplet 3/2 { c'8 e'8 g'8 } b'4 d''8 e'8 ~ |\n"
            ),
            (
                "d'8b8\\tuplet 3/2{c'8 e'8 g'8}b'4d''8e'8~|",
                "d'8 b8 \\tuplet 3/2 { c'8 e'8 g'8 } b'4 d''8 e'8 ~ |\n"
            )
        ]
        parser = LineParser()
        for raw, expected in cases:
            self.assertEqual(
                parser.sanitize(raw), expected
            )


if __name__ == "__main__":
    unittest.main()
