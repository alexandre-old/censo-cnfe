#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os

import click

from censo_cnde import parser
from censo_cnde.bancos import MongoDB
from censo_cnde.configuracao import DIR_DADOS
from censo_cnde.utils import horario


@click.group()
def cli():
    pass


@cli.command(name='importar-dados')
@click.argument('estado')
def importar_dados(estado):

    arquivos_txt = glob.glob(os.path.join(DIR_DADOS, estado, '*.TXT'))

    if not arquivos_txt:
        raise ValueError('Estado inválido')

    click.echo(
        '[{}] Total de arquivos para processar: {}'.format(horario(), len(arquivos_txt))
    )

    mongodb = MongoDB()

    for arquivo_txt in arquivos_txt:

        linhas = parser.processar_arquivo(arquivo_txt)

        click.echo('[{}] {} linhas processadas'.format(horario(), len(linhas)))

        mongodb.inserir_varios(linhas, estado)

        click.echo(
            '[{}] linhas inseridas na collection {}'.format(horario(), estado)
        )



@cli.command(name='exportar-dados')
@click.argument('arquivo_path', type=click.Path(exists=True))
@click.argument('salvar_em', type=click.Path(exists=True))
def exportar_dados(arquivo, salvar_em):
    pass


if __name__ == '__main__':
    cli()
