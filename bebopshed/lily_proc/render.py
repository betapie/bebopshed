
from .lily_builder import (
    LilyBuilder, LilyCommand, LilyExpression, LilySimulExpression
)


def main():
    chords = "bes1:m7 es:7 as:7+"
    line = """r8 c''8 \\tuplet 3/2 {des8 es8 f8} as8 bes b c |
        des d es b c c16 as es8 des |
        c as f e as4 bes4 |
        es,4 es4"""

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

    lily_string2 = builder.dump()
    print(lily_string2)


if __name__ == "__main__":
    main()
