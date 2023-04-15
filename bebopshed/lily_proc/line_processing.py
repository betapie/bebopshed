from .line import Line
from .chord import Chords
from .pitch import Key, BasePitch, Accidental
from .transpose import KeyTransposer


class LineProcessor:
    def process(line: Line, chords: Chords, **kwargs) -> tuple:
        processor = LineProcessor._create_processor(**kwargs)
        if processor:
            return processor.process(line, chords)
        return line, chords

    def _create_processor(**kwargs):
        if "transpose" in kwargs:
            return LineProcessor._create_transposer_processor(
                **kwargs["transpose"]
            )
        if "chops_builder" in kwargs:
            return LineProcessor._create_chops_builder_processor(
                **kwargs["chops_builder"]
            )
        return None

    def _create_transposer_processor(**kwargs):
        orig_key = Key.from_lily(kwargs["orig_key"])
        target_key = Key.from_lily(kwargs["target_key"])
        return LineTransposeProcessor(orig_key, target_key)

    def _create_chops_builder_processor(**kwargs):
        orig_key = Key.from_lily(kwargs["orig_key"])
        start_key = Key.from_lily(kwargs["start_key"])
        delta = int(kwargs["delta"])
        return ChopsBuilderProcessor(orig_key, start_key, delta)


class LineTransposeProcessor:
    def __init__(self, orig_key: Key, target_key: Key):
        self.orig_key = orig_key
        self.target_key = target_key

    def process(self, line: Line, chords: Chords) -> tuple:
        transposer = KeyTransposer(self.orig_key, self.target_key)
        line = transposer.transpose(line)
        chords = transposer.transpose(chords)
        return line, chords


class ChopsBuilderProcessor:
    PREFERRED_KEYS = {
        0: Key(BasePitch.C, Accidental.NATURAL),
        1: Key(BasePitch.D, Accidental.FLAT),
        2: Key(BasePitch.D, Accidental.NATURAL),
        3: Key(BasePitch.E, Accidental.FLAT),
        4: Key(BasePitch.E, Accidental.NATURAL),
        5: Key(BasePitch.F, Accidental.NATURAL),
        6: Key(BasePitch.F, Accidental.SHARP),
        7: Key(BasePitch.G, Accidental.NATURAL),
        8: Key(BasePitch.A, Accidental.FLAT),
        9: Key(BasePitch.A, Accidental.NATURAL),
        10: Key(BasePitch.B, Accidental.FLAT),
        11: Key(BasePitch.B, Accidental.NATURAL),
    }

    def __init__(self, orig_key: Key, start_key: Key, delta: int):
        self.orig_key = orig_key
        self.start_key = start_key
        self.delta = delta

    def process(self, line: Line, chords: Chords) -> tuple:
        line.pad()
        chords.pad()
        result_line = Line([])
        result_chords = Chords([])
        start_val = (
            self.start_key.base_pitch.value + self.start_key.accidental.value
        )
        if start_val < 0:
            start_val += 12
        elif start_val >= 12:
            start_val -= 12

        cur_val = start_val
        while True:
            cur_key = self.PREFERRED_KEYS[cur_val]
            transposer = KeyTransposer(self.orig_key, cur_key)
            transposed_line = transposer.transpose(line)
            transposed_chords = transposer.transpose(chords)
            result_line._bars.extend(transposed_line._bars)
            result_chords._bars.extend(transposed_chords._bars)
            cur_val += self.delta
            if cur_val < 0:
                cur_val += 12
            elif cur_val >= 12:
                cur_val -= 12
            if cur_val == start_val:
                break

        return result_line, result_chords
