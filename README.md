# Documentação do Projeto [Blog Coletivo]

## Introdução
* **Objetivo:** Escreva o que vier à sua cabeça, nós registraremos pro mundo!
* **Tecnologias:** React no front-end, Flask no back-end

| **Desenvolvedor front-end chefe:** Mikael Baracho

- Github: <a href='https://github.com/MikaelBarachoOficial'>MikaelBarachoOficial</a>
- Instagram: <a href='https://www.instagram.com/omikaelbaracho/'>@omikaelbaracho</a>
- Linkedin: <a href="https://www.linkedin.com/in/mikael-baracho-9190571b2/">Mikael Baracho</a>

| **Desenvolvedor back-end chefe:**  Andressa Sales

- Github: <a href="https://github.com/AndressaSales"> Andressa Sales</a>
- Linkedin: <a href="https://www.linkedin.com/in/andressa-sales-04553a281/">Andresssa Sales</a>


<h1 style="color: cyan"> Front-End </h1>

## Uso
* **Iniciando o projeto:** > npm run dev (Agora é com o Vite react app)
* **Funcionalidades:**
    * Ler e imprimir os posts existentes
    * Fazer o post dos das mensagens e enivar para o server-side
    * ...
* **Exemplos de uso:** O usuário posta uma mensagem e vai direto para o servidor com data, nome e horário.

## Desenvolvimento
* **Estrutura do projeto:** O app rodará no client>src>App.jsx, onde se concentrará toda a informação que o usuário desejar, incluindo os posts e a caixa de escrever a mensagem
* **Contribuindo:** Precisando de uma API para ser tratada

## Licença
* Não temos licença haha

<h1 style="color: green"> Back-End </h1>

* **Bibliotecas e Frameworks**
    * usando o:
        * **Python**~> uma linguagem de programação versátil e amplamente utilizada conhecida por sua simplicidade e legibilidade. 
        * **Flask**~> Um micro framework web para o python, usado para aplicação web com APIs. 
        * **Peewee**~> Uma biblioteca ORM (Object-RElational Mappin  g) para python, que facilita a interação com bancos de dados.
        <br/>
    Com esses três elementos trabalhando juntos, foi possível criar uma API.
* **Funcionalidade:**
    * **1. Recuperação de Dados (GET)**
        * Permite que obtenham informações de todos os registros em uma tabela.

    * **2. Criação de Novos Registros (POST)**
        * Usado para adicionar novos usuários e postagens.


# Link da Api

    $ http://127.0.0.1:5000/user/
#
    * **Obs:** Caso não funcione, siga o manual

# Manual

* Antes de tudo você vai ter que instalar esses dois:
    # Install
    * **Flask:** 
        ```
       $ pip install flask
       ```
    * **Peewee:**
        ```
        $ pip install peewee
        ```

* Agora para ter acesso a pasta do backend, siga esses passos:

    * **1° Passo:**
        * para entra:
            * cd backend
            
    * **2° Passo:**
        * dentro da pasta do backend há um pasta com o nome **venv**, precisamos ativar este ambiente
            * .venv/bin/activate
                * **Obs:** se esse comando der um erro use esse comando: 
                    * Set-ExecutionPolicy RemoteSigned -Scope Process, depois ative de novo o ambiente
    * **3° Passo:**
        * run:
            * python main.py
    * **4° Passo:**
        * Aperte na url e bote:
            * /user, para acessar a api