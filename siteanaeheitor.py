import streamlit as st
from datetime import datetime
from PIL import Image

# --- CONFIGURAÇÃO BOHO CHIC ---
st.set_page_config(page_title="Ana & Heitor | Eternal", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #F7F3F0; }
    h1, h2, p { color: #5D473A; font-family: 'Playfair Display', serif; text-align: center; }
    h3 { color: #A6634B; text-align: center; font-family: 'Lato', sans-serif; text-transform: uppercase; letter-spacing: 2px; }
    .stButton>button { background-color: #A6634B; color: white; border-radius: 50px; border: none; width: 100%; }
    .stImage > img { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("#### A & H")
st.markdown("*\"O amor é o elo perfeito\"*")
st.write("---")
st.title("Ana & Heitor")
st.markdown("### 03 DE OUTUBRO DE 2026")

# --- SEÇÃO DE FOTOS LADO A LADO ---
try:
    img1 = Image.open('ana e heitor3.jpg')
    img2 = Image.open('ana e heitor4.jpg')
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.image(img1, use_container_width=True)
    with col_f2:
        st.image(img2, use_container_width=True)
except FileNotFoundError:
    st.warning("Dica: Certifique-se de que as fotos 'ana e heitor3.jpg' e 'ana e heitor4.jpg' estão na mesma pasta do código!")

# --- CONTADOR ---
data_casamento = datetime(2026, 10, 3, 17, 0)
falta = data_casamento - datetime.now()

st.write("---")
c1, c2, c3 = st.columns(3)
c1.metric("Dias", falta.days)
c2.metric("Horas", falta.seconds // 3600)
c3.metric("Minutos", (falta.seconds // 60) % 60)

# --- LOCAL E RSVP ---
st.write("---")
st.write("### Localização")
st.markdown("Grajagan Resort - Ilha do Mel / PR")
st.map(latitude=-25.5562, longitude=-48.3375)

st.write("---")
st.write("### RSVP")
nome = st.text_input("Seu Nome")
if st.button("Confirmar Presença"):
    st.success(f"Presença de {nome} confirmada!")

st.write("---")
st.markdown("<p style='font-size: 0.8em;'>Desenvolvido por Regina | iRizzi Tech</p>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("💌 Deixe um recado para os noivos")

with st.form("meu_recado", clear_on_submit=True):
    nome_convidado = st.text_input("Seu nome:")
    mensagem = st.text_area("Sua mensagem carinhosa:")
    botao_enviar = st.form_submit_button("Enviar Mensagem")

    if botao_enviar:
        if nome_convidado and mensagem:
            st.success(f"Obrigado, {nome_convidado}! Seu recado foi enviado com sucesso. ❤️")
        else:
            st.error("Por favor, preencha o nome e a mensagem antes de enviar.")
