from pitch import Pitch, Accidental, Octave
from duration import Duration


class Note:
    def __init__(
        self,
        pitch: Pitch,
        accidental: Accidental,
        octave: Octave,
        duration: Duration,
    ):
        self.pitch = pitch
        self.accidental = accidental
        self.octave = octave
        self.duration = duration

    def __str__(self):
        pass
