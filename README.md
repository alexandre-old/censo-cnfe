CENSO-CNFE PARSER E CLI
=======================

Projeto para parsear os dados do diretório [CNFE](ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/Cadastro_Nacional_de_Enderecos_Fins_Estatisticos/) do [último censo](ftp://ftp.ibge.gov.br/Censos/Censo_Demografico_2010/).

Esse projeto ainda é bem experimental (sim, funciona). Colabore com pull requests e issues =]

## Sobre os dados

Para utilizar esse projeto é necessário baixar os dados diretamente do site/ftp do IBGE.
Se você tiver algum problema para baixar esses dados e/ou quiser apenas a base de dados
processados, eu posso tentar ajudar. (abra uma issue)

## Layouts

Para facilitar o processo, eu criei um arquivo `layout.json` com o mesmo conteúdo do `Layout.xls`
fornecido pelo IBGE.

Durante parsing, a chave `categorias` não é adicionada. Eu não estou muito certo a respeito dessa
decisão, mas eu acredito que essas informação devem ficar separadas por serem algo mais próximo a
um metada dado do que conteúdo dos arquivos processados.

## A CLI (command line interface)

A CLI permite exportar dados para arquivos ou DBs. A versão atual sabe lidar com diretórios,
arquivos .zip e arquivos .TXT (os formatos disponíveis no site/ftp do IBGE).

Para exportar os dados para os DBs disponíveis, você deve utilizar o arquivos `settings.json`
correspondente disponível no diretório `settings/` (e.g. `settings/mongodb.json`).

```bash

(censo-cnfe) o0x41e@incdev ~/Development/python/censo-cnfe (master)
 ~>./manage.py
Usage: manage.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  export-to-couchdb
  export-to-json
  export-to-mongodb
```

### Exportar para arquivo

Por enquanto o único formato disponível é o formado JSON.

#### Exemplos

```bash
(censo-cnfe) o0x41e@incdev ~/Development/python/censo-cnfe (master)
~>./manage.py export-to-json ~/Documents/Cadastro_Nacional_de_Enderecos_Fins_Estatisticos/SP/ ~/Documents/censo-cnfe/SP/
```

### Exportar para uma base de dados MongoDB

#### Exemplos

```bash
(censo-cnfe) o0x41e@incdev ~/Development/python/censo-cnfe (master)
~>./manage.py export-to-mongodb ~/Documents/Cadastro_Nacional_de_Enderecos_Fins_Estatisticos/SP/ settings/mongodb.json
```

### Exportar para uma base de dados CouchDB

#### Exemplos

```bash
(censo-cnfe) o0x41e@incdev ~/Development/python/censo-cnfe (master)
~>./manage.py export-to-couchdb ~/Documents/Cadastro_Nacional_de_Enderecos_Fins_Estatisticos/SP/ settings/couchdb.json
```

## Performance

```
(censo-cnfe) alexandre ~/Development/python/censo-cnfe (master)
 ~>time ./manage.py export-to-json examples/35188000500.zip /tmp/censo-cnfe/

 Parsing file: '35188000500'
Created file: '35188000500'.json

 Ok, Done!


real	2m4.164s
user	2m1.580s
sys	0m4.300s
```

```
alexandre /tmp
 ~>unzip 35188000500.zip
Archive:  35188000500.zip
  inflating: 35188000500.TXT
alexandre /tmp
 ~>wc -l 35188000500.TXT
301638 35188000500.TXT
```

## Licença

Esse projeto utiliza a licença [GPLv3](https://en.wikipedia.org/wiki/GNU_General_Public_License#Version_3), você pode lê-la no arquivo __LICENSE__.

## Instalação do projeto

_Considere utilizar a versão mais recente do Python3._

* Copiar o repositório: `git clone https://github.com/alexandre/censo-cnfe`
* Criar um vrtualenv: `mkproject -p $(which python3) censo-cnfe`
* Instalar dependências: `pip install -r requirements.txt`

