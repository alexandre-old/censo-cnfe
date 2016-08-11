import json

from censo_cnfe import parser


class Dataset:

    def __init__(self, stream):

        self._stream = stream

        self._data = parser.FileParser(self.content)

    @property
    def content(self):
        return self._stream.readlines()

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

        if not output.lower().endswith('.json'):

            output = '{}.json'.format(output)

        with open(output, 'w') as f:
            for chunk in self.export():
                f.write(chunk)
