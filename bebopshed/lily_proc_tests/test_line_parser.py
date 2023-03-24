import unittest
from lily_proc.line_parser import LineParser


class TestNote(unittest.TestCase):
    def test_parse(self):
        parser = LineParser()
        lily_str = "d'8b8\\tuplet 3/2{c'8 e'8 g'8}b'4d''8e'8~|"
        line = parser.parse(lily_str)
        self.assertEqual(line.to_lily(), parser.sanitize(lily_str))

    def test_sanitize(self):
        cases = [
            (
                "b'8 a'8 as'8 b8 d'8 f'8 e'8 e'16 es'16 |",
                "b'8 a'8 aes'8 b8 d'8 f'8 e'8 e'16 ees'16 |",
            ),
            (
                "es'8a'8as'8b8d'8f'8e'8e'16es'16|",
                "ees'8 a'8 aes'8 b8 d'8 f'8 e'8 e'16 ees'16 |",
            ),
            (
                "d'8 b8 \\tuplet 3/2 {c'8 e'8 g'8} b'4 d''8 e'8 ~ |",
                "d'8 b8 \\tuplet 3/2 { c'8 e'8 g'8 } b'4 d''8 e'8 ~ |",
            ),
            (
                "d'8b8\\tuplet 3/2{c'8 e'8 g'8}b'4d''8e'8~|",
                "d'8 b8 \\tuplet 3/2 { c'8 e'8 g'8 } b'4 d''8 e'8 ~ |",
            ),
            (
                "a4a4a4a4|\n\na4a4a4a4~|a1",
                "a4 a4 a4 a4 |\na4 a4 a4 a4 ~ |\na1",
            ),
            (
                "a4a4a8r4.|\n\na4a4r2~|a1",
                "a4 a4 a8 r4. |\na4 a4 r2 ~ |\na1",
            ),
        ]
        parser = LineParser()
        for raw, expected in cases:
            self.assertEqual(parser.sanitize(raw), expected)


if __name__ == "__main__":
    unittest.main()
