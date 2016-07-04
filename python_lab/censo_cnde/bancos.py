# -*- coding: utf-8 -*-

from pymongo import MongoClient

from . import configuracao


bancos_disponiveis = dict()


def registrar_banco(classe_banco):

    bancos_disponiveis[classe_banco.__name__.lower()] = classe_banco

    return classe_banco


class Banco(object):

    def __init__(self):

        self._configuracao = None

        self._client = None

        self._configurar()

    def _configurar(self):
        raise NotImplementedError('Subclasses devem immplementar esse método')

    def inserir(self, item, referencia):
        raise NotImplementedError('Subclasses devem implementar esse método')

    def inserir_varios(self, items, referencia):
        raise NotImplementedError('Subclasses devem implementar esse método')


@registrar_banco
class MongoDB(Banco):

    def _configurar(self):

        self._configuracao = configuracao.obter_configuracao_mongodb()

        self._client = MongoClient(self._configuracao['uri'])

        self._db = self._client['censo2010']

    def inserir_varios(self, items, collection):
        self._db[collection].insert(doc_or_docs=items)
