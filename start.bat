@echo off
python main.py
echo.
echo ====================================
echo Iniciando servidor...
echo ====================================
REM Ejecutar aplicación

echo.
echo Configuracion lista.
)
    exit /b 1
    pause
    echo.
    echo Por favor, copia .env.example a .env y configuralo.
    echo ADVERTENCIA: No se encontro el archivo .env
if not exist ".env" (
echo [4/4] Verificando configuración...
REM Verificar configuración

echo.
echo Dependencias instaladas.
pip install -q -r requirements.txt
echo [3/4] Instalando dependencias...
REM Instalar/actualizar dependencias

echo.
call .venv\Scripts\activate.bat
echo [2/4] Activando entorno virtual...
REM Activar entorno virtual

)
    echo.
    echo [1/4] Entorno virtual ya existe.
) else (
    echo.
    echo Entorno virtual creado.
    python -m venv .venv
    echo [1/4] Creando entorno virtual...
if not exist ".venv" (
REM Verificar si existe el entorno virtual

echo.
echo ====================================
echo Dashboard de Finanzas Personales
echo ====================================

