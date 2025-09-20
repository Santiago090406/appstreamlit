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
        Hoy celebro tenerte en mi vida, porque eres alguien <b>único y especial</b>.  
        Que este día esté lleno de sonrisas, cariño y momentos inolvidables.  
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
st.image("https://co.pinterest.com/pin/81275968271251412/", caption="Un corazón que late por ti 💓", use_column_width=True)

# Botón sorpresa
if st.button("💌 Haz clic aquí para tu sorpresa"):
    st.success("✨ Eres muy importante para mí, gracias por ser parte de mi vida. 💕")

