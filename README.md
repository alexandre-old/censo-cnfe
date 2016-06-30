# (Censo 2010) Cadastro Nacional de Endereços para fins estatisticos

Projeto para parsear e importar [em uma base mongodb] os dados do CNDE do ultimo censo realizado pelo IBGE. O projeto se divide em [basicamente] 2 partes:

* Parser para gerar uma representação JSON de cada arquivo [.txt]
* CLI para importar dados para a base dados MongoDB

## Layouts

Além da versão .xls oferecida pelo IBGE, há dentro desse projeto uma versão .json com o objetivo de facilitar
o processamento dos dados.
