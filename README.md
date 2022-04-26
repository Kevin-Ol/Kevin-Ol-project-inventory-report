# Projeto Inventory Reports

Projeto feito como critério avaliativo na escola de programação Trybe.

Foi utilizada a linguagem de programação Python.

O objetivo do projeto foi consolidar o conhecimento em orientação a objetos, entendendo conceitos como Entidade, Abstração, Encapsulamento, Herança,
Polimorfismo, construtor, atributos e métodos. Também foram aplicados padrões de projeto Iterator e Strategy.

## Instruções para reproduzir o projeto

#### Pré Requisitos

Possuir Python instalado

---

1. Clone o repositório
  * `git@github.com:Kevin-Ol/project-inventory-report.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    * `cd project-inventory-report`

2. Inicie e ative um ambiente virtual
  * `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências
  * `python3 -m pip install -r dev-requirements.txt`

---

Os requisitos desenvolvidos no projeto são:

`inventory_report/reports/simple_report.py`

- Classe `SimpleReport`: possui um método de classe `generate` que possui como parâmetro uma lista de dicionários e retorna uma string 
formatada como um relatório;

`inventory_report/reports/complete_report.py`

- Classe `CompleteReport`: classe que herda o método de classe `generate` da classe `SimpleReport`, especializando seu comportamento e retornando uma 
string com maiores detalhes;

`inventory_report/inventory/inventory.py`

- Classe `Inventory`: possui um método de classe `import_data` que possui como parâmetros o caminho do arquivo e o tipo de relatório (simples ou completo)
e retorna o relatório desejado, se adaptando aos formatos csv, json ou xml;

`inventory_report/importer/importer.py`

- Classe `Importer`: classe abstrata para definir assinatura do método `import_data` em suas classes herdeiras: `CsvImporter`, `JsonImporter` e 
`XmlImporter`, responsáveis por fazer a leitura das respectivas extensões de arquivos, lançando erros quando necessário;

`inventory_report/inventory/inventory_iterator.py`

- Classe `InventoryRefactor`: refatoração da classe `Inventory`, aplicando o padrão de projeto strategy através do uso das classes herdadas de `Importer`.
Possui como parâmetro de inicialização qual classe `Importer` deve ser utilizada para leitura do arquivo e método de classe `import_data` semelhante ao 
da classe `Inventory`. Além disso foi criado um iterator modificado utilizando a classe `InventoryIterator`;

`inventory_report/main.py`

- Função `main`: função para gerar relatório utilizando a classe `InventoryRefactor` que pode ser executada no terminal em 
linhas de comando através da entrada:

``` bash
$ inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```
