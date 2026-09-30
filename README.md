# 🛍️ ShopAI
## 🖥️ Interface

![Interface do ShopAI](assets/shopai-interface.png)

Assistente virtual para uma loja online desenvolvido como projeto de estudo
utilizando Python, Streamlit e integração com a OpenAI API.

## 📌 Sobre o projeto

O ShopAI foi desenvolvido durante meus estudos de Vibe Coding e desenvolvimento
de aplicações com Inteligência Artificial.

A aplicação possui uma interface de chat construída com Streamlit e mantém
o histórico da conversa durante a sessão.

## 🚀 Funcionalidades

- Interface de chat com Streamlit
- Histórico de mensagens durante a sessão
- Prompt de sistema para definir o comportamento do assistente
- Integração com OpenAI API
- Variáveis de ambiente para proteção da API Key

## 🛠️ Tecnologias

- Python
- Streamlit
- OpenAI API
- python-dotenv
- Git
- GitHub

## 📚 O que aprendi

Durante o desenvolvimento pratiquei:

- configuração do ambiente Python;
- instalação de dependências com pip;
- utilização de bibliotecas Python;
- criação de aplicações com Streamlit;
- integração com APIs;
- utilização de variáveis de ambiente;
- depuração e interpretação de erros;
- conceitos iniciais de segurança de credenciais.

## ⚙️ Como executar

Clone o repositório:

git clone URL_DO_REPOSITORIO

Entre na pasta do projeto e instale as dependências:

pip install -r requirements.txt

Crie um arquivo `.env`:

OPENAI_API_KEY=sua_chave_aqui

Execute:

streamlit run app.py

## 🔐 Segurança

A chave da API não está armazenada no código-fonte.

As credenciais são carregadas através de variáveis de ambiente utilizando
python-dotenv e o arquivo `.env` está incluído no `.gitignore`.

## 📌 Status

Projeto educacional.

A interface e o fluxo local foram executados com sucesso. A integração com
a OpenAI API está implementada. A geração de respostas requer créditos
disponíveis na conta da API utilizada.

## 👨‍💻 Autor

Filipe Santos Coutinho

Estudante de Análise e Desenvolvimento de Sistemas.