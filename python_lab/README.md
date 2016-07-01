# Python lab

Versão Python do parser e CLI do projeto. Esse laboratório utiliza a versão `3.5.x`.

## CLI

A CLI está disponível através do arquivo `manage.py`, os comandos disponíveis são:

* `importar-dados <banco de dados> <caminho para arquivo .zip ou diretório>`
* `exportar-json <caminho para arquivo.zip ou diretório> <caminho salvar arquivos gerados>`


# Como preparar o ambiente

* Criar um virtualenv (considerando que você tem o [virtualenvwrapper] (https://gist.github.com/alexandre/a9f9015ac4f05472d98c) instalado:
```bash
mkproject -p $(which python3.5) censo-cnde-parser
```

* Instalar dependências:
```bash
pip install -r requirements.txt
```
