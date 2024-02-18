<img src="docs/assets/ale-logo-color.svg" width="70">

# Alê API - Exemplo base com FastAPI

# Contexto Geral

Bem vindo ao repositório da aplicação **Alê API**!

# Documentação

A documentação da API está organizada em 3 partes de acordo com o objetivo em relação a aplicação.

- [Implementação](#implementação)
- [Rotas da API](#rotas-da-api)
- [Repositório](#repositório)

## Implementação

A Documentação de Implementação tem o objetivo de descrever detalhes de implementação dos métodos da aplicação com foco em desenvolvedores que irão escrever código fonte.

Para ter acesso a Documentação de Implementação no navegador execute o seguinte comando no terminal:

```bash
task docs
```

> Ative o [ambiente virtual](#ambiente-virtual) para executar o comando

## Rotas da API

A Documentação das Rotas da API é feita utilizando OpenAPI e tem foco em desenvolvedores que precisam integrar com esta API.  
Para ter acesso a documentação basta executar a aplicação e acessar a rota raiz (http://localhost:8123/) no navegador:

```bash
task run
```

> Ative o [ambiente virtual](#ambiente-virtual) para executar o comando

## Repositório

**\*Este documento!\*\***  
Neste documento está descrito o contexto e o propósito desta aplicação. Além de detalhar o que é necessário para configurar o ambiente de desenvolvimento e subir a aplicação.

# Pré-Requisitos

![python](https://img.shields.io/badge/python-v3.12-blue)
[![poetry](https://img.shields.io/badge/poetry-venv-orange)](https://python-poetry.org/docs/basic-usage/)

Além dos pré-requisitos sugerimos fortemente que instale e configure as [Recomendações para o ambiente de desenvolvimento](#recomendações-para-o-ambiente-de-desenvolvimento).

Com a versão correta do python e última versão do Poetry instalados, você poderá executar o comandos necessários para desenvolver e rodar a aplicação:

## Instalar dependências

```bash
poetry env use 3.12.2
```

```bash
poetry install --no-root
```

Utilize este comando para instalar todas as dependências da aplicação (configuradas no arquivo **_pyproject.tom_**).

## Ambiente Virtual

```bash
poetry shell
```

> Pré requisito para qualquer outro comando

Sempre que abrir um novo terminal é necessário executar este comando para garantir que está no ambiente virtual (venv) com os requisitos da aplicação devidamente instalados.

# Tasks

Diversas tasks (comandos personalizados de terminal) foram configuradas para facilitar o desenvolvimento.  
Veja as configurações na seção [tool.taskipy.tasks] do **_pyproject.toml_**  
Para listar todas as tasks disponíveis execute:

```bash
task --list
```

ou

```bash
task -l
```

> Ative o [ambiente virtual](#ambiente-virtual) para executar o comando

```bash
TASKS DISPONÍVEIS:
run         Executa o projeto
check       Aplica o linter e conduz uma verificação completa do projeto
lint        Aplica o linter no código
docs        Faz o build e serve a documentação do projeto em um servidor web local
req         Exporta o arquivo 'requirements.txt'
sec         Realiza uma auditoria de segurança nas dependências do pip
test        Executa todos os testes unitários
cov         Executa os testes e abre a pasta do relatório HTML de cobertura de testes
report      Abre a pasta do relatório HTML de cobertura de testes
docker      Faz o build da imagem e executa o container docker com docker-compose
clean       Limpa o cache do projeto
docs_build  Faz o build da documentação do projeto
lint_check  Imprime no terminal relatório de linting, sem aplicar modificações
pre_cov     Executa automaticamente os testes antes do comando 'task cov'
post_check  Executa automaticamente após o comando 'task check'
```

# Recomendações para o ambiente de desenvolvimento

![Windows 10/11](https://flat.badgen.net/badge/icon/windows10~11?icon=windows&label) ![WSL2 Ubuntu](https://flat.badgen.net/badge/WSL2/Ubuntu/orange) ![VSCode](https://flat.badgen.net/badge/icon/VSCode?icon=visualstudio&label)

Sugerimos que configure seu ambiente de desenvolvimento no WSL2 com Ubuntu, e utilize o VSCode com as extensões de Remote WSL.  
Aqui tem um guia super simplificado pra fazer isso com poucos comandos:  
https://github.com/alexandremendoncaalvaro/wsl-python

### Gerenciamento de versões do python:

- [pyenv](https://github.com/pyenv/pyenv)

### Gerenciamento de bibliotecas organizando em ambientes virtuais, de forma similar ao Nodejs:

- [poetry](https://python-poetry.org/docs/basic-usage/)

## Extensões recomendadas do VSCode

Pesquise nas extensões do VSCode para habilitar.  
Todas as sugestões são gratuitas.

**Acesso remoto ao WSL:**

- WSL

**Desenvolvimento Python:**

- Python
- Python Test Explorer for Visual Studio Code
- Black Formatter
- isort
- Even Better TOML

**Correção ortográfica:**

- Code Spell Checker
- Brazilian Portuguese - Code Spell Checker

**Autocompletar:**

- Path Intellisense

**Recursos Git**

- Git Graph

**Fluxogramas no README**

- Draw.io Integration

**Mob Programming/ Pair Programming remoto**

- Live Share
