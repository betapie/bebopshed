
#(set! paper-alist
  (cons '("line_paper_size" . (cons (* 800 pt) (* 100 pt))) paper-alist))

\paper {
  #(set-paper-size "line_paper_size")
}

\header {
    tagline = "Created by Bebopshed"
}