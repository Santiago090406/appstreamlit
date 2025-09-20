import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="💝 Día del Amor y la Amistad", page_icon="💖", layout="centered")

# Título principal
st.markdown("<h1 style='text-align: center; color: #FF4B91;'>💘 ¡Feliz Día del Amor y la Amistad! 💘</h1>", unsafe_allow_html=True)

# Mensaje especial
st.markdown(
    """
    <div style="text-align: center; font-size: 20px; color: #FF6F91;">
        Hoy celebro tenerte en mi vida, porque eres alguien <b>única y especial</b>.  
        Que este día esté lleno de sonrisas, cariño y momentos inolvidables.
        baja, abajo hay un regalo 😉 TE QUIERO
    </div>
    """,
    unsafe_allow_html=True,
)

# Animación de corazoncito
placeholder = st.empty()
for i in range(6):
    if i % 2 == 0:
        placeholder.markdown("<h1 style='text-align: center; color: red;'>❤️</h1>", unsafe_allow_html=True)
    else:
        placeholder.markdown("<h1 style='text-align: center; color: pink;'>💖</h1>", unsafe_allow_html=True)
    time.sleep(0.5)

# Imagen decorativa (puedes cambiar el link a otra imagen/gif romántico)
st.image("https://pm1.aminoapps.com/6404/dfc00d9165d7db945e543d84b813083add7171e8_hq.jpg", caption="Un corazón que late por ti 💓", use_column_width=True)

# Botón sorpresa
if st.button("💌 Haz clic aquí para tu sorpresa"):
    st.success("✨ Eres alguien muy importante para mi, aunque aveces no estoy,convivir estos hermosos momentos en el colegio han sido hermosos para mi cada dia espero volverte a ver aunque se que hay momentos en los que simplemente no se puede dar, pero sabes aunque dices que es una palabra muy fuerte, te amo, aunque no sepa como este mi corazon, mi mente si esta dispuesta a verte; 💖hasta los 1000 Dias💖💕")
