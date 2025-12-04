"""
Punto de entrada de la aplicación
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🚀 Iniciando aplicación de Finanzas Personales...")
    print("📊 Dashboard disponible en: http://localhost:5000")
    print("⚠️  Recuerda configurar tus credenciales de Firebase en .env")
    app.run(debug=True, host='0.0.0.0', port=5000)

