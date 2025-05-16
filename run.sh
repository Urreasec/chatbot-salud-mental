#!/bin/bash

echo "Verificando si python3-venv está instalado..."
if ! dpkg -l | grep -q python3-venv; then
    echo "Instalando python3-venv..."
    sudo apt-get update
    sudo apt-get install -y python3-venv
fi

echo "Creando entorno virtual..."
python3 -m venv venv

echo "Activando entorno virtual..."
source venv/bin/activate

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Iniciando el Asistente Virtual de Salud Mental..."
streamlit run app.py

# Desactivar el entorno virtual al salir
deactivate 