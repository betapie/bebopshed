import subprocess
import tempfile


class MusicRenderer:
    LILYPOND_VERSION = "2.22.1"

    def render(self, line_ly: str, chords_ly: str):
        lily_string = self.create_ly_string(line_ly, chords_ly)
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

    def create_ly_string(self, line_ly: str, chords_ly: str):
        ly_string = ""
        ly_string += f"\\version \"{self.LILYPOND_VERSION}\" \n\n"

        # TODO includes, styles
        ly_string += "\\include \"music_renderer/lily_styles/line.ily\""
        ly_string += "\\include \"music_renderer/lily_styles/lilyjazz.ily\""
        ly_string += "\\include \"music_renderer/lily_styles/jazzchords.ily\""

        ly_string += "\\score {\n"
        ly_string += "<<\n"

        ly_string += "\\chords {\n"
        ly_string += chords_ly + '\n'
        ly_string += "}\n"

        ly_string += "\\new Staff \\relative c {\n"
        ly_string += line_ly + '\n'
        ly_string += "}\n"

        ly_string += ">>\n"
        ly_string += "}\n"

        return ly_string
