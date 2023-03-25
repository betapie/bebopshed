# from .line import Line
from .pitch import Pitch, BasePitch, Accidental, Octave
from .music_object import MusicObject


class Transposer:
    BASE_PITCHES = [
        BasePitch.C,
        BasePitch.D,
        BasePitch.E,
        BasePitch.F,
        BasePitch.G,
        BasePitch.A,
        BasePitch.B,
    ]
    NUM_BASE_PITCHES = 7

    def __init__(self, from_pitch: Pitch, to_pitch: Pitch):
        self._delta_base = self.BASE_PITCHES.index(
            to_pitch.base_pitch
        ) - self.BASE_PITCHES.index(from_pitch.base_pitch)
        self._delta_abs = (
            to_pitch.absolute_pitch() - from_pitch.absolute_pitch()
        )

    def transpose(self, object: MusicObject):
        if isinstance(object, Pitch):
            return self._transpose_pitch(object)
        return None

    def _transpose_pitch(self, pitch: Pitch):
        octave = pitch.octave.value
        base_pitch_idx = (
            self.BASE_PITCHES.index(pitch.base_pitch) + self._delta_base
        )
        if base_pitch_idx < 0:
            base_pitch_idx += self.NUM_BASE_PITCHES
            # octave -= 1
        elif base_pitch_idx >= self.NUM_BASE_PITCHES:
            base_pitch_idx -= self.NUM_BASE_PITCHES
            # octave += 1

        base_pitch = self.BASE_PITCHES[base_pitch_idx]
        base_delta = base_pitch.value - (
            pitch.base_pitch.value + pitch.accidental.value
        )
        acc_delta = self._delta_abs - base_delta
        if acc_delta > 0:
            while acc_delta > 2:
                acc_delta -= 12
                octave += 1
        else:
            while acc_delta < -2:
                acc_delta += 12
                octave -= 1

        # TODO: if abs(acc_delta) > 1 -> simplify -> change base_pitch

        return Pitch(base_pitch, Accidental(acc_delta), Octave(octave))
