#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from concurrent import futures

from censo_cnde.configuracao import LAYOUT_JSON


def gerar_representacao_json():
    with open(LAYOUT_JSON) as arquivo:
        return json.load(arquivo)


class Linha(object):

    def __init__(self, linha):

        self._linha = linha.decode('latin1')
        self._arquivo_layout = None
        self._layout = {}

        self.arquivo_layout = gerar_representacao_json()
        self.gerar_layout(self.arquivo_layout)


    def gerar_layout(self, arquivo_layout, chave_principal=None):

        for chave, item in arquivo_layout.items():

            if not item.get('posicao_inicial'):
                self.gerar_layout(arquivo_layout[chave], chave_principal=chave)
            else:
                inicio = item['posicao_inicial'] - 1
                fim = inicio + item['tamanho']

                estrutura = {
                    'valor': slice(inicio, fim),
                    'categorias': item['categorias']
                }

                if chave_principal:
                    self._layout[chave_principal] = {}
                    self._layout[chave_principal][chave] = estrutura

                else:
                    self._layout[chave] = estrutura


    def as_dict(self):

        dados = {}

        for chave, item in self._layout.items():

            if set(item.keys()) != set(['valor', 'categorias']):

                dados[chave] = {}

                for sub_chave, sub_item in item.items():

                    dados[chave][sub_chave] = {
                        'valor': self._linha[sub_item['valor']],
                        'categorias': sub_item['categorias']
                    }
            else:

                dados[chave] = {
                    'valor': self._linha[item['valor']],
                    'categorias': item['categorias']
                }


        dados['metadados'] = {'linha_original': self._linha}

        return dados


def obter_dados(linha_nao_processada):
    return Linha(linha_nao_processada).as_dict()


def processar_arquivo(arquivo, max_workers=8):

    print('Processando arquivo: {}'.format(arquivo))

    with open(arquivo, 'rb') as _arquivo:
        linhas_do_arquivo = _arquivo.readlines()

    linhas_processadas = []

    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

        linhas_para_processar = [
            executor.submit(obter_dados, l) for l in linhas_do_arquivo
        ]

        for linha in futures.as_completed(linhas_para_processar):
            linhas_processadas.append(linha.result())

    return linhas_processadas
