import streamlit as st
from datetime import datetime
from PIL import Image
import requests

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

# --- SEÇÃO DE FOTOS ---
try:
    img1 = Image.open('ana e heitor3.jpg')
    img2 = Image.open('ana e heitor4.jpg')
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.image(img1, use_container_width=True)
    with col_f2:
        st.image(img2, use_container_width=True)
except FileNotFoundError:
    st.warning("Imagens não encontradas no diretório.")

# --- CONTADOR ---
data_casamento = datetime(2026, 10, 3, 17, 0)
falta = data_casamento - datetime.now()

st.write("---")
c1, c2, c3 = st.columns(3)
c1.metric("Dias", falta.days)
c2.metric("Horas", falta.seconds // 3600)
c3.metric("Minutos", (falta.seconds // 60) % 60)

# --- LOCALIZAÇÃO ---
st.write("---")
st.write("### Localização")
st.markdown("Grajagan Resort - Ilha do Mel / PR")
st.map(latitude=-25.5562, longitude=-48.3375)

# --- LISTA DE PRESENTES (NOVO) ---
st.write("---")
st.write("### 🎁 Sugestões de Presentes")
st.write("Sua presença é o maior presente, mas se desejar nos mimar, aqui estão algumas sugestões:")

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.markdown("**☕ Cafeteira Retrô**")
    st.info("Valor: R$ 150,00")
    if st.button("Presentear Cafeteira"):
        st.write("Chave PIX: **kelin.rrizzi@gmail.com**")

with col_p2:
    st.markdown("**🏖️ Jantar Romântico**")
    st.info("Valor: R$ 300,00")
    if st.button("Presentear Jantar"):
        st.write("Chave PIX: **kelin.rrizzi@gmail.com**")

# --- RSVP E RECADO (INTEGRADOS PARA E-MAIL) ---
st.write("---")
st.subheader("💌 RSVP & Recado para os Noivos")

email_destino = "kelin.rrizzi@gmail.com"

with st.form("form_contato", clear_on_submit=True):
    nome_user = st.text_input("Seu nome:")
    presenca = st.radio("Você irá ao evento?", ("Sim, com certeza!", "Infelizmente não poderei ir"))
    mensagem_user = st.text_area("Deixe seu recado:")
    
    submit = st.form_submit_button("Enviar para os Noivos")

    if submit:
        if nome_user and mensagem_user:
            link_envio = f"https://formsubmit.co/ajax/{email_destino}"
            dados = {
                "Nome": nome_user,
                "Presença": presenca,
                "Mensagem": mensagem_user,
                "_subject": f"Novo RSVP/Recado de {nome_user}"
            }
            try:
                requests.post(link_envio, data=dados)
                st.success(f"Feito, {nome_user}! Sua mensagem foi enviada. ❤️")
            except:
                st.error("Erro ao enviar. Verifique sua conexão.")
        else:
            st.error("Por favor, preencha nome e mensagem.")

st.write("---")
st.markdown("<p style='font-size: 0.8em;'>Desenvolvido por Regina | iRizzi Tech</p>", unsafe_allow_html=True)
