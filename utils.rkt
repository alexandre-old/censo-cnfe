#lang racket

;; Código com pequenas modificações a partir da resposta:
;; https://stackoverflow.com/questions/108169/how-do-i-take-a-slice-of-a-list-a-sublist-in-scheme

(define get-n-items
    (lambda (lst num)
        (if (> num 0)
            (cons (car lst) (get-n-items (cdr lst) (- num 1)))
            '()))) ;'

(define slice
    (lambda (start count [lst '()]) ;; Deixar a lista como parametro opcional para conseguir usar curry.
        (if (> start 1)
            (slice (cdr lst) (- start 1) count)
            (get-n-items lst count))))