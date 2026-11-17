# 🚌 Automação Web – Coleta de Dados de Linhas de Ônibus

## 📌 Sobre o Projeto

Este projeto consiste em uma aplicação desenvolvida em **Python** que utiliza automação web para navegar pelo site [Ônibus.info](https://onibus.info/linhas) e coletar informações sobre o transporte público.

Através da biblioteca **Playwright**, a aplicação automatiza a navegação entre os terminais e as páginas das linhas de ônibus, extraindo informações que podem ser utilizadas posteriormente em processos de organização, análise e tratamento de dados.

O projeto foi desenvolvido com o objetivo de explorar conceitos de automação web, web scraping e coleta automatizada de informações.

## ⚙️ Tecnologias Utilizadas

- **Python:** Linguagem utilizada no desenvolvimento da aplicação.
- **Playwright:** Biblioteca responsável pela automação do navegador e interação com elementos das páginas web.

## 🚀 Funcionalidades

- Abertura automatizada do site Ônibus.info.
- Identificação e navegação pelos terminais disponíveis.
- Acesso automatizado às páginas das linhas de ônibus.
- Extração do nome e código de identificação das linhas.
- Identificação dos sentidos de circulação.
- Coleta dos nomes das paradas de ônibus.
- Organização das informações em objetos Python.

## 📂 Estrutura do Projeto

```text
AutomacaoWeb/
│
├── main.py           # Script principal de automação web
├── informacoes.py    # Classes para organização dos dados coletados
└── README.md         # Documentação do projeto
```

## 💻 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Izillen/AutomacaoWeb.git
```

### 2. Acesse a pasta do projeto

```bash
cd AutomacaoWeb
```

### 3. Instale as dependências

```bash
pip install playwright
```

### 4. Execute a aplicação

```bash
python main.py
```

**Observação:** A aplicação está configurada para utilizar o Microsoft Edge (`msedge`). É necessário ter o navegador instalado para executar a automação conforme a configuração atual.

## 🧠 Conhecimentos Aplicados

Durante o desenvolvimento deste projeto, foram explorados conceitos importantes de:

- Automação de processos web.
- Web Scraping e extração de informações.
- Manipulação de elementos HTML.
- Navegação automatizada entre páginas.
- Programação orientada a objetos (POO).
- Organização e estruturação de dados com Python.
