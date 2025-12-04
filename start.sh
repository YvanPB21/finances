#!/bin/bash

echo "===================================="
echo "Dashboard de Finanzas Personales"
echo "===================================="
echo ""

# Verificar si existe el entorno virtual
if [ ! -d ".venv" ]; then
    echo "[1/4] Creando entorno virtual..."
    python3 -m venv .venv
    echo "Entorno virtual creado."
    echo ""
else
    echo "[1/4] Entorno virtual ya existe."
    echo ""
fi

# Activar entorno virtual
echo "[2/4] Activando entorno virtual..."
source .venv/bin/activate
echo ""

# Instalar/actualizar dependencias
echo "[3/4] Instalando dependencias..."
pip install -q -r requirements.txt
echo "Dependencias instaladas."
echo ""

# Verificar configuración
echo "[4/4] Verificando configuración..."
if [ ! -f ".env" ]; then
    echo "ADVERTENCIA: No se encontró el archivo .env"
    echo "Por favor, copia .env.example a .env y configúralo."
    echo ""
    exit 1
fi
echo "Configuración lista."
echo ""

# Ejecutar aplicación
echo "===================================="
echo "Iniciando servidor..."
echo "===================================="
echo ""
python main.py

