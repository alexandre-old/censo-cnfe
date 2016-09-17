import io
import os
import zipfile


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
