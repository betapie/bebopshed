\version "2.22.1"
\include "../stylesheet/lilyjazz.ily"
\include "../stylesheet/jazzchords.ily"

\score {
    <<
    \chords {
        r4 es2:m7 as:7 des:7+
    }
    \new Staff \relative c {
        \partial 4 es'8 e | 
        f8 ges g as a bes b d |
        f4 es8 des8 (des4)
    }
    >>
}
