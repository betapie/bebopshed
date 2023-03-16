import subprocess
import tempfile

from .lily_builder import (
    LilyBuilder, LilyCommand, LilyExpression, LilySimulExpression
)


class MusicRenderer:
    def render(self, line: str, chords: str, **kwargs):
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

        builder.add(LilyCommand(
            "include", "\"lily_proc/lily_styles/line.ily\""))
        builder.add(LilyCommand(
            "include", "\"lily_proc/lily_styles/lilyjazz.ily\""))
        builder.add(LilyCommand(
            "include", "\"lily_proc/lily_styles/jazzchords.ily\""))

        music_expr = LilySimulExpression(
            LilyExpression("chords", chords),
            LilyExpression(
                "new Staff", line
            )
        )

        if "transpose_from" in kwargs and "transpose_to" in kwargs:
            from_key = kwargs["transpose_from"].lower()
            to_key = kwargs["transpose_to"].lower()
            music_expr = LilyExpression(
                f"transpose {from_key} {to_key}",
                music_expr
            )

        builder.add(
            LilyExpression(
                "score",
                music_expr
            )
        )

        return builder.dump()
