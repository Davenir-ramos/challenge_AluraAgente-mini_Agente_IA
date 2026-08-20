import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

st.set_page_config(page_title="Mini Assistente", page_icon="🤖")
st.title("🤖 Mini Assistente de Documentos")

# Guarda o texto extraído do PDF entre interações
if "texto_documento" not in st.session_state:
    st.session_state.texto_documento = None

arquivo = st.file_uploader("Envie um PDF", type="pdf")

if arquivo is not None and st.session_state.texto_documento is None:
    leitor = PdfReader(arquivo)
    texto = ""
    for pagina in leitor.pages:
        texto += pagina.extract_text() or ""
    st.session_state.texto_documento = texto
    st.success(f"PDF carregado! ({len(leitor.pages)} páginas)")

if st.session_state.texto_documento:
    pergunta = st.text_input("Faça uma pergunta sobre o documento:")

    if pergunta:
        with st.spinner("Pensando..."):
            resposta = client.chat.completions.create(
                model="meta/llama-3.1-8b-instruct",
                messages=[
                    {
                        "role": "system",
                        "content": "Responda apenas com base no documento fornecido. Se a resposta não estiver no texto, diga que não sabe."
                    },
                    {
                        "role": "user",
                        "content": f"Documento:\n{st.session_state.texto_documento}\n\nPergunta: {pergunta}"
                    }
                ],
            )
            st.write(resposta.choices[0].message.content)