#!/bin/bash

# Activar el entorno virtual
source venv/bin/activate

# Ejecutar la aplicación
streamlit run app.py

# Desactivar el entorno virtual al salir
deactivate 