import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime
import os
from PIL import Image
import io
import base64
from openai import OpenAI
import pygame
from gtts import gTTS
from mindfulness import mindfulness_page

# Configuración de la API
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key="5b21115633f24d58a877a50410ac78eb",  # Clave de API de Nicolas
)

# Inicializar el estado de la sesión
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = {'date': [], 'mood': []}
if 'current_mood' not in st.session_state:
    st.session_state.current_mood = 5
if 'page' not in st.session_state:
    st.session_state.page = 'chat'
if 'voice_enabled' not in st.session_state:
    st.session_state.voice_enabled = False
if 'visual_enabled' not in st.session_state:
    st.session_state.visual_enabled = True

# Función para generar respuestas de texto
def get_ai_response(prompt):
    response = client.chat.completions.create(
        model="google/gemini-2.0-flash",
        messages=[
            {"role": "system", "content": "Eres un asistente de salud mental empático y profesional. Tu objetivo es brindar apoyo emocional, escuchar activamente, y ofrecer consejos útiles basados en técnicas de terapia cognitivo-conductual. No diagnostiques, pero sugiere buscar ayuda profesional cuando sea apropiado."},
            *st.session_state.messages,
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        top_p=0.7,
        frequency_penalty=1,
        max_tokens=512,
    )
    return response.choices[0].message.content

# Función para generar imágenes relajantes
def generate_calming_image(prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"Imagen relajante y terapéutica que represente: {prompt}. Estilo artístico suave, colores calmantes, sin texto.",
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        st.error(f"Error al generar imagen: {e}")
        return None

# Función para convertir texto a voz
def text_to_speech(text):
    tts = gTTS(text=text, lang='es', slow=False)
    filename = "response.mp3"
    tts.save(filename)
    return filename

# Función para reproducir audio
def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Cargar CSS personalizado
def load_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Interfaz de usuario con Streamlit
st.set_page_config(page_title="Asistente de Salud Mental", layout="wide")
load_css()

# Sidebar para navegación y opciones
with st.sidebar:
    st.title("Mi Bienestar")
    
    # Navegación
    st.markdown("### Navegación")
    if st.button("💬 Chat Terapéutico", key="nav_chat"):
        st.session_state.page = 'chat'
    if st.button("🧘 Mindfulness y Relajación", key="nav_mindfulness"):
        st.session_state.page = 'mindfulness'
    if st.button("📊 Mi Progreso", key="nav_progress"):
        st.session_state.page = 'progress'
    
    st.markdown("---")
    
    # Registro de estado de ánimo
    st.markdown("### ¿Cómo te sientes hoy?")
    mood = st.slider("", 1, 10, st.session_state.current_mood, key="mood_slider")
    
    if st.button("Registrar estado de ánimo", key="record_mood"):
        st.session_state.current_mood = mood
        st.session_state.mood_data['date'].append(datetime.now().strftime("%Y-%m-%d %H:%M"))
        st.session_state.mood_data['mood'].append(mood)
        st.success("¡Estado de ánimo registrado!")
    
    st.markdown("---")
    
    # Opciones para el chat
    if st.session_state.page == 'chat':
        st.markdown("### Opciones")
        st.session_state.voice_enabled = st.checkbox("Activar respuestas por voz", value=st.session_state.voice_enabled, key="voice_enabled_sidebar")
        st.session_state.visual_enabled = st.checkbox("Activar imágenes relajantes", value=st.session_state.visual_enabled, key="visual_enabled_sidebar")

# Página de chat
def chat_page():
    st.title("Asistente Virtual de Salud Mental")
    st.markdown("Conversa conmigo sobre cómo te sientes. Estoy aquí para escucharte y apoyarte.")
    
    # Mostrar el historial de mensajes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Entrada del usuario
    if prompt := st.chat_input("¿Cómo puedo ayudarte hoy?"):
        # Añadir mensaje del usuario al historial
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Mostrar indicador de "pensando"
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = get_ai_response(prompt)
                st.markdown(response)
                
                # Generar y mostrar imagen si está habilitado
                if st.session_state.visual_enabled and len(st.session_state.messages) % 2 == 0:
                    with st.spinner("Generando imagen relajante..."):
                        image_prompt = f"Una imagen relajante relacionada con: {prompt}"
                        image_url = generate_calming_image(image_prompt)
                        if image_url:
                            st.image(image_url, caption="Imagen relajante generada para ti")
                
                # Convertir respuesta a voz si está habilitado
                if st.session_state.voice_enabled:
                    with st.spinner("Generando respuesta de voz..."):
                        audio_file = text_to_speech(response)
                        st.audio(audio_file)
        
        # Añadir respuesta al historial
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Sección de recursos
    st.markdown("---")
    st.markdown("### Recursos de ayuda")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Líneas de ayuda
        - **Línea de crisis**: 800-123-4567
        - **Chat de apoyo emocional**: [www.apoyoemocional.org](https://www.apoyoemocional.org)
        - **Directorio de terapeutas**: [www.directorioterapeutas.org](https://www.directorioterapeutas.org)
        """)
    
    with col2:
        st.markdown("""
        #### Recursos de autoayuda
        - **Mindfulness para principiantes**: [Guía práctica](https://www.mindful.org)
        - **Ejercicios de respiración**: [Técnicas efectivas](https://www.respira.com)
        - **Diario de gratitud**: [Plantillas descargables](https://www.gratitud.org)
        """)

# Página de progreso
def progress_page():
    st.title("Mi Progreso Emocional")
    
    if not st.session_state.mood_data['date']:
        st.info("Aún no has registrado tu estado de ánimo. Utiliza el control deslizante en la barra lateral para comenzar a registrar cómo te sientes.")
        return
    
    # Mostrar gráfico de progreso
    st.markdown("### Evolución de tu estado de ánimo")
    df = pd.DataFrame(st.session_state.mood_data)
    
    # Gráfico principal
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(range(len(df['date'])), df['mood'], marker='o', linestyle='-', color='#1f77b4')
    ax.set_ylabel('Estado de ánimo (1-10)')
    ax.set_ylim(0, 11)
    ax.set_xticks(range(len(df['date'])))
    ax.set_xticklabels([d.split()[0] for d in df['date']], rotation=45)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title('Seguimiento de tu bienestar emocional')
    st.pyplot(fig)
    
    # Estadísticas
    st.markdown("### Estadísticas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Promedio", f"{np.mean(df['mood']):.1f}/10")
    
    with col2:
        st.metric("Mejor día", f"{np.max(df['mood'])}/10")
    
    with col3:
        st.metric("Tendencia", f"{df['mood'].iloc[-1] - df['mood'].iloc[0]:.1f}", 
                 delta_color="normal" if df['mood'].iloc[-1] - df['mood'].iloc[0] >= 0 else "inverse")
    
    # Tabla de registros
    st.markdown("### Historial de registros")
    st.dataframe(df.rename(columns={'date': 'Fecha', 'mood': 'Estado de ánimo'}))
    
    # Recomendaciones basadas en los datos
    st.markdown("### Recomendaciones personalizadas")
    
    avg_mood = np.mean(df['mood'])
    if avg_mood < 4:
        st.warning("Tu estado de ánimo promedio es bajo. Considera programar una consulta con un profesional de la salud mental.")
        st.markdown("""
        Recomendaciones:
        - Prueba las meditaciones guiadas en la sección de Mindfulness
        - Establece pequeñas metas diarias para aumentar tu sensación de logro
        - Mantén un diario de gratitud para enfocarte en aspectos positivos
        """)
    elif avg_mood < 7:
        st.info("Tu estado de ánimo está en un rango medio. Hay espacio para mejorar tu bienestar.")
        st.markdown("""
        Recomendaciones:
        - Incorpora ejercicio físico regular a tu rutina
        - Practica técnicas de respiración cuando te sientas estresado
        - Conecta con amigos o familiares que te brinden apoyo
        """)
    else:
        st.success("¡Tu estado de ánimo promedio es bueno! Sigue con tus prácticas positivas.")
        st.markdown("""
        Recomendaciones:
        - Continúa con las actividades que te hacen sentir bien
        - Comparte tus estrategias de bienestar con otros
        - Establece nuevos objetivos de crecimiento personal
        """)

# Renderizar la página correspondiente
if st.session_state.page == 'chat':
    chat_page()
elif st.session_state.page == 'mindfulness':
    mindfulness_page()
elif st.session_state.page == 'progress':
    progress_page() 