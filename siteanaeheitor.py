import streamlit as st
from datetime import datetime
from PIL import Image

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Ana & Heitor | Eternal", page_icon="🌿", layout="centered")

# --- ESTILO VISUAL (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #F7F3F0; }
    h1, h2, p { color: #5D473A; font-family: 'serif'; text-align: center; }
    .stButton>button { background-color: #A6634B; color: white; border-radius: 50px; width: 100%; border: none; padding: 10px; }
    .main-form { background-color: white; padding: 20px; border-radius: 15px; border: 1px solid #E0D6D0; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h4 style='text-align: center;'>A & H</h4>", unsafe_allow_html=True)
st.markdown("<p style='italic'>\"O amor é o elo perfeito\"</p>", unsafe_allow_html=True)
st.write("---")
st.title("Ana & Heitor")
st.markdown("### 03 DE OUTUBRO DE 2026")

# --- FOTOS ---
try:
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.image('ana e heitor3.jpg', use_container_width=True)
    with col_f2:
        st.image('ana e heitor4.jpg', use_container_width=True)
except:
    st.info("🌿 Espaço reservado para as fotos do casal.")

# --- CONTADOR ---
st.write("---")
data_casamento = datetime(2026, 10, 3, 17, 0)
falta = data_casamento - datetime.now()
c1, c2, c3 = st.columns(3)
c1.metric("Dias", falta.days)
c2.metric("Horas", falta.seconds // 3600)
c3.metric("Minutos", (falta.seconds // 60) % 60)

# --- LOCALIZAÇÃO ---
st.write("---")
st.write("### 📍 Localização")
st.markdown("Grajagan Resort - Ilha do Mel / PR")
st.map(latitude=-25.5562, longitude=-48.3375)

# --- LISTA DE PRESENTES ---
st.write("---")
st.write("### 🎁 Sugestões de Presentes")
col_p1, col_p2 = st.columns(2)
with col_p1:
    st.markdown("**☕ Cafeteira Retrô**\n\nValor: R$ 150,00")
    if st.button("Presentear Cafeteira"):
        st.code("PIX: kelin.rrizzi@gmail.com", language="text")
with col_p2:
    st.markdown("**🏖️ Jantar Romântico**\n\nValor: R$ 300,00")
    if st.button("Presentear Jantar"):
        st.code("PIX: kelin.rrizzi@gmail.com", language="text")

# --- RSVP E RECADOS (FORMULÁRIO SEGURO) ---
st.write("---")
st.subheader("💌 RSVP & Recado para os Noivos")

email_destino = "heitor.engmec@outlook.com"

# Criando o formulário HTML sem recuos para evitar bugs de exibição
form_html = f"""
<div class="main-form">
<form action="https://formsubmit.co/{email_destino}" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_subject" value="Novo Recado: Ana e Heitor">
<label>Seu Nome:</label><br>
<input type="text" name="name" required style="width: 100%; margin-bottom: 15px; border: 1px solid #A6634B; border-radius: 5px; padding: 8px;"><br>
<label>Você irá ao evento?</label><br>
<select name="Presença" style="width: 100%; margin-bottom: 15px; border: 1px solid #A6634B; border-radius: 5px; padding: 8px;">
<option value="Sim">Sim, com certeza!</option>
<option value="Não">Infelizmente não poderei ir</option>
</select><br>
<label>Sua Mensagem:</label><br>
<textarea name="message" required style="width: 100%; height: 100px; margin-bottom: 15px; border: 1px solid #A6634B; border-radius: 5px; padding: 8px;"></textarea><br>
<button type="submit" style="background-color: #A6634B; color: white; border: none; padding: 12px; border-radius: 50px; width: 100%; cursor: pointer; font-weight: bold;">
ENVIAR MENSAGEM AGORA
</button>
</form>
</div>
"""

st.markdown(form_html, unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='font-size: 0.8em;'>Desenvolvido por Regina | iRizzi Tech</p>", unsafe_allow_html=True)
