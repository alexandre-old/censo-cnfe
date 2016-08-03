import os


DEFAULT_LAYOUT_PATH = os.path.join(os.path.abspath('.'), 'layout/laytout.json')


class Layout(object):

    '''TODO: Docstring for Layout. '''

    def __init__(self, layout_path=None):

        '''TODO: docstring '''

        self._layout_path = layout_path or DEFAULT_LAYOUT_PATH
