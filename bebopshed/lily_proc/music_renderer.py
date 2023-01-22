import subprocess
import tempfile

from .lily_builder import (
    LilyBuilder, LilyCommand, LilyExpression, LilySimulExpression
)


class MusicRenderer:
    def render(self, line: str, chords: str):
        lily_string = self.create_lily_string(line, chords)
        tmp_file = tempfile.NamedTemporaryFile("r", dir="tmp", suffix=".svg")

        proc = subprocess.Popen(
            ["lilypond", "-o", tmp_file.name[:-4], "--svg", '-'],
            stdin=subprocess.PIPE)
        try:
            proc.communicate(bytes(lily_string, "utf-8"))
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()

        svg_content = tmp_file.read()
        tmp_file.close()
        return svg_content

    def create_lily_string(self, line: str, chords: str):
        builder = LilyBuilder()

        builder.add(LilyCommand(
            "include", "\"lily_proc/lily_styles/line.ily\""))
        builder.add(LilyCommand(
            "include", "\"lily_proc/lily_styles/lilyjazz.ily\""))
        builder.add(LilyCommand(
            "include", "\"lily_proc/lily_styles/jazzchords.ily\""))

        builder.add(
            LilyExpression(
                "score",
                LilySimulExpression(
                    LilyExpression("chords", chords),
                    LilyExpression(
                        "new Staff",
                        LilyExpression("relative c", line)
                    )
                )
            )
        )

        return builder.dump()
