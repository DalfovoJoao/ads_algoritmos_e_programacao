# Sistema Web de Lista de Compras 🛒

Projeto acadêmico da disciplina de **Algoritmos e Programação**, do curso de Análise e Desenvolvimento de Sistemas (ADS).

## Objetivo

Praticar lógica de programação e organização de código em uma aplicação de lista de compras.

A estrutura web foi preparada pelo professor; o exercício propõe o desenvolvimento da lógica do sistema pelos alunos, em equipe.

## Tecnologias

- Python
- Flask
- HTML
- SQLite

## Funcionalidades presentes no código

- Páginas de cadastro e login;
- Criação de listas de compras;
- Inclusão de itens com nome, código de barras, preço e quantidade;
- Visualização dos itens cadastrados;
- Consulta de item por código de barras.

## Como executar localmente

1. Instale o **Python 3**.
2. Baixe este repositório e abra a pasta no terminal.
3. Instale o Flask:

   ```bash
   python -m pip install flask
   ```

4. Execute:

   ```bash
   python server.py
   ```

5. No navegador, acesse `http://127.0.0.1:5000`.

> Dependendo do seu ambiente, o comando pode ser `python3` em vez de `python`.

## Organização

- `main.py`: classe principal e regras da aplicação;
- `server.py`: rotas Flask;
- `shoppinglib/`: módulos de usuários, itens, listas e banco de dados;
- `templates/`: páginas HTML;
- `static/`: arquivos estáticos;
- `main_not_send.py`: exercício alternativo de terminal, preservado como histórico de estudo.

## Conceitos praticados

Condições, funções, listas, módulos, entrada e validação de dados, rotas web e persistência em banco de dados.

## Limitações

Este repositório é um **projeto educacional**, não uma aplicação pronta para produção. A implementação atual precisa de melhorias em autenticação, gerenciamento de sessões, tratamento de erros e proteção das credenciais antes de qualquer uso real. Não utilize senhas reais ao testar.

Os arquivos `.db` que já fazem parte do histórico devem ser conferidos antes de qualquer compartilhamento ou reutilização com dados reais.
