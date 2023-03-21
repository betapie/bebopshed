# import re


class LineParser:
    def parse(self, line: str):
        tokens = self.sanitize(line).split()
        # TODO
        return tokens

    def sanitize(self, line_str: str):
        result = ""
        prev = "\n"
        is_command = False
        for c in line_str:
            next = ''
            if is_command:
                if c == ' ':
                    is_command = False
                next = c
            else:
                if c == ' ' and prev != ' ':
                    next = ' '
                elif c == '\\':
                    is_command = True
                    if prev != ' ' and prev != '\n':
                        result += ' '
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
                    if prev != ' ' and prev != '\n':
                        result += ' '
                    next = c
                    if c == '|':
                        result += '|'
                        next = '\n'
                else:
                    next = c
            result += next
            prev = next

        return result
