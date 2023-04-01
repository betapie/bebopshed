from .line import Line
from .chord import Chords
from .pitch import Key
from .transpose import KeyTransposer


class LineProcessor():
    def process(line: Line, chords: Chords, **kwargs) -> tuple:
        processor = LineProcessor._create_processor(**kwargs)
        if processor:
            return processor.process(line, chords)
        return line, chords

    def _create_processor(**kwargs):
        if "transpose_from" in kwargs and "transpose_to" in kwargs:
            return LineProcessor._create_transposer(**kwargs)

    def _create_transposer(**kwargs):
        orig_key = Key.from_lily(kwargs["transpose_from"])
        target_key = Key.from_lily(kwargs["transpose_to"])
        return LineTransposer(orig_key, target_key)


class LineTransposer():
    def __init__(self, orig_key: Key, target_key: Key):
        self.orig_key = orig_key
        self.target_key = target_key

    def process(self, line: Line, chords: Chords) -> tuple:
        transposer = KeyTransposer(self.orig_key, self.target_key)
        line = transposer.transpose(line)
        chords = transposer.transpose(chords)
        return line, chords
