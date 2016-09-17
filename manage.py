#!/usr/bin/env python

import json
import os
import zipfile

import click

from censo_cnfe import db as db_handlers
from censo_cnfe import export as _export
from censo_cnfe import utils


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

    for file_name, _file in utils.get_all_text_files(cnfe_file):

        click.echo('\n Parsing file: {!r}'.format(file_name))

        data = _export.JSON(_file)

        if output_is_dir:
            data.export_to_file(os.path.join(output, file_name))
        else:
            data.export_to_file(output, file_name)

        click.echo('Created file: {!r}.json'.format(file_name))

    click.echo('\n Ok, Done!\n')


@export.command(name='export-to-couchdb')
@click.argument('cnfe_file_dir', type=click.Path(exists=True, dir_okay=True))
@click.argument('settings', type=click.Path(exists=True))
def export_to_couchdb(cnfe_file_dir, settings):

    with open(settings) as _settings:
        settings = json.loads(_settings.read())

    couchdb = db_handlers.CouchDB(settings)

    for file_name, _file in utils.get_all_text_files(cnfe_file_dir):

        click.echo('\n Parsing file: {!r}'.format(file_name))

        data = _export.DB(_file)

        data.export(couchdb)

        click.echo('Saved {!r} into couchdb'.format(file_name))


@export.command(name='export-to-mongodb')
@click.argument('cnfe_file_dir', type=click.Path(exists=True, dir_okay=True))
@click.argument('settings', type=click.Path(exists=True))
def export_to_mongodb(cnfe_file_dir, settings):

    with open(settings) as _settings:
        settings = json.loads(_settings.read())

    collection = list(filter(None, cnfe_file_dir.split('/')))[-1]

    mongodb = db_handlers.MongoDB(settings, collection=collection)

    for file_name, _file in utils.get_all_text_files(cnfe_file_dir):

        click.echo('\n Parsing file: {!r}'.format(file_name))

        data = _export.DB(_file)

        data.export(mongodb)

        click.echo('Saved {!r} into mongodb'.format(file_name))


if __name__ == '__main__':
    export()
