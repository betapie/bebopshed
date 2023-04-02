import subprocess
import tempfile
import decouple

from .lily_builder import (
    LilyBuilder,
    LilyExpression,
    LilySimulExpression,
)
from .line_parser import LineParser
from .chord import Chords
from .line_processing import LineProcessor


class MusicRenderer:
    def render(self, line: str, chords: str, **kwargs):
        # TODO: handle errors in lily string creation
        lily_string = self.create_lily_string(line, chords, **kwargs)
        tmp_file = tempfile.NamedTemporaryFile(
            "r",
            dir="/tmp",
            suffix=".cropped.svg",
        )

        proc = subprocess.Popen(
            [
                "lilypond",
                "-o",
                tmp_file.name[:-12],
                "--svg",
                "-dno-print-pages",
                "-dcrop",
                "-",
            ],
            stdin=subprocess.PIPE,
        )
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

        styles_path = f"{decouple.config('SITE_PATH')}/lily_proc/lily_styles"
        builder.add_include(f"{styles_path}/line.ily").add_include(
            f"{styles_path}/lilyjazz.ily"
        ).add_include(f"{styles_path}/jazzchords.ily")

        parser = LineParser()
        line = parser.parse(line)
        print(chords)
        chords = Chords.from_lily(chords)
        line, chords = LineProcessor.process(line, chords, **kwargs)

        music_expr = LilySimulExpression(
            LilyExpression("chords", chords.to_lily()),
            LilyExpression("new Staff", line.to_lily()),
        )

        builder.add(LilyExpression("score", music_expr))

        return builder.dump()
