# 🔥 Configuración de Firebase

## ⚠️ Requisitos de Versión

Para usar bases de datos nombradas, necesitas:
- **firebase-admin >= 6.5.0** (Recomendado: 7.1.0 o superior)

Si tienes una versión antigua, actualiza con:
```bash
pip install --upgrade firebase-admin
```

## Configuración de Bases de Datos

### Base de Datos por Defecto

Si no especificas ningún nombre de base de datos en `.env`, la aplicación usará la base de datos por defecto de Firestore llamada `(default)`.

### Bases de Datos Nombradas

Firebase Firestore permite crear múltiples bases de datos en un mismo proyecto. Esto es útil para:

- **Separar entornos**: Desarrollo, Pruebas, Producción
- **Múltiples usuarios**: Cada usuario puede tener su propia base de datos
- **Organización**: Separar datos por propósito o categoría

### Cómo Crear una Nueva Base de Datos

1. Ve a [Firebase Console](https://console.firebase.google.com/)
2. Selecciona tu proyecto
3. En el menú lateral, haz clic en **Firestore Database**
4. Haz clic en el ícono de 3 puntos (⋮) junto al nombre de la base de datos actual
5. Selecciona **"Crear base de datos"**
6. Asigna un nombre (por ejemplo: `produccion`, `desarrollo`, `testing`)
7. Selecciona la ubicación y modo de inicio
8. Haz clic en **Crear**

### Configurar la Aplicación

Una vez creada tu base de datos, configúrala en el archivo `.env`:

```bash
# Ejemplo para producción
FIREBASE_DATABASE_NAME=produccion

# Ejemplo para desarrollo
FIREBASE_DATABASE_NAME=desarrollo

# Ejemplo para testing
FIREBASE_DATABASE_NAME=testing
```

**Importante**: Si comentas o eliminas esta línea, se usará la base de datos `(default)`.

## Ejemplos de Uso

### Caso 1: Desarrollo y Producción Separados

**Archivo `.env.development`:**
```bash
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json
FIREBASE_DATABASE_NAME=desarrollo
FLASK_SECRET_KEY=dev-secret-key
FLASK_ENV=development
```

**Archivo `.env.production`:**
```bash
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json
FIREBASE_DATABASE_NAME=produccion
FLASK_SECRET_KEY=prod-secret-key-super-segura
FLASK_ENV=production
```

Luego ejecuta:
```bash
# Para desarrollo
cp .env.development .env
python main.py

# Para producción
cp .env.production .env
python main.py
```

### Caso 2: Múltiples Usuarios

Si quieres que diferentes personas usen la misma aplicación pero con datos separados:

**Usuario 1:**
```bash
FIREBASE_DATABASE_NAME=usuario-juan
```

**Usuario 2:**
```bash
FIREBASE_DATABASE_NAME=usuario-maria
```

### Caso 3: Base de Datos por Defecto

Si solo necesitas una base de datos:

```bash
# Dejar comentado o no incluir la línea
# FIREBASE_DATABASE_NAME=
```

## Verificación

Cuando inicies la aplicación, verás en la consola qué base de datos se está usando:

```
🚀 Iniciando aplicación de Finanzas Personales...
📦 Usando base de datos: mi-base-datos
📊 Dashboard disponible en: http://localhost:5000
```

Si no ves el mensaje "📦 Usando base de datos:", significa que estás usando la base de datos por defecto.

## Migración de Datos

Si necesitas migrar datos entre bases de datos:

### Opción 1: Exportar/Importar desde Firebase Console

1. Ve a Firestore Database
2. Selecciona la pestaña **"Exportar/Importar"**
3. Exporta desde la base de datos origen
4. Cambia a la base de datos destino
5. Importa los datos exportados

### Opción 2: Script de Python

Puedes crear un script para copiar datos:

```python
import os
from firebase_admin import credentials, firestore, initialize_app

# Inicializar con la base de datos origen
cred = credentials.Certificate("firebase-credentials.json")
app = initialize_app(cred)

db_origen = firestore.client(database="desarrollo")
db_destino = firestore.client(database="produccion")

# Copiar colecciones
colecciones = ['savings_accounts', 'credit_cards', 'cash', 'savings_goals']

for coleccion in colecciones:
    docs = db_origen.collection(coleccion).stream()
    for doc in docs:
        db_destino.collection(coleccion).document(doc.id).set(doc.to_dict())
    print(f"✅ {coleccion} copiada")

print("✅ Migración completada")
```

## Reglas de Seguridad

**IMPORTANTE**: Cada base de datos tiene sus propias reglas de seguridad.

Configura las reglas en Firebase Console:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Permitir todo (solo para desarrollo local)
    match /{document=**} {
      allow read, write: if true;
    }
    
    // Para producción, agregar autenticación:
    // match /{document=**} {
    //   allow read, write: if request.auth != null;
    // }
  }
}
```

## Límites y Consideraciones

### Límites de Firestore
- **Lecturas/Escrituras**: 50,000 por día (plan gratuito)
- **Bases de datos**: Hasta 100 bases de datos por proyecto
- **Almacenamiento**: 1 GB (plan gratuito)

### Mejores Prácticas
1. **Nombres descriptivos**: Usa nombres claros como `produccion`, `desarrollo`
2. **Documentación**: Mantén un registro de qué base de datos usa cada entorno
3. **Seguridad**: Nunca uses la misma base de datos para desarrollo y producción
4. **Backups**: Exporta datos regularmente desde Firebase Console

## Solución de Problemas

### Error: "Database not found"
- Verifica que el nombre en `.env` coincida exactamente con el nombre en Firebase
- Los nombres son sensibles a mayúsculas/minúsculas
- Asegúrate de que la base de datos existe en Firebase Console

### Error: "Permission denied"
- Revisa las reglas de seguridad de la base de datos específica
- Cada base de datos tiene sus propias reglas

### No se muestra qué base de datos se está usando
- Verifica que `FIREBASE_DATABASE_NAME` esté en tu archivo `.env`
- Asegúrate de que no tenga espacios extra
- Reinicia la aplicación después de modificar `.env`

## Comandos Útiles

```bash
# Ver qué base de datos estás usando
cat .env | grep FIREBASE_DATABASE_NAME  # Linux/Mac
type .env | findstr FIREBASE_DATABASE_NAME  # Windows

# Cambiar rápidamente de base de datos
# Linux/Mac
export FIREBASE_DATABASE_NAME=desarrollo
python main.py

# Windows (PowerShell)
$env:FIREBASE_DATABASE_NAME="desarrollo"
python main.py
```

---

**Nota**: La funcionalidad de múltiples bases de datos está disponible en Firebase Firestore desde 2023. Si tu proyecto es anterior, es posible que necesites actualizarlo.

