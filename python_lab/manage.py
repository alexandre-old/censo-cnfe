#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click


class BancosDisponiveis(click.ParamType):

    name = 'bancos_disponiveis'

    def convert(self, value, param, ctx):
        return value


BANCOS_DISPONIVEIS = BancosDisponiveis()


@click.group()
def cli():
    pass


@cli.command(name='importar-dados')
@click.argument('db', type=BANCOS_DISPONIVEIS)
@click.argument('arquivo', type=click.Path(exists=True))
def importar_dados(db, arquivo):
    pass


@cli.command(name='exportar-dados')
@click.argument('arquivo', type=click.Path(exists=True))
@click.argument('salvar_em', type=click.Path(exists=True))
def exportar_dados(arquivo, salvar_em):
    pass


if __name__ == '__main__':
    cli()
