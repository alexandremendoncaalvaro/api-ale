# Alê API

Bem vindo a Documentação de Implementação do Exemplo de API do Alê.  
Aqui você irá encontrar os detalhes de implementação dos métodos no código fonte desta aplicação.

## Documentação Automática

Esta página de documentação é gerada automaticamente com base na **_docstring_** documentada diretamente nos métodos da aplicação.  
Utilize o menu ao lado para obter os detalhes de implementação por módulo.

Para que a **_docstring_** seja listada corretamente, o script **_update_docs.sh_** executa automaticamente antes do build do **Mkdocs** (que gera esta documentação) varrendo a pasta **apps** para criar uma estrutura de pastas espelhada em **docs** contendo o arquivo com o nome do módulo e a extensão _.md_ e dentro deste arquivo referenciar o módulo correspondente com "**::: modulo**".  
Exemplo:

> original: ./app/core/openapi.py  
> gerado: ./docs/core/openapi.md  
> Conteúdo de **openapi.md**:

```
::: core.openapi
```

A partir desta estrutura o **Mkdocs** utiliza um plugin para gerar a documentação a partir das **_docstrings_**.  
Configuração no **mkdocs.yml**:

```
plugins:
  - mkdocstrings:
      handlers:
        python:
          paths: [app]
```

## Docstring Styleguide

Adotamos o [Guia de estilos do Google](https://google.github.io/styleguide/pyguide.html) para as docstrings.

[Este vídeo](https://youtu.be/zU0ECYN_C6k) contém exemplos práticos de como padronizar a documentação com docstrings.
