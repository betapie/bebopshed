import random
from .pitch import Key, BasePitch, Accidental


class KeyRng:
    MAJOR_KEYS = [
        Key(BasePitch.C, Accidental.NATURAL),
        Key(BasePitch.F, Accidental.NATURAL),
        Key(BasePitch.G, Accidental.NATURAL),
        Key(BasePitch.B, Accidental.FLAT),
        Key(BasePitch.D, Accidental.NATURAL),
        Key(BasePitch.E, Accidental.FLAT),
        Key(BasePitch.A, Accidental.NATURAL),
        Key(BasePitch.A, Accidental.FLAT),
        Key(BasePitch.E, Accidental.NATURAL),
    ]

    MAJOR_KEY_WEIGHTS = [8, 8, 8, 4, 4, 2, 2, 1, 1]

    MINOR_KEYS = [
        Key(BasePitch.A, Accidental.NATURAL),
        Key(BasePitch.D, Accidental.NATURAL),
        Key(BasePitch.E, Accidental.NATURAL),
        Key(BasePitch.G, Accidental.NATURAL),
        Key(BasePitch.B, Accidental.NATURAL),
        Key(BasePitch.C, Accidental.NATURAL),
        Key(BasePitch.F, Accidental.SHARP),
        Key(BasePitch.F, Accidental.NATURAL),
        Key(BasePitch.C, Accidental.SHARP),
    ]

    MINOR_KEY_WEIGHTS = [8, 8, 6, 4, 3, 4, 2, 1, 1]

    def getMajorKey() -> Key:
        return random.choices(
            KeyRng.MAJOR_KEYS, weights=KeyRng.MAJOR_KEY_WEIGHTS, k=1
        )[0]

    def getMinorKey() -> Key:
        return random.choices(
            KeyRng.MINOR_KEYS, weights=KeyRng.MINOR_KEY_WEIGHTS, k=1
        )[0]
