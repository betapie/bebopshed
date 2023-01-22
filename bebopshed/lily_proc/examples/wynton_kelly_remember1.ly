
\version "2.22.1"

\include "../lily_styles/line.ily"
\include "../lily_styles/lilyjazz.ily"
\include "../lily_styles/jazzchords.ily"

\score {
    <<
    \chords {
        bes1:m7 es:7 as:7+
    }
    \new Staff \relative c {
        r8 f'8 \tuplet 3/2 {as8 bes8 b8} c8 des d es |
        des16 es des b c4 g8 bes8 a16 bes a g |
        \partial 2 as8 c,
    }
    >>
}
