#!/usr/bin/env racket
#lang racket

(require racket/cmdline)

(struct parametros (arquivos diretorio layout)
        #:guard (lambda (arquivos diretorio layout struct-name)
                  (unless (not (eq? '() arquivos))
                    (error "Nenhum arquivo especificado"))
                  (values arquivos diretorio layout)))


;; Parametros da CLI
(define diretorio (make-parameter #f))
(define arquvos (make-parameter '()))
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
    (parametros arquivos (layout) (diretorio))))

(define (main)
  (let ((dados importar-dados))
    (println (parametros-arquivos dados))
    (println (parametros-diretorio dados))
    (println (parametros-layout dados))))

(main)