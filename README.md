# MS-Candidatos 
## Microserviço de gerenciamento de dados dos candidatos da plataforma BAE Brasil

## 1. Instalação e Execução do Servidor Flask:
Importante: pressupõe-se o uso de gerenciadores de pacote e de ambientes virtuais como ```pip``` 
e ```venv```, respectivamente ou ```pipenv```.

### 1.1. Instalação das dependências:
```shell
pip install -r requirements.txt
```

### 1.2. Inicialização do banco de dados:
No diretório ```/src/api``` executar o comando:
```shell
flask init_db
```

### 1.3. Inicialização da aplicação:
No diretório ```/src/api``` executar o comando:
```shell
flask run
```

## 2. Endpoints Disponíveis:
### 2.1. Candidatos:
Schema
```json
{
  "id_candidato": "int",
  "nome_usuario": "str",
  "senha": "str",
  "nome_completo": "str",
  "data_nascimento": "datetime",
  "nacionalidade": "str",
  "lingua_nativa": "str",
  "portugues_fluente": "bool"
}
```
> **GET** <br>
> **Listar** todos os candidatos: ```/candidatos/list``` <br>
> **Buscar** por id_candidato ou nome_usuario: ```/candidatos/get``` <br>

> **POST** <br>
> **Criar** novo: ```/candidatos/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_candidato: ```/candidatos/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_candidato: ```/candidatos/delete```

### 2.2. Contatos:
Schema
```json
{
  "id_contato": "int",
  "descricao": "str",
  "complemento": "str",
  "tipo_contato": {
    "0": "Telefone",
    "1": "Celular",
    "2": "Email"
  },
  "id_candidato": "int" 
}
```
> **GET** <br>
> **Listar** todos os contatos ou todos contatos de um candidato por id_candidato: ```/contatos/list``` <br>
> **Buscar** por id_contato: ```/contatos/get``` <br>

> **POST** <br>
> **Criar** novo: ```/contatos/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_contato: ```/contatos/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_contato: ```/contatos/delete```

### 2.3. Documentos:
Schema
```json
{
  "id_documento": "int",
  "descricao": "str",
  "tipo_documento": "str", 
  "pais_emissao": "str",
  "data_emissao": "datetime",
  "id_candidato": "int" 
}
```
> **GET** <br>
> **Listar** todos os documentos ou todos documentos de um candidato por id_candidato: ```/documentos/list``` <br>
> **Buscar** por id_documento: ```/documentos/get``` <br>

> **POST** <br>
> **Criar** novo: ```/documentos/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_documento: ```/documentos/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_documento: ```/documentos/delete```
