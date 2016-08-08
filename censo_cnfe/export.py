import json

from censo_cnfe import parser


class Dataset:

    def __init__(self, filepath):

        self.filepath = filepath
        self._data = parser.FileParser(self.file)

    @property
    def file(self):
        with open(self.filepath, 'rb') as f:
            return f.readlines()

    @property
    def lines(self):
        return self._data.lines

    def export(self):
        raise NotImplementedError('Subclasses should implement this')

    def export_to_file(self):
        raise NotImplementedError('Subclasses should implement this')


class JSON(Dataset):

    @property
    def _as_dict(self):
        for line in self.lines:
            yield dict(line)

    def export(self):
        yield from json.dumps(list(self._as_dict), indent=4)

    def export_to_file(self, output):

        with open(output, 'w') as f:
            for chunk in self.export():
                f.write(chunk)
