#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import json
from concurrent import futures


def gerar_representacao_json():
    with open('./layouts/layout.json') as arquivo:
        return json.load(io.StringIO(''.join(arquivo.readlines())))


class Linha(object):

    def __init__(self, linha):

        self._linha = linha  # linha não tratada
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
                # Nesse caso o layout tem sub chaves

                for sub_chave, sub_item in item.items():

                    if not dados.get(chave):
                        dados[chave] = {}

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


def processar_arquivo(arquivo, max_workers=20):

    with futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

        with open(arquivo, 'rb') as _arquivo:

            linhas_do_arquivo = [
                executor.submit(obter_dados, arquivo_linha)
                for arquivo_linha in _arquivo.readlines()
            ]

            for linha_processada in futures.as_completed(linhas_do_arquivo):
                yield linha_processada.result()
