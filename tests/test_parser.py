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
