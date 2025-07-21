import streamlit as st
import requests

API_URL = "http://localhost:8000/upload"  # mude para o IP da sua EC2 quando for rodar lá

st.title("Uploader de Arquivo Excel")

uploaded_file = st.file_uploader("Selecione o arquivo Excel", type=["xlsx"])

if uploaded_file:
    if st.button("Enviar para API"):
        files = {"file": (uploaded_file.name, uploaded_file.read())}
        response = requests.post(API_URL, files=files)
        st.write(response.json())
