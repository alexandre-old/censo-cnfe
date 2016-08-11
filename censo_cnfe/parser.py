import json
import os
from concurrent.futures import as_completed, ThreadPoolExecutor


DEFAULT_LAYOUT_PATH = os.path.join(
    os.path.abspath('.'),
    'censo_cnfe/layouts/layout.json'
)


def get_layout_json():

    '''Returns the default layout json content'''

    with open(DEFAULT_LAYOUT_PATH) as f:
        return json.load(f)


class Layout:

    '''Object that represents the layout specified by the IBGE '''

    def __init__(self, layout=None):

        self._layout = {}
        self._keys = []

        self._set_base_layout(layout or get_layout_json())

    def __iter__(self):
        for key in self._keys:
            yield key, self[key]

    def __getitem__(self, key):

        if '__' in key:

            # FIXME: Only two levels of depth is considered
            _base_key, _sub_key = key.split('__')

            return self._layout[_base_key][_sub_key]

        _item = self._layout[key]

        _range = _item['posicao_inicial'] - 1, _item['tamanho'] - 1

        return slice(_range[0], _range[0] + _range[1])

    def _set_base_layout(self, layout):

        for key, value in layout.items():

            if not value.get('tamanho'):

                self._keys += list(
                    '{}__{}'.format(key, sub) for sub in layout[key]
                )

                self._layout[key] = Layout(layout=value)
            else:
                self._layout[key] = value
                self._keys.append(key)


class LineParser:

    def __init__(self, raw_line, layout):

        self._line = raw_line.decode('latin-1').strip()
        self._layout = layout

    @property
    def data(self):
        for key, _slice in self._layout:
            yield key, self._line[_slice]


class FileParser:

    def __init__(self, file):

        self._file = file
        self._layout = Layout()

    @property
    def lines(self):

        with ThreadPoolExecutor(max_workers=20) as executor:

            _lines = [
                executor.submit(self.parse_line, _line) for _line in self._file
            ]

            for line in as_completed(_lines):
                yield line.result()

    def parse_line(self, line):
        return tuple(item for item in LineParser(line, self._layout).data)
