import json

from censo_cnfe import parser


class Dataset:

    def __init__(self, filepath):

        self.filepath = filepath
        self._data = parser.FileParser(self.file)

    @property
    def file(self):
        with open(self.filepath) as f:
            return f.readlines()

    @property
    def headers(self):
        return self.data._layout._keys

    @property
    def lines(self):
        yield from self._data.lines

    def export(self):
        raise NotImplementedError('Subclasses should implement this')


class JSON(Dataset):

    def export(self):
        return json.dumps([dict(line) for line in self.lines])
