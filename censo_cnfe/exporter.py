import json

from censo_cnfe import parser


class Dataset:

    def __init__(self, filepath):

        self.filepath = filepath
        self.data = parser.FileParser(self.file)

    @property
    def file(self):
        with open(self.filepath) as f:
            return f.readlines()

    @property
    def headers(self):
        return self.data._layout._keys

    @property
    def lines(self):
        raise NotImplementedError('Subclasses should implement this')

    def export(self):
        raise NotImplementedError('Subclasses should implement this')


class JSON(Dataset):

    @property
    def lines(self):
        for line in self.data.lines:
            yield dict(line)

    def export(self):
        return json.dumps(list(self.lines))
