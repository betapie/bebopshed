from .version import LILY_VERSION


class LilyBuilder:
    def __init__(self):
        self.version = LILY_VERSION
        self._tokens = []

    def set_version(self, version):
        self.version = version
        return self

    def add(self, *tokens):
        self._tokens += tokens
        return self

    def dump(self) -> str:
        retval = f"\\version \"{self.version}\"\n"
        for tok in self._tokens:
            retval += str(tok) + "\n"
        return retval


class LilyCommand:
    def __init__(self, command, content):
        self._command = command
        self._content = content

    def __str__(self) -> str:
        return f"\\{self._command} {self._content}"


class LilyExpression:
    def __init__(self, command, *tokens):
        self._command = command
        self._tokens = list(tokens)

    def __str__(self) -> str:
        retval = ""
        if self._command:
            retval += f"\\{self._command} "
        retval += "{\n"
        for tok in self._tokens:
            retval += f"{str(tok)}\n"
        retval += "}"
        return retval


class LilySimulExpression:
    def __init__(self, *tokens):
        self._tokens = list(tokens)

    def __str__(self) -> str:
        retval = "<<\n"
        for tok in self._tokens:
            retval += f"{str(tok)}\n"
        retval += ">>"
        return retval
