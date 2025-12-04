# 💰 Dashboard de Finanzas Personales

Aplicación web para gestionar tu balance financiero centralizado: cuentas de ahorro, tarjetas de crédito, efectivo y metas de ahorro.

## ✨ Características

- 💰 **Gestión de cuentas de ahorro**: Administra múltiples cuentas bancarias
- 💳 **Control de tarjetas de crédito**: Monitorea límites, saldos y uso de crédito
- 💵 **Registro de efectivo**: Controla el efectivo en diferentes ubicaciones
- 🎯 **Metas de ahorro**: Define y da seguimiento a tus objetivos financieros
- 📊 **Dashboard centralizado**: Visualiza tu patrimonio neto, activos y pasivos
- 📱 **Diseño responsive**: Optimizado para móvil y escritorio
- 🔥 **Sin autenticación**: Acceso directo y rápido (ideal para uso personal)

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- Cuenta de Firebase (gratuita)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd finances
   ```

2. **Crear y activar entorno virtual**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Firebase**
   - Ir a [Firebase Console](https://console.firebase.google.com/)
   - Crear un nuevo proyecto
   - Ir a Configuración del proyecto > Cuentas de servicio
   - Generar nueva clave privada (archivo JSON)
   - Guardar el archivo en la raíz del proyecto

5. **Configurar variables de entorno**
   ```bash
   # Copiar el archivo de ejemplo
   copy .env .env  # Windows
   cp .env .env    # Linux/Mac
   ```
   
   Editar `.env` y configurar:
   ```
   FIREBASE_CREDENTIALS_PATH=ruta/al/archivo-firebase.json
   FLASK_SECRET_KEY=tu-clave-secreta-aqui
   FLASK_ENV=development
   
   # ⚠️ OBLIGATORIO: Debes especificar el nombre de tu base de datos
   # NO se puede omitir - la aplicación requiere una base de datos nombrada
   FIREBASE_DATABASE_NAME=finances
   ```

6. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

7. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## 📂 Estructura del Proyecto

```
finances/
├── app/
│   ├── __init__.py          # Inicialización de Flask
│   ├── routes.py            # Rutas y API endpoints
│   ├── models.py            # Modelos de datos
│   └── firebase_config.py   # Configuración de Firestore
├── templates/
│   ├── base.html            # Plantilla base
│   ├── dashboard.html       # Dashboard principal
│   ├── accounts.html        # Cuentas de ahorro
│   ├── cards.html           # Tarjetas de crédito
│   ├── cash.html            # Efectivo
│   └── goals.html           # Metas de ahorro
├── main.py                  # Punto de entrada
├── requirements.txt         # Dependencias Python
├── .env.example             # Ejemplo de variables de entorno
└── README.md                # Este archivo
```

## 🛠️ Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: HTML5, JavaScript (Vanilla), Tailwind CSS
- **Base de datos**: Google Cloud Firestore
- **Íconos**: Font Awesome
- **Hosting**: Puede desplegarse en Heroku, Render, Google Cloud, etc.

## 📊 Funcionalidades por Módulo

### Dashboard
- Resumen de patrimonio neto
- Total de activos (ahorros + efectivo)
- Total de deuda en tarjetas
- Crédito disponible
- Progreso de metas de ahorro
- Lista de cuentas y tarjetas

### Cuentas de Ahorro
- Agregar, editar y eliminar cuentas
- Especificar banco y moneda
- Ver balance total

### Tarjetas de Crédito
- Gestionar múltiples tarjetas
- Límite de crédito y saldo actual
- Día de corte
- Indicador visual de uso de crédito

### Efectivo
- Registrar efectivo en diferentes ubicaciones
- Múltiples monedas
- Total consolidado

### Metas de Ahorro
- Definir objetivos financieros
- Seguimiento de progreso (%)
- Fecha objetivo
- Metas completadas destacadas

## 🔧 API Endpoints

### Cuentas de Ahorro
- `GET /api/accounts` - Listar todas las cuentas
- `POST /api/accounts` - Crear nueva cuenta
- `PUT /api/accounts/<id>` - Actualizar cuenta
- `DELETE /api/accounts/<id>` - Eliminar cuenta

### Tarjetas de Crédito
- `GET /api/cards` - Listar todas las tarjetas
- `POST /api/cards` - Crear nueva tarjeta
- `PUT /api/cards/<id>` - Actualizar tarjeta
- `DELETE /api/cards/<id>` - Eliminar tarjeta

### Efectivo
- `GET /api/cash` - Listar registros de efectivo
- `POST /api/cash` - Crear nuevo registro
- `PUT /api/cash/<id>` - Actualizar registro
- `DELETE /api/cash/<id>` - Eliminar registro

### Metas de Ahorro
- `GET /api/goals` - Listar todas las metas
- `POST /api/goals` - Crear nueva meta
- `PUT /api/goals/<id>` - Actualizar meta
- `DELETE /api/goals/<id>` - Eliminar meta

### Resumen
- `GET /api/summary` - Obtener resumen financiero completo

## 🔐 Seguridad

**Nota**: Esta aplicación está diseñada para uso personal local sin autenticación. Si deseas desplegarla públicamente, considera:

- Implementar autenticación (Firebase Auth, JWT, etc.)
- Agregar validación de usuarios
- Configurar reglas de seguridad en Firestore
- Usar HTTPS
- Implementar rate limiting

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue.

---

Hecho con ❤️ para ayudarte a gestionar tus finanzas personales

