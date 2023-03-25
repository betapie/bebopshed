import unittest
from lily_proc.transposer import Transposer
from lily_proc.pitch import Pitch, BasePitch, Accidental, Octave


class TestTransposer(unittest.TestCase):
    def test_transpose_pitch_up(self):
        pitch_from = Pitch(BasePitch.C, Accidental.NATURAL, Octave.ONE_LINED)
        pitch_to = Pitch(BasePitch.E, Accidental.FLAT, Octave.ONE_LINED)

        transposer = Transposer(pitch_from, pitch_to)

        cases = [
            (
                Pitch(BasePitch.C, Accidental.NATURAL, Octave.ONE_LINED),
                Pitch(BasePitch.E, Accidental.FLAT, Octave.ONE_LINED),
            ),
            (
                Pitch(BasePitch.B, Accidental.NATURAL, Octave.ONE_LINED),
                Pitch(BasePitch.D, Accidental.NATURAL, Octave.TWO_LINED),
            ),
            (
                Pitch(BasePitch.B, Accidental.FLAT, Octave.ONE_LINED),
                Pitch(BasePitch.D, Accidental.FLAT, Octave.TWO_LINED),
            ),
            (
                Pitch(BasePitch.F, Accidental.SHARP, Octave.ONE_LINED),
                Pitch(BasePitch.A, Accidental.NATURAL, Octave.ONE_LINED),
            ),
            (
                Pitch(BasePitch.D, Accidental.FLAT, Octave.ONE_LINED),
                Pitch(BasePitch.F, Accidental.FLAT, Octave.ONE_LINED),
            )
        ]

        for pitch, transposed in cases:
            self.assertEqual(transposer.transpose(pitch), transposed)

    def test_transpose_pitch_up_oct(self):
        pitch_from = Pitch(BasePitch.F, Accidental.NATURAL, Octave.ONE_LINED)
        pitch_to = Pitch(BasePitch.D, Accidental.FLAT, Octave.TWO_LINED)

        transposer = Transposer(pitch_from, pitch_to)

        cases = [
            (
                Pitch(BasePitch.F, Accidental.NATURAL, Octave.ONE_LINED),
                Pitch(BasePitch.D, Accidental.FLAT, Octave.TWO_LINED),
            ),
            (
                Pitch(BasePitch.A, Accidental.NATURAL, Octave.ONE_LINED),
                Pitch(BasePitch.F, Accidental.NATURAL, Octave.TWO_LINED),
            ),
            (
                Pitch(BasePitch.C, Accidental.NATURAL, Octave.TWO_LINED),
                Pitch(BasePitch.A, Accidental.FLAT, Octave.TWO_LINED),
            ),
            (
                Pitch(BasePitch.E, Accidental.FLAT, Octave.ONE_LINED),
                Pitch(BasePitch.C, Accidental.FLAT, Octave.TWO_LINED),
            ),
            (
                Pitch(BasePitch.G, Accidental.SHARP, Octave.ONE_LINED),
                Pitch(BasePitch.E, Accidental.NATURAL, Octave.TWO_LINED),
            )
        ]

        for pitch, transposed in cases:
            self.assertEqual(transposer.transpose(pitch), transposed)

    def test_transpose_pitch_down(self):
        pitch_from = Pitch(BasePitch.E, Accidental.FLAT, Octave.ONE_LINED)
        pitch_to = Pitch(BasePitch.C, Accidental.NATURAL, Octave.ONE_LINED)

        transposer = Transposer(pitch_from, pitch_to)

        cases = [
            (
                Pitch(BasePitch.E, Accidental.FLAT, Octave.ONE_LINED),
                Pitch(BasePitch.C, Accidental.NATURAL, Octave.ONE_LINED),
            ),
            (
                Pitch(BasePitch.D, Accidental.NATURAL, Octave.TWO_LINED),
                Pitch(BasePitch.B, Accidental.NATURAL, Octave.ONE_LINED),
            ),
            (
                Pitch(BasePitch.D, Accidental.FLAT, Octave.TWO_LINED),
                Pitch(BasePitch.B, Accidental.FLAT, Octave.ONE_LINED),
            ),
            (
                Pitch(BasePitch.A, Accidental.NATURAL, Octave.ONE_LINED),
                Pitch(BasePitch.F, Accidental.SHARP, Octave.ONE_LINED),
            ),
            (
                Pitch(BasePitch.F, Accidental.FLAT, Octave.ONE_LINED),
                Pitch(BasePitch.D, Accidental.FLAT, Octave.ONE_LINED),
            )
        ]

        for pitch, transposed in cases:
            self.assertEqual(transposer.transpose(pitch), transposed)
