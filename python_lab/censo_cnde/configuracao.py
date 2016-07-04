# -*- coding: utf-8 -*-

import json

CONF_MONGODB = 'censo_cnde/configuracao/mongodb.json'

LAYOUT_JSON = 'censo_cnde/layouts/layout.json'

DIR_DADOS = './dados/cnde/'


def obter_configuracao_mongodb():
    with open(CONF_MONGODB) as _mongodb:
        return json.load(_mongodb)
