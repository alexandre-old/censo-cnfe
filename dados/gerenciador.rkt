#!/usr/bin/env racket
#lang racket

(require racket/cmdline)

(define diretorio (make-parameter #f))
(define arquvo-zip (make-parameter null))
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
   #:args (arquivo-zip)
   arquivo-zip))