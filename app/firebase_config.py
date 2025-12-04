"""
Configuración de Firebase Firestore
"""
import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

# Inicializar Firebase
def initialize_firebase():
    """Inicializa la conexión con Firebase"""
    try:
        # Verificar si ya está inicializado
        firebase_admin.get_app()
        # No está inicializado, proceder a inicializar
    except ValueError:
        cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')

        if not cred_path or not os.path.exists(cred_path):
            print("ADVERTENCIA: No se encontraron credenciales de Firebase.")
            print(f"Por favor, configura FIREBASE_CREDENTIALS_PATH en .env")
            print(f"Ruta buscada: {cred_path}")
            # Usar credenciales por defecto para desarrollo local sin Firebase
            cred = credentials.Certificate({
                "type": "service_account",
                "project_id": "demo-project",
            }) if False else None

            if cred is None:
                return None
        else:
            cred = credentials.Certificate(cred_path)

        firebase_admin.initialize_app(cred)

    # Obtener el nombre de la base de datos desde .env (OBLIGATORIO)
    database_name = os.getenv('FIREBASE_DATABASE_NAME')

    if not database_name:
        # No se especificó nombre de base de datos - ERROR
        print("❌ ERROR: FIREBASE_DATABASE_NAME no está configurado en .env")
        print("❌ Debes especificar el nombre de la base de datos en tu archivo .env")
        print("❌ Ejemplo: FIREBASE_DATABASE_NAME=finances")
        print("")
        print("⚠️  La aplicación NO puede continuar sin especificar una base de datos.")
        raise ValueError("FIREBASE_DATABASE_NAME es obligatorio en el archivo .env")

    print(f"📦 Usando base de datos: {database_name}")

    # Obtener el cliente de Firestore con la base de datos nombrada
    # En firebase-admin >= 7.0, el parámetro se llama 'database_id' no 'database'
    try:
        # Intentar primero con la API nueva (firebase-admin >= 7.0)
        db_client = firestore.client()

        # Obtener el project_id desde las credenciales
        app = firebase_admin.get_app()
        project_id = app.project_id

        # Construir el string de la base de datos en el formato correcto
        database_string = f"projects/{project_id}/databases/{database_name}"

        # Usar el atributo interno para especificar la base de datos
        db_client._database_string_internal = database_string

        print(f"✅ Conectado a: {database_string}")
        return db_client

    except Exception as e:
        print(f"❌ ERROR al conectar a la base de datos: {e}")
        print(f"❌ Verifica que la base de datos '{database_name}' existe en Firebase Console")
        raise

# Cliente de Firestore global
db = initialize_firebase()

