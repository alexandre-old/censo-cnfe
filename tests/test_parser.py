import os

from censo_cnfe import parser


def test_default_layout_path():
    """Garatir que o arquivo existe no projeto

    """

    assert os.path.exists(parser.DEFAULT_LAYOUT_PATH)


def test_get_layout_json():
    """Teste simples apenas para garantir alguns detalhes do conteudo
    do layouts/layout.json

    """

    layout_json = parser.get_layout_json()

    assert isinstance(layout_json, dict)

    assert layout_json != {}

    expected_item_keys = ['categorias', 'posicao_inicial', 'tamanho']
    for key, value in layout_json.items():

        if key == 'complemento':

            # 6 chaves "value_n" e 6 chaves "elemento_n"
            assert len(value.keys()) == 12

            # Todos os subitems são dicionários
            assert all(isinstance(item, dict) for item in value.values())

            # Todos os subitens contém as chaves esperadas e apenas elas.
            assert all(
                sorted(item.keys()) == expected_item_keys
                for item in value.values()
            )

            assert all(len(item.keys()) == 3 for item in value.values())

        else:

            # Os itens "simples" contém as chaves esperadas e apenas elas.
            assert sorted(value.keys()) == expected_item_keys
            assert len(value.keys()) == 3


def test_layout_without_depth():
    """Testar Layout() com um layout alternativo sem profundidade

    """

    layout_json = {
        'cep': {
            'posicao_inicial': 1,
            'tamanho': 8,
            'categorias': {}
        }
    }

    layout = parser.Layout(layout=layout_json)

    assert layout._keys == ['cep']

    assert layout._layout == layout_json


def test_layout_with_depth():
    """Testar Layout() com dois níveis de profundidade. (versão do layout.json)

    """

    layout_json = {
        'cep': {
            'posicao_inicial': 1,
            'tamanho': 8,
            'categorias': {}
        },
        'complemento': {
            'elemento_1': {
                'posicao_inicial': 9,
                'tamanho': 2,
                'categorias': {}
            },
            'valor_1': {
                'posicao_inicial': 11,
                'tamanho': 2,
                'categorias': {}
            },
        },
    }

    layout = parser.Layout(layout=layout_json)

    expected_keys = ['cep', 'complemento__elemento_1', 'complemento__valor_1']

    assert sorted(layout._keys) == expected_keys

    assert isinstance(layout._layout['complemento'], parser.Layout)


def test_layout_getitem_with_depth():
    """Testar o método __getitem__ quando o layout.json tem profundidade.

    """

    layout_json = {
        'cep': {
            'posicao_inicial': 1,
            'tamanho': 8,
            'categorias': {}
        },
        'complemento': {
            'elemento_1': {
                'posicao_inicial': 9,
                'tamanho': 2,
                'categorias': {}
            },
            'valor_1': {
                'posicao_inicial': 11,
                'tamanho': 2,
                'categorias': {}
            },
        },
    }

    layout = parser.Layout(layout=layout_json)

    assert layout['cep'] == slice(0, 7)

    assert isinstance(layout._layout['complemento'], parser.Layout)

    assert layout._layout['complemento']['elemento_1'] == slice(8, 9)

    assert layout._layout['complemento']['valor_1'] == slice(10, 11)
