import copy
from .music_object import MusicObject
from .pitch import Pitch, BasePitch, Accidental, Octave
from .note import Note
from .tuplet import Tuplet
from .line import Line


class PitchTransposer:
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
        if isinstance(object, Note):
            return self._transpose_note(object)
        if isinstance(object, Tuplet):
            return self._transpose_tuplet(object)
        if isinstance(object, Line):
            return self._transpose_line(object)
        # object does not need to be transposed
        return copy.deepcopy(object)

    def _transpose_pitch(self, pitch: Pitch) -> Pitch:
        octave = pitch.octave.value
        base_pitch_idx = (
            self.BASE_PITCHES.index(pitch.base_pitch) + self._delta_base
        )
        if base_pitch_idx < 0:
            base_pitch_idx += self.NUM_BASE_PITCHES
        elif base_pitch_idx >= self.NUM_BASE_PITCHES:
            base_pitch_idx -= self.NUM_BASE_PITCHES

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

    def _transpose_note(self, note: Note) -> Note:
        pitch = self._transpose_pitch(note.pitch)
        duration = copy.deepcopy(note.duration)
        return Note(pitch, duration)

    def _transpose_tuplet(self, tuplet: Tuplet) -> Tuplet:
        objects = [self.transpose(obj) for obj in tuplet._objects]
        rational = copy.deepcopy(tuplet._rational)
        return Tuplet(rational, objects)

    def _transpose_line(self, line: Line) -> Line:
        objects = [self.transpose(obj) for obj in line._objects]
        return Line(objects)
