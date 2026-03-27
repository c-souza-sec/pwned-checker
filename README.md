# 🔐 Verificador de Vazamento de Senhas

Uma aplicação simples em Python com interface gráfica (Tkinter) que verifica se uma senha já foi exposta em vazamentos de dados conhecidos utilizando a **API Have I Been Pwned**.

## 🚀 Funcionalidades

* Verifica se uma senha foi vazada
* Utiliza hash SHA-1 (modelo de k-anonimato)
* Interface gráfica simples e intuitiva
* Feedback em tempo real para o usuário
* Tratamento de erros de conexão

## 🛠️ Tecnologias Utilizadas

* Python 3
* Tkinter (interface gráfica)
* Requests (requisições HTTP)
* Hashlib (biblioteca nativa para hash)

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/c-souza-sec/pwned-checker.git
cd pwned-checker
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

```bash
python interface.py
```

## 🔎 Como Funciona

* A senha é convertida em um hash SHA-1
* Apenas os 5 primeiros caracteres do hash são enviados para a API
* A API retorna possíveis correspondências
* O aplicativo verifica se o restante do hash está presente na resposta

Esse método garante que sua senha nunca seja totalmente exposta (modelo de k-anonimato).

## ⚠️ Aviso

Este projeto é para fins educacionais.
Evite utilizar senhas reais ou sensíveis durante os testes.

## 📁 Estrutura do Projeto

```
├── interface.py
├── requirements.txt
└── README.md
```

## ✨ Melhorias Futuras

* Adicionar indicador de carregamento
* Melhorar o design da interface
* Converter para executável (.exe)
* Adicionar verificador de força de senha

## 🤝 Contribuição

Sinta-se à vontade para fazer um fork deste repositório e enviar pull requests.

## 📄 Licença

Este projeto é open-source e está disponível sob a licença MIT.
