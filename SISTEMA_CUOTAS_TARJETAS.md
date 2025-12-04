# Sistema de Cuotas para Tarjetas de Crédito

## 📋 Descripción

Sistema completo implementado para gestionar **compras en cuotas/meses sin intereses** en tarjetas de crédito, permitiendo:

- ✅ Registrar solo compras en cuotas (MSI)
- ✅ Calcular automáticamente el pago mensual
- ✅ Seguimiento de cuotas pagadas y pendientes
- ✅ Marcar cuotas como pagadas cada mes
- ✅ Vista detallada por tarjeta

## 🎯 Problema Resuelto

**Antes:** No se podía calcular el pago mensual de las tarjetas considerando las cuotas activas.

**Ahora:** El sistema calcula automáticamente cuánto debes pagar cada mes sumando todas las cuotas pendientes de tus compras en meses sin intereses.

---

## 📁 Archivos Modificados/Creados

### 1. **app/models.py** ✅
- **Agregado:** Clase `CardInstallment`
- **Función:** Gestionar compras en cuotas de tarjetas de crédito

**Métodos implementados:**
- `get_all_by_card(card_id)` - Obtiene todas las compras en cuotas de una tarjeta
- `get_by_id(installment_id)` - Obtiene una compra específica
- `create(data)` - Registra una nueva compra en cuotas
- `update(installment_id, data)` - Actualiza una compra (ej: marcar cuota como pagada)
- `delete(installment_id)` - Elimina una compra
- `get_monthly_payment_for_card(card_id)` - **Calcula el pago mensual total**

**Estructura de datos:**
```python
{
    'card_id': 'id_de_la_tarjeta',
    'description': 'Laptop Dell',
    'total_amount': 15000.00,
    'total_months': 12,
    'paid_months': 3,
    'purchase_date': datetime,
    'monthly_payment': 1250.00,      # Calculado automáticamente
    'remaining_months': 9             # Calculado automáticamente
}
```

---

### 2. **app/routes.py** ✅
- **Agregado:** Import de `CardInstallment`
- **Agregadas:** 6 nuevas rutas API + 1 ruta de vista

**Rutas API implementadas:**

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/cards/<card_id>/installments` | Listar compras en cuotas |
| POST | `/api/cards/<card_id>/installments` | Crear compra en cuotas |
| PUT | `/api/cards/<card_id>/installments/<id>` | Actualizar compra |
| DELETE | `/api/cards/<card_id>/installments/<id>` | Eliminar compra |
| GET | `/api/cards/<card_id>/monthly-payment` | Calcular pago mensual |

**Ruta de vista:**
- GET `/cards/<card_id>` - Página de detalle de tarjeta

---

### 3. **templates/card_detail.html** ✅ NUEVO
Nueva página completa para gestionar cuotas de una tarjeta.

**Características:**
- 📊 **Header con información de la tarjeta:** Saldo, límite, disponible
- 💰 **Cálculo de pago mensual:** Muestra el total a pagar considerando todas las cuotas activas
- 📝 **Lista de compras en cuotas:** Con progreso visual
- ➕ **Modal para agregar compras:** Descripción, monto, meses
- ✏️ **Editar compras existentes**
- ✅ **Marcar cuota como pagada:** Botón rápido para cada compra activa
- 🗑️ **Eliminar compras**

**Secciones principales:**
1. Botón "Volver a Tarjetas"
2. Header morado con datos de la tarjeta
3. Card destacado con pago mensual total
4. Lista de compras en cuotas (activas y completadas)
5. Modal para agregar/editar compras

---

### 4. **templates/cards.html** ✅
- **Modificado:** Agregado botón "Ver Detalle" (ícono de ojo)

**Botones por tarjeta:**
- 👁️ Verde: Ver Detalle (nuevo)
- ✏️ Azul: Editar
- 🗑️ Rojo: Eliminar

---

## 🚀 Cómo Usar el Sistema

### Paso 1: Acceder a la página de tarjetas
```
http://localhost:5000/cards
```

### Paso 2: Hacer clic en el botón "Ver Detalle" (ícono de ojo verde)
Esto te llevará a la página de detalle de la tarjeta seleccionada.

### Paso 3: Agregar una compra en cuotas
1. Clic en "Agregar Compra en Cuotas"
2. Llenar el formulario:
   - **Descripción:** Ej: "Laptop Dell XPS"
   - **Monto total:** Ej: 15,000.00
   - **Número de cuotas:** Seleccionar (3, 6, 9, 12, 18, 24 MSI)
   - **Cuotas ya pagadas:** 0 (si es nueva)
   - **Fecha de compra:** Seleccionar fecha
3. Guardar

### Paso 4: Ver el pago mensual calculado
El sistema automáticamente calcula y muestra:
- **Pago mensual total:** Suma de todas las cuotas activas
- **Cuotas por compra:** Monto mensual por cada compra

### Paso 5: Marcar cuotas como pagadas
Cada mes:
1. Ir al detalle de la tarjeta
2. En cada compra activa, clic en "Marcar cuota como pagada"
3. El sistema actualiza automáticamente el pago mensual

---

## 💡 Ejemplo Práctico

### Escenario:
Tienes una tarjeta con estas compras en MSI:

1. **Laptop:** $12,000 en 12 MSI → $1,000/mes (quedan 8 cuotas)
2. **Refrigerador:** $9,000 en 6 MSI → $1,500/mes (quedan 4 cuotas)
3. **Celular:** $6,000 en 3 MSI → $2,000/mes (completada)

### Resultado en el sistema:
```
PAGO MENSUAL POR CUOTAS
Total a pagar este mes: $2,500.00
```

**Desglose:**
- Laptop: $1,000/mes ✅
- Refrigerador: $1,500/mes ✅
- Celular: $0/mes (ya pagada) ⚪

---

## 📊 Base de Datos (Firebase)

### Nueva Colección: `card_installments`

**Campos:**
```javascript
{
  "card_id": "abc123",              // ID de la tarjeta
  "description": "Laptop Dell",     // Descripción
  "total_amount": 15000.00,         // Monto total
  "total_months": 12,               // Total de meses
  "paid_months": 3,                 // Cuotas pagadas
  "purchase_date": Timestamp,       // Fecha de compra
  "created_at": Timestamp,          // Fecha de registro
  "updated_at": Timestamp           // Última actualización
}
```

**Índices requeridos en Firebase:**
- `card_id` + `purchase_date` (para ordenar por fecha)

---

## 🎨 Interfaz de Usuario

### Página de Detalle de Tarjeta

#### Header (Morado)
```
┌─────────────────────────────────────────┐
│  Tarjeta Citibanamex              Editar│
│  Banamex                                 │
│                                          │
│  Saldo Actual    Límite      Disponible │
│  $5,000.00      $20,000.00   $15,000.00 │
└─────────────────────────────────────────┘
```

#### Pago Mensual (Card Blanco)
```
┌─────────────────────────────────────────┐
│ 🧮 Pago Mensual por Cuotas              │
│ Calculado en base a MSI                 │
│                                          │
│              Total a pagar este mes     │
│                   $2,500.00             │
└─────────────────────────────────────────┘
```

#### Compras en Cuotas
```
┌─────────────────────────────────────────┐
│ 💳 Compras en Cuotas / MSI     + Agregar│
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ Laptop Dell                    ✏️ 🗑️ │ │
│ │ 15/10/2024                           │ │
│ │                                      │ │
│ │ Monto Total  Pago Mensual  Restantes│ │
│ │ $12,000.00   $1,000.00      8 de 12 │ │
│ │                                      │ │
│ │ ████████░░░░ 66%                    │ │
│ │                                      │ │
│ │ ✅ Marcar cuota como pagada          │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

---

## ✅ Características Implementadas

- [x] Modelo de datos `CardInstallment`
- [x] Rutas API completas (CRUD)
- [x] Cálculo automático de pago mensual
- [x] Página de detalle de tarjeta
- [x] Modal para agregar/editar compras
- [x] Botón "Marcar cuota como pagada"
- [x] Progreso visual con barras
- [x] Diferenciación visual (activas vs completadas)
- [x] Botón "Ver Detalle" en cards.html
- [x] Validaciones de formularios
- [x] Notificaciones toast
- [x] Responsive design

---

## 🔄 Flujo de Trabajo Mensual

1. **Inicio de mes:**
   - Revisar pago mensual calculado
   - Pagar el monto mostrado

2. **Después del pago:**
   - Entrar al detalle de la tarjeta
   - Marcar las cuotas como pagadas
   - Ver actualización automática del próximo mes

3. **Nueva compra en MSI:**
   - Agregar en el sistema
   - Ver el nuevo pago mensual

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python + Flask
- **Base de datos:** Firebase Firestore
- **Frontend:** HTML5 + Tailwind CSS + JavaScript
- **Iconos:** Font Awesome

---

## 📝 Notas Importantes

1. **Solo registrar MSI:** Este sistema es solo para compras en meses sin intereses. Las compras de contado ya están en el saldo de la tarjeta.

2. **Actualizar mensualmente:** Es importante marcar las cuotas pagadas cada mes para mantener el cálculo preciso.

3. **Múltiples tarjetas:** Cada tarjeta tiene su propio conjunto de compras en cuotas.

4. **Fecha de compra:** Ayuda a recordar cuándo se hizo la compra y estimar cuándo termina.

---

## 🎯 Próximas Mejoras Posibles

- [ ] Notificaciones de próximo pago
- [ ] Gráficas de proyección de pagos
- [ ] Exportar a PDF/Excel
- [ ] Recordatorios automáticos
- [ ] Categorías de compras
- [ ] Historial de pagos

---

## 🚀 ¡Listo para Usar!

El sistema está completamente implementado y funcional. Solo necesitas:

1. Iniciar la aplicación: `python main.py`
2. Ir a: `http://localhost:5000/cards`
3. Hacer clic en "Ver Detalle" en cualquier tarjeta
4. Comenzar a agregar tus compras en cuotas

---

**Fecha de implementación:** 3 de Diciembre de 2025  
**Versión:** 1.0.0  
**Estado:** ✅ Completado y funcional

