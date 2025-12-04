# 🚀 Guía de Inicio Rápido

## Configuración Inicial (Solo la primera vez)

### 1. Configurar Firebase

1. Ve a https://console.firebase.google.com/
2. Crea un nuevo proyecto o usa uno existente
3. En el menú lateral, haz clic en el ícono de configuración ⚙️ > "Configuración del proyecto"
4. Ve a la pestaña "Cuentas de servicio"
5. Haz clic en "Generar nueva clave privada"
6. Guarda el archivo JSON en la carpeta raíz del proyecto

### 2. Configurar Variables de Entorno

1. Copia el archivo de ejemplo:
   ```bash
   # Windows (PowerShell)
   copy .env .env
   
   # Linux/Mac
   cp .env .env
   ```

2. Edita el archivo `.env` y actualiza:
   ```
   FIREBASE_CREDENTIALS_PATH=nombre-de-tu-archivo-firebase.json
   FLASK_SECRET_KEY=genera-una-clave-secreta-aleatoria
   FLASK_ENV=development
   ```

### 3. Instalar Dependencias

#### Opción A: Usando el script de inicio (Recomendado)
```bash
# Windows
start.bat

# Linux/Mac
chmod +x start.sh
./start.sh
```

#### Opción B: Manual
```bash
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno virtual
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
python main.py
```

## Uso Diario

### Iniciar la Aplicación

**Opción 1 - Script automático:**
```bash
# Windows
start.bat

# Linux/Mac
./start.sh
```

**Opción 2 - Manual:**
```bash
# 1. Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 2. Ejecutar
python main.py
```

### Acceder a la Aplicación

Una vez iniciada, abre tu navegador en:
```
http://localhost:5000
```

### Detener la Aplicación

Presiona `Ctrl + C` en la terminal donde está corriendo el servidor.

## Estructura de la Aplicación

```
Dashboard (/)           → Vista general de tus finanzas
Cuentas (/accounts)     → Gestionar cuentas de ahorro
Tarjetas (/cards)       → Gestionar tarjetas de crédito
Efectivo (/cash)        → Registrar efectivo en mano
Metas (/goals)          → Definir y seguir metas de ahorro
```

## Funcionalidades Principales

### 📊 Dashboard
- Muestra tu patrimonio neto (activos - deudas)
- Total de activos (ahorros + efectivo)
- Deuda total en tarjetas
- Crédito disponible
- Progreso de metas de ahorro

### 💰 Cuentas de Ahorro
- Agregar múltiples cuentas
- Especificar banco y moneda
- Ver balance total consolidado

### 💳 Tarjetas de Crédito
- Registrar límite de crédito
- Saldo actual usado
- Día de corte
- Indicador visual de uso (%)

### 💵 Efectivo
- Registrar efectivo en diferentes ubicaciones
- Múltiples monedas
- Total consolidado

### 🎯 Metas de Ahorro
- Definir objetivo y monto
- Fecha límite opcional
- Barra de progreso visual
- Marcado automático de metas completadas

## Solución de Problemas

### Error: "No se encontraron credenciales de Firebase"
- Asegúrate de haber descargado el archivo JSON de Firebase
- Verifica que la ruta en `.env` sea correcta
- El archivo debe estar en la raíz del proyecto

### Error: "ModuleNotFoundError"
- Activa el entorno virtual
- Ejecuta: `pip install -r requirements.txt`

### La aplicación no carga datos
- Verifica tu conexión a internet
- Revisa la consola del navegador (F12) para errores
- Verifica que Firebase esté configurado correctamente

### Puerto 5000 ya en uso
- Detén otras aplicaciones en el puerto 5000
- O edita `main.py` para usar otro puerto:
  ```python
  app.run(debug=True, host='0.0.0.0', port=8000)
  ```

## Consejos de Uso

### 📱 Acceso desde Móvil
Si quieres acceder desde tu teléfono en la misma red:

1. Encuentra tu IP local:
   ```bash
   # Windows
   ipconfig
   # Linux/Mac
   ifconfig
   ```

2. En tu móvil, abre:
   ```
   http://TU_IP_LOCAL:5000
   ```

### 💾 Respaldo de Datos
Tus datos están en Firebase Firestore. Para hacer respaldo:
- Ve a Firebase Console > Firestore Database
- Puedes exportar o hacer respaldo desde ahí

### 🗄️ Bases de Datos Nombradas (OBLIGATORIO)

**⚠️ Esta aplicación REQUIERE que especifiques un nombre de base de datos.**

La aplicación NO puede usar la base de datos por defecto "(default)". Debes:

1. Crear una base de datos con nombre en Firebase Console
2. Especificar su nombre en `.env`:
   ```
   FIREBASE_DATABASE_NAME=finances
   ```

**Ventajas de usar bases de datos nombradas:**
- Separar entornos (desarrollo/producción)
- Múltiples usuarios con datos independientes
- Mejor organización y control

**Ejemplos:**
```bash
# Para desarrollo
FIREBASE_DATABASE_NAME=desarrollo

# Para producción
FIREBASE_DATABASE_NAME=produccion

# Para un usuario específico
FIREBASE_DATABASE_NAME=usuario-juan
```

Si no especificas este valor, la aplicación mostrará un error y no se iniciará.

### 🔒 Seguridad
**IMPORTANTE**: Esta aplicación NO tiene autenticación. 
- Solo úsala en tu red local
- NO la expongas a internet sin agregar seguridad
- NO compartas tus credenciales de Firebase

## Comandos Útiles

```bash
# Ver logs detallados
python main.py

# Instalar nueva dependencia
pip install nombre-paquete
pip freeze > requirements.txt

# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Limpiar caché de Python
# Windows
del /S *.pyc
# Linux/Mac
find . -name "*.pyc" -delete
```

## Próximas Mejoras Sugeridas

- [ ] Exportar reportes a PDF/Excel
- [ ] Gráficas interactivas con Chart.js
- [ ] Historial de transacciones
- [ ] Categorización de gastos
- [ ] Múltiples usuarios con autenticación
- [ ] Modo oscuro
- [ ] Notificaciones de metas cumplidas
- [ ] Conversión automática de monedas

---

¿Necesitas ayuda? Revisa el README.md completo o abre un issue en el repositorio.

