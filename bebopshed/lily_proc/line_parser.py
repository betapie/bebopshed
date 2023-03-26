from fractions import Fraction
import re
from .music_object import BarLine, Tie, Rest
from .note import Note
from .line import Line
from .tuplet import Tuplet
from .duration import CommonDuration, Duration


class LineParser:
    def parse(self, line: str):
        tokens = self.sanitize(line).split()
        last_base_duration = CommonDuration.QUARTER
        objects, _ = self._parse_tokens(tokens, 0, last_base_duration)
        return Line(objects)

    def _parse_tokens(self, tokens, idx, last_common_duration):
        objects = []

        while idx < len(tokens):
            token = tokens[idx]
            if token == "}":
                break
            elif token == "\\tuplet":
                rational = Fraction(tokens[idx + 1])
                # TODO assert tokens[idx + 2] == '{'
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
