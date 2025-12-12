# 🎯 Pasos para Ejecutar la Aplicación

## ✅ Lista de Verificación Pre-Ejecución

Antes de ejecutar la aplicación por primera vez, asegúrate de tener:

- [ ] Python 3.8 o superior instalado
- [ ] Cuenta de Firebase creada
- [ ] Archivo de credenciales Firebase descargado
- [ ] Archivo `.env` configurado

---

## 🔥 Paso 1: Configurar Firebase

### 1.1 Crear Proyecto en Firebase

1. Ve a https://console.firebase.google.com/
2. Haz clic en "Agregar proyecto"
3. Nombre del proyecto: `finanzas-personales` (o el que prefieras)
4. Desactiva Google Analytics (opcional para este proyecto)
5. Haz clic en "Crear proyecto"

### 1.2 Activar Firestore

1. En el menú lateral, haz clic en "Firestore Database"
2. Haz clic en "Crear base de datos"
3. Selecciona "Iniciar en modo de producción" o "Modo de prueba"
4. Selecciona la ubicación más cercana (ej: `southamerica-east1`)
5. Haz clic en "Habilitar"

### 1.3 Descargar Credenciales

1. Haz clic en el ícono de configuración ⚙️ (arriba a la izquierda)
2. Selecciona "Configuración del proyecto"
3. Ve a la pestaña "Cuentas de servicio"
4. Haz clic en "Generar nueva clave privada"
5. Confirma haciendo clic en "Generar clave"
6. Se descargará un archivo JSON
7. **IMPORTANTE**: Mueve este archivo a la carpeta raíz del proyecto
8. Renómbralo a algo simple como `firebase-credentials.json`

---

## 📝 Paso 2: Configurar Variables de Entorno

### 2.1 Crear archivo .env

```bash
# En Windows (PowerShell)
copy .env.example .env

# En Linux/Mac
cp .env.example .env
```

### 2.2 Editar archivo .env

Abre el archivo `.env` con tu editor favorito y configura:

```env
# Nombre del archivo JSON que descargaste
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json

# Genera una clave secreta aleatoria (puedes usar cualquier texto largo)
FLASK_SECRET_KEY=mi-clave-super-secreta-12345

# Modo de desarrollo
FLASK_ENV=development

# ⚠️ OBLIGATORIO: Nombre de tu base de datos de Firestore
# NO puedes omitir esto - la aplicación lo requiere
FIREBASE_DATABASE_NAME=finances
```

**💡 Tip**: Para generar una clave secreta aleatoria en Python:
```python
import secrets
print(secrets.token_hex(32))
```

**⚠️ IMPORTANTE sobre la base de datos**: 
- `FIREBASE_DATABASE_NAME` es **OBLIGATORIO**
- La aplicación **NO** funcionará sin este valor
- **NO** se puede usar la base de datos por defecto
- Debes crear una base de datos con nombre en Firebase Console
- Más información en `FIREBASE_CONFIG.md`

---

## 🐍 Paso 3: Preparar Entorno Python

### 3.1 Verificar versión de Python

```bash
python --version
# Debe ser 3.8 o superior
```

Si no tienes Python instalado, descárgalo desde: https://www.python.org/downloads/

### 3.2 Crear entorno virtual

```bash
python -m venv .venv
```

### 3.3 Activar entorno virtual

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

Deber��as ver `(.venv)` al inicio de tu línea de comando.

### 3.4 Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:
- Flask (framework web)
- Firebase Admin SDK
- python-dotenv
- gunicorn

---

## 🚀 Paso 4: Ejecutar la Aplicación

### Opción A: Usando el script automático (Recomendado)

**Windows:**
```bash
start.bat
```

**Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

### Opción B: Manualmente

```bash
# Asegúrate de que el entorno virtual esté activado
python main.py
```

---

## 🌐 Paso 5: Acceder a la Aplicación

1. Abre tu navegador web
2. Ve a: http://localhost:8000
3. Deberías ver el Dashboard de Finanzas

---

## ✨ Paso 6: Probar la Aplicación

### Agregar tu primera cuenta de ahorro

1. Ve a "Cuentas" en el menú
2. Haz clic en "Agregar Cuenta"
3. Completa el formulario:
   - Nombre: "Cuenta de ahorros principal"
   - Banco: "BBVA"
   - Balance: 10000
   - Moneda: MXN
4. Haz clic en "Guardar"

### Agregar una tarjeta de crédito

1. Ve a "Tarjetas" en el menú
2. Haz clic en "Agregar Tarjeta"
3. Completa el formulario:
   - Nombre: "Tarjeta Platinum"
   - Banco: "Citibanamex"
   - Límite: 50000
   - Saldo usado: 15000
   - Día de corte: 15
4. Haz clic en "Guardar"

### Agregar efectivo

1. Ve a "Efectivo" en el menú
2. Haz clic en "Agregar Efectivo"
3. Completa el formulario:
   - Descripción: "Cartera"
   - Cantidad: 500
   - Ubicación: "Personal"
4. Haz clic en "Guardar"

### Crear una meta de ahorro

1. Ve a "Metas" en el menú
2. Haz clic en "Agregar Meta"
3. Completa el formulario:
   - Nombre: "Vacaciones 2025"
   - Monto objetivo: 30000
   - Monto actual: 8000
   - Fecha: 2025-12-15
4. Haz clic en "Guardar"

### Verificar el Dashboard

1. Ve al "Dashboard" en el menú
2. Deberías ver:
   - Patrimonio Neto calculado
   - Total de activos
   - Deuda en tarjetas
   - Progreso de tu meta

---

## 🎉 ¡Listo!

Tu aplicación está funcionando correctamente. Ahora puedes:

- ✅ Agregar más cuentas, tarjetas, efectivo y metas
- ✅ Editar y actualizar tus datos
- ✅ Ver tu situación financiera en tiempo real
- ✅ Acceder desde tu móvil en la misma red

---

## 🛑 Detener la Aplicación

Para detener el servidor:
1. Ve a la terminal donde está corriendo
2. Presiona `Ctrl + C`

---

## 🔄 Volver a Ejecutar

La próxima vez que quieras usar la aplicación:

```bash
# Windows
start.bat

# Linux/Mac
./start.sh
```

O manualmente:
```bash
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
python main.py
```

---

## ❓ Problemas Comunes

### Error: "No module named 'flask'"
**Solución**: 
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

### Error: "No se encontraron credenciales de Firebase"
**Solución**: 
1. Verifica que el archivo JSON esté en la raíz del proyecto
2. Verifica que `.env` tenga la ruta correcta
3. El nombre en `.env` debe coincidir con el archivo

### Error: "Address already in use" (Puerto ocupado)
**Solución**:
Edita `main.py` y cambia el puerto:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```
Luego accede a: http://localhost:8000

### La página no carga o muestra errores
**Solución**:
1. Verifica la consola donde está corriendo el servidor
2. Abre las herramientas de desarrollo del navegador (F12)
3. Revisa la pestaña "Console" para ver errores JavaScript
4. Verifica tu conexión a internet (necesaria para Firestore)

---

## 📱 Acceder desde tu Móvil

1. Asegúrate de que tu móvil y PC estén en la misma red WiFi
2. Encuentra la IP de tu computadora:
   ```bash
   # Windows
   ipconfig
   
   # Linux/Mac
   ifconfig
   ```
3. Busca la IP local (ejemplo: 192.168.1.100)
4. En tu móvil, abre el navegador y ve a:
   ```
   http://TU_IP:8000
   ```

---

## 💾 Respaldo de Datos

Tus datos están en Firebase Firestore y se guardan automáticamente en la nube.

Para hacer respaldo manual:
1. Ve a Firebase Console
2. Firestore Database
3. Puedes exportar las colecciones

---

## 🎓 Próximos Pasos

Ahora que tu aplicación funciona, puedes:

1. **Personalizar**: Modifica los colores, textos, etc.
2. **Extender**: Agrega nuevas funcionalidades
3. **Mejorar**: Implementa las sugerencias del RESUMEN.md
4. **Compartir**: Sube tu proyecto a GitHub

---

**¿Necesitas ayuda?** Revisa:
- `README.md` - Documentación completa
- `QUICKSTART.md` - Guía rápida
- `RESUMEN.md` - Resumen del proyecto

¡Disfruta gestionando tus finanzas! 💰📊

