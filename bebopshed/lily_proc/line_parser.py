import re
from fractions import Fraction

from .bar import Bar
from .duration import CommonDuration, Duration
from .lily_error import LilyParseError
from .line import Line
from .music_object import BarLine, Rest, Tie
from .note import Note
from .tuplet import Tuplet


class LineParser:
    def parse(self, line: str):
        sanitized = self.sanitize(line)
        bar_strings = sanitized.split("|")
        last_base_duration = CommonDuration.QUARTER
        bars = []
        for bar_str in bar_strings:
            tokens = bar_str.split()
            objects, _ = self._parse_tokens(tokens, 0, last_base_duration)
            if objects:
                bar = Bar(objects)
                if not bar.duration_check():
                    raise LilyParseError(
                        ("LineParser: duration check for bar:" f" '{bar_str}' failed")
                    )
                bars.append(bar)

        return Line(bars)

    def _parse_tokens(self, tokens, idx, last_common_duration):
        objects = []

        while idx < len(tokens):
            token = tokens[idx]
            if not token:
                idx += 1
                continue
            if token == "}":
                break
            elif token == "\\tuplet":
                rational = Fraction(tokens[idx + 1])
                if tokens[idx + 2] != "{":
                    raise LilyParseError(
                        (
                            "LineParser error: contents of tuplet have to"
                            "be in a {} block"
                        )
                    )
                tuplet_objects, idx = self._parse_tokens(
                    tokens, idx + 3, last_common_duration
                )
                objects.append(Tuplet(rational, tuplet_objects))
            elif token == "~":
                objects.append(Tie())
            elif token == "|":
                objects.append(BarLine())
            elif token.startswith("r"):
                rest = Rest.from_lily(token)
                if not rest.duration:
                    rest = Rest(Duration(last_common_duration))
                last_common_duration = rest.duration.base_duration
                objects.append(rest)
            else:
                note = Note.from_lily(token)
                if not note.duration:
                    note.duration = Duration(last_common_duration)
                last_common_duration = note.duration.base_duration
                objects.append(note)
            idx += 1
        return objects, idx

    def sanitize(self, line_str: str) -> str:
        result = ""
        line_str = line_str.replace("\r", "")
        prev = "\n"
        is_command = False
        for c in line_str:
            next = ""
            if is_command:
                if c == " ":
                    is_command = False
                next = c
            else:
                if c == " " and prev != " ":
                    continue
                elif c == "\n" and prev == "\n":
                    continue
                elif c == "\\":
                    is_command = True
                    if prev != " " and prev != "\n":
                        result += " "
                    next = c
                elif c == "e" and prev in ["c", "d", "e", "f", "g", "a", "b"]:
                    next = c
                elif c in [
                    "~",
                    "{",
                    "}",
                    "|",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "a",
                    "b",
                    "r",
                ]:
                    if prev != " " and prev != "\n":
                        result += " "
                    next = c
                    if c == "|":
                        result += "|"
                        next = "\n"
                else:
                    next = c
            result += next
            prev = next

        regex = r"(\b[ea])(s)"
        result = re.sub(regex, r"\1es", result)
        result = result.strip()
        if result[-1] != "|":
            result += " |"
        return result
