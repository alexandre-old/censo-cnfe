import os

from censo_cnfe import parser


def test_defaukt_layout_path():

    expected_path = os.path.join(os.path.abspath('.'), 'layout/laytout.json')

    assert parser.DEFAULT_LAYOUT_PATH == expected_path
