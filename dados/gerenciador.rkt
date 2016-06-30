#!/usr/bin/env racket
#lang racket

(require racket/cmdline)

(define diretorio (make-parameter #f))
(define arquvos (make-parameter null))
(define layout (make-parameter "./layouts/layout.json"))

(define importar-dados
  (command-line
   #:program "importar-dados"
   #:once-each
   [("-l" "--layout") _layout
                      "Caminho para o arquivo de layout"
                      (layout _layout)]
   [("-d" "--diretorio") "Informa que o caminho especificado é um diretorio com .zips"
                         (diretorio #t)]

   #:args arquivos
    arquivos))

(define (main)
  (let ((arquivos importar-dados))
    (if (eq? '() arquivos)
        (raise-argument-error 'importar-dados "Caminho para arquivos .zip" arquivos)
        null)
    (for ([arquivo arquivos])
      (println arquivo))))

(main)
  