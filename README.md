# censo-cnde-parser

Esse projeto tem como objetivo oferecer uma maneira de "processar" (entenda-se "gerar uma representação que facilite a análise") [e/ou importar] os dados [públicos] do ultimo censo do IBGE. Esse projeto não tem qualquer vinculo com o IBGE, é uma iniciativa livre e comunitária.

## Sobre a licença escolhida

Nós acreditamos que o esforço para obter os dados, processá-los, estruturá-los em uma base de dados e etc pode ser bem menor se as pessoas compartilharem o seu trabalho. Esse projeto é de uso livre (seguindo a ideia "free as in freedom") e escolhemos a licensa [GPLV3](https://github.com/dados-ibge/censo-cnde-parser/blob/master/LICENSE) como uma maneira de garantir que todos possam usufruir de melhorias no projeto (o que não limita o objetivo final e individual).

# Descrição da organização do projeto

## Layouts

Diretório responsável por guardar o arquivo de layout oferecido pelo IBGE e outros formatos do mesmo arquivo para facilitar o processo de parsing.

Até o momento, além do arquivo `.xls`, há um arquivo `.json` com uma construção simples.

## Dados

Diretório responsável por guardar maneiras de obter os dados do ultimo censo. Além do endereço FTP do IBGE pode ser interessante estabelecer cópias desses dados para não prejudicar o servidor do IBGE.

## Banco pré processado

Além da[s] ferramenta[s] para "processar" os dados, em cada laboratório há algum tipo de script que permite importar os dados para um banco de dados específico.
Com o objetivo de compartilhar essas bases de dados "pré processadas", esse diretório contém informações sobre como obter essas
bases (e.g. links para download ou torrent). Nesse diretório há também links para base de dados enriquecidas (e.g. o censo não conseguiu levantar todos os dados sobre latitude e longitude de cada CEP, mas utilizando outras ferramentas foi possível recuperar essas informações e atualizar a base de dados)

## Configuração

Diretório responsável por guardar arquivos de configuração genéricos para os laboratórios que "processam" os dados. Além disso é nesse diretório que ficam os arquivos de configuração/conexão para os bancos de dados (e.g. mongodb, dynamodb).

*Todos esses arquivos consideram apenas o ambiente de desenvolvimento e não contém qualquer informação sensível (e.g. host, usuário, senha, etc)*

## Laboratórios

Códigos em uma linguagem específica para processar os dados utilizando as informações descritas nos demais diretórios. Em um segundo momento, pode ser interessante dividir esses laboratórios em repositórios especificos.

Até o momento, há apenas dois laborabórios: um com a linguagem Python e outro com a linguagem Racket.
