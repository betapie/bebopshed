from fractions import Fraction
from .music_token import BarLine, Tie
from .note import Note
from .line import Line
from .tuplet import Tuplet


class LineParser:
    def parse(self, line: str):
        tokens = self.sanitize(line).split()
        objects, _ = self._parse_tokens(tokens, 0)
        return Line(objects)

    def _parse_tokens(self, tokens, idx):
        objects = []

        while idx < len(tokens):
            token = tokens[idx]
            if token == "}":
                break
            elif token == "\\tuplet":
                rational = Fraction(tokens[idx + 1])
                # TODO assert tokens[idx + 2] == '{'
                tuplet_objects, idx = self._parse_tokens(tokens, idx + 3)
                objects.append(Tuplet(rational, tuplet_objects))
            elif token == "~":
                objects.append(Tie())
            elif token == "|":
                objects.append(BarLine())
            else:
                note = Note.from_lily(token)
                if note:
                    objects.append(note)
            idx += 1
        return objects, idx

    def sanitize(self, line_str: str):
        result = ""
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
                    next = " "
                elif c == "\\":
                    is_command = True
                    if prev != " " and prev != "\n":
                        result += " "
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

        return result.strip()
