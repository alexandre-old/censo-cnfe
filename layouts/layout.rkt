#lang racket

;; Representa uma linha no arquivo .txt de acordo com o layout especificado pelo IBGE

;; uma coluna representa um item na linha. Cada coluna tem uma posição inicial
;; e um tamanho. Algumas colunas tem  valores especificos que são definidos
;; no item categoria.
(define-struct coluna (posicao-inicial tamanho [categoria #:auto])
  #:auto-value '()