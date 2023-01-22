
from music_renderer import MusicRenderer


def main():
    renderer = MusicRenderer()

    chords = "bes1:m7 es:7 as:7+"
    line = """r8 c''8 \\tuplet 3/2 {des8 es8 f8} as8 bes b c |
        des d es b c c16 as es8 des |
        c as f e as4 bes4 |
        es,4 es4"""

    renderer.render(line, chords)


if __name__ == "__main__":
    main()
