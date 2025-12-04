"""
Inicialización de la aplicación Flask
"""
from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    """Factory function para crear la aplicación Flask"""
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')

    # Configuración
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['JSON_SORT_KEYS'] = False

    # Registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app

