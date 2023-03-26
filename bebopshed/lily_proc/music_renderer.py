import subprocess
import tempfile

from .lily_builder import (
    LilyBuilder, LilyCommand, LilyExpression, LilySimulExpression
)
from .line_parser import LineParser
from .pitch import Key
from .transpose import KeyTransposer


class MusicRenderer:
    def render(self, line: str, chords: str, **kwargs):
        # TODO: handle errors in lily string creation
        lily_string = self.create_lily_string(line, chords, **kwargs)
        tmp_file = tempfile.NamedTemporaryFile(
            "r", dir="tmp", suffix=".cropped.svg")

        proc = subprocess.Popen(
            ["lilypond", "-o", tmp_file.name[:-12],
                "--svg", "-dno-print-pages", "-dcrop", '-'],
            stdin=subprocess.PIPE)
        try:
            proc.communicate(bytes(lily_string, "utf-8"))
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()

        svg_content = tmp_file.read()
        tmp_file.close()
        return svg_content

    def create_lily_string(self, line: str, chords: str, **kwargs):
        builder = LilyBuilder()

        builder.add(
            LilyCommand("include", "\"lily_proc/lily_styles/line.ily\"")
        ).add(
            LilyCommand("include", "\"lily_proc/lily_styles/lilyjazz.ily\"")
        ).add(
            LilyCommand("include", "\"lily_proc/lily_styles/jazzchords.ily\"")
        )

        parser = LineParser()
        line = parser.parse(line)
        if "transpose_from" in kwargs and "transpose_to" in kwargs:
            orig_key = Key.from_lily(kwargs["transpose_from"])
            target_key = Key.from_lily(kwargs["transpose_to"])
            transposer = KeyTransposer(orig_key, target_key)
            line = transposer.transpose(line)
            from_key = kwargs["transpose_from"].lower()
            to_key = kwargs["transpose_to"].lower()
            chords_expr = LilyExpression(
                f"transpose {from_key} {to_key}",
                LilyExpression("chords", chords)
            )
        else:
            chords_expr = LilyExpression("chords", chords)
        line = line.to_lily()
        music_expr = LilySimulExpression(
            chords_expr,
            LilyExpression("new Staff", line)
        )

        builder.add(
            LilyExpression(
                "score",
                music_expr
            )
        )

        return builder.dump()
