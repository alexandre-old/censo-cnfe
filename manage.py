#!/usr/bin/env python

import io
import os
import zipfile

import click

from censo_cnfe import export as _export


def get_all_text_files(dir_zip_or_text_file):

    # TODO: Refactoring...Make it work -> make it right -> make it fast

    if os.path.isdir(dir_zip_or_text_file):

        _dir = dir_zip_or_text_file  # just a shorter name

        for item in os.listdir(_dir):

            if not item.lower().endswith('.zip'):
                continue

            zfile = zipfile.ZipFile(os.path.join(_dir, item))

            for textfile in zfile.namelist():
                yield textfile.split('.')[0], io.BytesIO(zfile.read(textfile))

    elif zipfile.is_zipfile(dir_zip_or_text_file):

        zfile = zipfile.ZipFile(dir_zip_or_text_file)

        for textfile in zfile.namelist():
            yield textfile.split('.')[0], io.BytesIO(zfile.read(textfile))

    else:

        file_name = dir_zip_or_text_file  # yet another shorther name

        with open(dir_zip_or_text_file, 'rb') as f:
            textfile = io.BytesIO(f.read())

        yield file_name, textfile


@click.group()
def export():
    pass


@export.command(name='export-to-json')
@click.argument('cnfe_file', type=click.Path(exists=True, dir_okay=True))
@click.argument('output', type=click.Path())
def export_to_json(cnfe_file, output):

    # If the argument 'cnfe_file' is a dir or a zip file, the output must be a
    # dir. It's easier reuse the .TXT file name for the .json created.

    if os.path.isdir(cnfe_file) or zipfile.is_zipfile(cnfe_file):
        if not os.path.isdir(output):
            raise click.exceptions.UsageError(
                'The output must be a directory because more than one file '
                'will be created'
            )
        output_is_dir = True
    else:
        output_is_dir = False

    for file_name, _file in get_all_text_files(cnfe_file):

        click.echo('\n Parsing file: {!r}'.format(file_name))

        data = _export.JSON(_file)

        if output_is_dir:
            data.export_to_file(os.path.join(output, file_name))
        else:
            data.export_to_file(output, file_name)

        click.echo('Created file: {!r}.json'.format(file_name))

    click.echo('\n Ok, Done!\n')


if __name__ == '__main__':
    export()
