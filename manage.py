#!/usr/bin/env python

import click

from censo_cnfe import export as _export


@click.group()
def export():
    pass


@export.command(name='export-to-json')
@click.argument('cnfe_file', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def export_to_json(cnfe_file, output):

    data = _export.JSON(cnfe_file)

    data.export_to_file(output)

    print('Arquivo {!r} criado com sucesso!'.format(output))


if __name__ == '__main__':
    export()
