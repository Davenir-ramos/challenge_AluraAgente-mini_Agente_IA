# Mini Agente IA de Documentos 🤖

Agente IA que lê um documento PDF e responde perguntas sobre o seu conteúdo, usando um modelo de linguagem via API da NVIDIA.

## 📋 Descrição do Projeto

Este projeto foi desenvolvido como parte de um challenge individual. O objetivo é construir um agente capaz de:

1. Ler um documento (PDF) escolhido pelo usuário.
2. Compreender seu conteúdo.
3. Responder perguntas relacionadas a esse conteúdo, baseando-se exclusivamente no texto do documento.

A aplicação conta com uma interface web simples (Streamlit) onde o usuário faz upload do PDF e digita perguntas em linguagem natural.

## 🏗️ Arquitetura

```
Usuário → Interface (Streamlit) → Extração de texto (pypdf)
                                         │
                                         ▼
                              Prompt (documento + pergunta)
                                         │
                                         ▼
                        API da NVIDIA (modelo de linguagem)
                                         │
                                         ▼
                              Resposta exibida na interface
```

Fluxo:
1. O usuário acessa a interface e envia um arquivo PDF.
2. O texto é extraído localmente com `pypdf` e guardado na sessão do Streamlit (`st.session_state`), para não reprocessar o PDF a cada pergunta.
3. O usuário digita uma pergunta na interface.
4. A pergunta é enviada junto com o texto do documento para o modelo de linguagem, com uma instrução de sistema para responder apenas com base no conteúdo fornecido.
5. A resposta do modelo é exibida diretamente na tela.

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal do projeto
- **Streamlit** — interface web (upload de arquivo, campo de pergunta, exibição de resposta)
- **pypdf** — extração de texto de arquivos PDF
- **OpenAI SDK** (compatível com a API da NVIDIA) — comunicação com o modelo de linguagem
- **NVIDIA NIM** (build.nvidia.com) — modelo de linguagem usado para gerar as respostas (`meta/llama-3.1-8b-instruct`)
- **python-dotenv** — carregamento da chave de API a partir de variáveis de ambiente
- **Oracle Cloud Infrastructure (OCI)** — hospedagem/deploy da aplicação com URL pública

## ⚙️ Instruções de Instalação

### Pré-requisitos
- Python 3.10+ instalado
- Uma API Key gratuita da NVIDIA (obtida em [build.nvidia.com](https://build.nvidia.com))

### Passo a passo

```bash
# 1. Clone o repositório
git clone <url-do-seu-repositorio>
cd mini_Agente_IA

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS

# 3. Instale as dependências
pip install openai fastapi uvicorn python-dotenv pypdf streamlit

# 4. Configure sua API Key
# Crie um arquivo .env na raiz do projeto com o conteúdo:
# NVIDIA_API_KEY=nvapi-sua-chave-aqui

# 5. Rode a aplicação
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`.

## 💬 Exemplos de Perguntas e Respostas

> Exemplos ilustrativos — atualize com perguntas reais feitas sobre o documento utilizado no seu teste.

**Pergunta:** "Qual é o tema principal deste documento?"
**Resposta:** *(resposta gerada pela IA com base no PDF enviado)*

**Pergunta:** "Existe alguma data ou prazo mencionado no texto?"
**Resposta:** *(resposta gerada pela IA com base no PDF enviado)*

**Pergunta:** "Resuma o documento em três frases."
**Resposta:** *(resposta gerada pela IA com base no PDF enviado)*

## 🚀 Deploy



URL pública: *(adicionar aqui após o deploy)*

## 📁 Estrutura do Projeto

```
mini_Agente_IA/
├── app.py            # Interface Streamlit (upload, extração de texto, chamada à IA)
├── .env              # Variáveis de ambiente (não versionar!)
├── .gitignore
└── README.md         # Este arquivo
```

## 📄 Licença

Projeto acadêmico, desenvolvido para fins de aprendizado.