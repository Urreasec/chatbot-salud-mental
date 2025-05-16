# Asistente Virtual de Salud Mental

Un asistente virtual de salud mental que combina texto, voz y elementos visuales para ofrecer apoyo emocional en tiempo real.

## Características

- **Chatbot empático**: Utiliza procesamiento de lenguaje natural para mantener conversaciones empáticas y de apoyo.
- **Visuales relajantes**: Genera imágenes calmantes relacionadas con la conversación.
- **Respuestas por voz**: Convierte las respuestas de texto a voz humana sintética.
- **Dashboard de seguimiento**: Monitorea el estado emocional del usuario a lo largo del tiempo.

## Requisitos

- Python 3.8 o superior
- Conexión a Internet para las API de IA
- python3-venv (para crear entornos virtuales)

## Instalación

### Método automático

1. Clona este repositorio o descarga los archivos.
2. Ejecuta el script de instalación:

```bash
./run.sh
```

Este script creará un entorno virtual, instalará todas las dependencias y ejecutará la aplicación.

### Método manual

Si prefieres configurar manualmente, sigue estos pasos:

1. Clona este repositorio o descarga los archivos.
2. Crea un entorno virtual:

```bash
python3 -m venv venv
```

3. Activa el entorno virtual:

```bash
source venv/bin/activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecuta la aplicación:

```bash
streamlit run app.py
```

6. Cuando termines, desactiva el entorno virtual:

```bash
deactivate
```

También puedes ver las instrucciones manuales ejecutando:

```bash
./manual_setup.sh
```

## Uso

1. Una vez que la aplicación esté en ejecución, abre tu navegador en `http://localhost:8501`

2. Interactúa con el asistente:
   - Escribe tus pensamientos o preocupaciones en el chat
   - Registra tu estado de ánimo diario
   - Activa o desactiva las funciones de voz e imágenes según tus preferencias
   - Explora las técnicas de mindfulness y relajación
   - Visualiza tu progreso emocional en el dashboard

## Notas importantes

- Este asistente NO reemplaza a un profesional de salud mental.
- Toda la información se almacena localmente durante la sesión.
- Si experimentas una crisis, busca ayuda profesional inmediata. 