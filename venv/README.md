# Gerenciador de Alunos (CRUD com MongoDB)

Este projeto é uma aplicação de console simples, desenvolvido em Python, que implementa um sistema de gerenciamento de alunos. Ele demonstra as quatro operações fundamentais de um banco de dados CRUD (Create, Read, Update, Delete) utilizando o MongoDB como sistema de gerenciamento de banco de dados NoSQL.

A aplicação possui uma estrutura modular, separando as responsabilidades de conexão com o banco, operações de manipulação de dados e funções utilitárias para uma melhor organização e manutenção do código.


## 🚀  Funcionalidades
O sistema oferece um menu interativo que permite ao usuário:

- Adicionar Aluno (Create): Cadastrar um novo aluno fornecendo informações como nome, idade, sexo, cidade e curso.

- Consultar Alunos (Read): Visualizar os registros dos alunos. Esta opção permite:

        1. Listar todos os alunos cadastrados.

        2. Filtrar alunos por um campo específico (ex: nome, cidade, curso).

- Atualizar Aluno (Update): Modificar as informações de um aluno já existente, identificando-o pelo seu **`ID único`**.

- Deletar Aluno (Delete): Remover o registro de um aluno do banco de dados, também por meio do **`seu ID`**.


## 🛠️ Estrutura do Projeto
O código-fonte está organizado nos seguintes arquivos:

- **`main.py`**: Ponto de entrada da aplicação. É responsável por exibir o menu principal e gerenciar o fluxo do programa, chamando as funções apropriadas de acordo com a escolha do usuário.

- **`banco_de_dados.py`**: Contém a função para estabelecer a conexão com o servidor MongoDB e selecionar o banco de dados e a coleção que serão utilizados pela aplicação.

- **`crud.py`**: Implementa toda a lógica para as operações de Create, Read, Update e Delete na coleção de estudantes no MongoDB.

- **`utilitarios.py`**: Agrupa funções de apoio, como a limpeza da tela do console e a formatação da exibição dos dados de um estudante.
## 📋 Pré-requisitos
Para executar este projeto, você precisará ter os seguintes softwares instalados:

- [Python 3](https://www.python.org/downloads/)

- [MongoDB](https://www.mongodb.com/try/download/community)

A biblioteca **`pymongo`** para Python.
## ⚙️ Instalação e Execução
Siga os passos abaixo para configurar e rodar o código:
1. Clone o repositório ou baixe os arquivos diretamente.

2. Instale a dependência pymongo usando o pip:

            
         pip install pymongo
            
3. Inicie o servidor MongoDB: Certifique-se de que o seu serviço do MongoDB esteja ativo e rodando no endereço padrão (**`mongodb://localhost:27017/`**), que é o configurado no **`arquivo banco_de_dados.py`**.

Após a execução, o menu interativo será exibido no console, e você poderá começar a gerenciar os registros dos alunos.

## ✍️ Exemplo de Uso
Ao iniciar o programa, você verá a seguinte interface:
```
===== Gerenciador de Alunos (CRUD MongoDB) =====
1. Adicionar Aluno (Create)
2. Consultar Alunos (Read)
3. Atualizar Aluno (Update)
4. Deletar Aluno (Delete)
5. Sair
==================================================
Escolha uma opção:
```
Basta inserir o número correspondente à operação desejada e seguir as instruções apresentadas.