import copy
from enum import Enum
from .music_object import MusicObject
from .pitch import Pitch, Key, BasePitch, Accidental, Octave
from .note import Note
from .tuplet import Tuplet
from .line import Line
from .chord import Chord, Chords


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

    def __init__(self, from_pitch: Pitch, to_pitch: Pitch, simplify=True):
        self._delta_base = self.BASE_PITCHES.index(
            to_pitch.base_pitch
        ) - self.BASE_PITCHES.index(from_pitch.base_pitch)
        self._delta_abs = (
            to_pitch.absolute_pitch() - from_pitch.absolute_pitch()
        )
        self._simplify = simplify

    def transpose(self, object: MusicObject):
        if isinstance(object, Pitch):
            return self._transpose_pitch(object)
        if isinstance(object, Key):
            return self._transpose_key(object)
        if isinstance(object, Note):
            return self._transpose_note(object)
        if isinstance(object, Chord):
            return self._transpose_chord(object)
        if isinstance(object, Tuplet):
            return self._transpose_tuplet(object)
        if isinstance(object, Line):
            return self._transpose_line(object)
        if isinstance(object, Chords):
            return self._transpose_chords(object)
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
            while acc_delta > 6:
                acc_delta -= 12
                octave += 1
        else:
            while acc_delta < -6:
                acc_delta += 12
                octave -= 1

        if self._simplify:
            if acc_delta > 1:
                base_pitch_idx += 1
                if base_pitch_idx >= len(self.BASE_PITCHES):
                    base_pitch_idx = 0
                    octave += 1
                base_pitch = self.BASE_PITCHES[base_pitch_idx]
            elif acc_delta < -1:
                base_pitch_idx -= 1
                if base_pitch_idx < 0:
                    base_pitch_idx = len(self.BASE_PITCHES) - 1
                    octave -= 1
                base_pitch = self.BASE_PITCHES[base_pitch_idx]
            acc_delta = self._delta_abs - (
                Pitch(
                    base_pitch, Accidental.NATURAL, Octave(octave)
                ).absolute_pitch()
                - pitch.absolute_pitch()
            )

        return Pitch(base_pitch, Accidental(acc_delta), Octave(octave))

    def _transpose_key(self, key: Key) -> Key:
        pitch = Pitch(key.base_pitch, key.accidental, Octave.ONE_LINED)
        transposed = self._transpose_pitch(pitch)
        return Key(transposed.base_pitch, transposed.accidental)

    def _transpose_note(self, note: Note) -> Note:
        pitch = self._transpose_pitch(note.pitch)
        duration = copy.deepcopy(note.duration)
        return Note(pitch, duration)

    def _transpose_chord(self, chord: Chord) -> Chord:
        key = self._transpose_key(chord.key)
        return Chord(key, chord.duration, chord.quality, chord.decorators)

    def _transpose_tuplet(self, tuplet: Tuplet) -> Tuplet:
        objects = [self.transpose(obj) for obj in tuplet._objects]
        rational = copy.deepcopy(tuplet._rational)
        return Tuplet(rational, objects)

    def _transpose_line(self, line: Line) -> Line:
        objects = [self.transpose(obj) for obj in line._objects]
        return Line(objects)

    def _transpose_chords(self, chords: Chords) -> Chords:
        objects = [self.transpose(obj) for obj in chords._objects]
        return Chords(objects)


class KeyTransposeStrategy(Enum):
    AUTO = 0
    UP = 1
    DOWN = 2


class KeyTransposer:
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

    def __init__(
        self, from_key: Key, to_key: Key, strategy=KeyTransposeStrategy.AUTO
    ):
        self.from_key = from_key
        self.to_key = to_key
        self.strategy = strategy

    def transpose(self, object: MusicObject):
        from_pitch = Pitch(
            self.from_key.base_pitch,
            self.from_key.accidental,
            Octave.ONE_LINED,
        )
        to_pitch = Pitch(
            self.to_key.base_pitch, self.to_key.accidental, Octave.ONE_LINED
        )
        delta = to_pitch.absolute_pitch() - from_pitch.absolute_pitch()
        if self.strategy == KeyTransposeStrategy.UP and delta < 0:
            to_pitch.octave = Octave(to_pitch.octave.value - 1)
        elif self.strategy == KeyTransposeStrategy.DOWN and delta > 0:
            to_pitch.octave = Octave(to_pitch.octave.value + 1)
        else:  # AUTO
            min_pitch, max_pitch = self._min_max_pitch(object)
            if min_pitch and max_pitch:
                mean_abs_pitch = (
                    max_pitch.absolute_pitch() + min_pitch.absolute_pitch()
                ) / 2
                pivot = Pitch(
                    BasePitch.B, Accidental.FLAT, Octave.ONE_LINED
                ).absolute_pitch()
                if delta < 0:
                    if pivot - (mean_abs_pitch + delta) > 6:
                        to_pitch.octave = Octave(to_pitch.octave.value + 1)
                elif delta > 0:
                    if mean_abs_pitch + delta - pivot > 6:
                        to_pitch.octave = Octave(to_pitch.octave.value - 1)

        pitch_transposer = PitchTransposer(from_pitch, to_pitch)
        return pitch_transposer.transpose(object)

    def _min_max_pitch(self, object: MusicObject) -> tuple:
        pitches = self._collect_pitches(object)
        min_pitch, max_pitch = None, None
        for pitch in pitches:
            abs_pitch = pitch.absolute_pitch()
            if not min_pitch or abs_pitch < min_pitch.absolute_pitch():
                min_pitch = pitch
            if not max_pitch or abs_pitch > max_pitch.absolute_pitch():
                max_pitch = pitch
        return min_pitch, max_pitch

    def _collect_pitches(self, object: MusicObject) -> list:
        pitches = []
        if isinstance(object, Note):
            pitches.append(object.pitch)
        elif isinstance(object, Line) or isinstance(object, Tuplet):
            for obj in object._objects:
                pitches.extend(self._collect_pitches(obj))
        return pitches
