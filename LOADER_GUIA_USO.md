# ✅ LOADER GLOBAL - GUÍA DE USO Y PRUEBA

## 🎯 ¿Qué es el Loader?

Un **indicador visual** que se muestra automáticamente cuando la aplicación está esperando respuestas del servidor. Mejora la experiencia del usuario mostrando que algo está cargando.

---

## 📸 Aspecto Visual

Cuando se hace una petición, aparece:

```
╔═══════════════════════════════════════╗
║  [Fondo oscuro semi-transparente]     ║
║                                        ║
║         ┌────────────────┐            ║
║         │                │            ║
║         │   🔄 Spinner   │            ║
║         │                │            ║
║         │  Cargando...   │            ║
║         └────────────────┘            ║
║                                        ║
╚═══════════════════════════════════════╝
```

**Características:**
- Fondo oscuro con blur
- Spinner azul giratorio  
- Texto "Cargando..."
- Se centra en la pantalla
- Aparece sobre todo el contenido

---

## 🧪 CÓMO PROBAR EL LOADER

### Prueba 1: Balance Mensual

1. Ve a `http://localhost:5000/budget`
2. **Observa:** El loader debe aparecer al cargar la página
3. Configura un salario (ej: 15000)
4. Clic en "Guardar Configuración"
5. **Observa:** El loader aparece brevemente mientras guarda
6. Agrega un gasto fijo (Renta - 5000)
7. **Observa:** El loader aparece al guardar

### Prueba 2: Detalle de Tarjeta

1. Ve a `http://localhost:5000/cards`
2. Clic en el ícono del ojo 👁️ de una tarjeta
3. **Observa:** El loader aparece al cargar el detalle

### Prueba 3: Eliminando Gasto

1. En Balance Mensual con gastos fijos
2. Elimina un gasto (ícono de basura)
3. Confirma
4. **Observa:** Loader aparece durante la eliminación

---

## 🎨 Estados del Loader

### ✅ Estado 1: Oculto (normal)
- El usuario interactúa normalmente
- No se ve el loader

### ⏳ Estado 2: Mostrando (cargando)
- Aparece overlay oscuro
- Spinner girando
- Texto "Cargando..."
- Usuario NO puede interactuar con la página

### ✅ Estado 3: Oculto (completado)
- Loader desaparece automáticamente
- Usuario puede interactuar de nuevo
- Toast de confirmación aparece

---

## 💻 IMPLEMENTACIÓN TÉCNICA

### Estructura HTML (en base.html)

```html
<div id="global-loader" class="fixed inset-0 bg-black bg-opacity-50 hidden items-center justify-center z-50">
    <div class="bg-white rounded-lg shadow-2xl p-8 flex flex-col items-center">
        <div class="loader-spinner mb-4"></div>
        <p class="text-gray-700 font-medium">Cargando...</p>
    </div>
</div>
```

### Funciones JavaScript (en base.html)

```javascript
// Mostrar loader manualmente (raro)
showLoader();

// Ocultar loader manualmente (raro)
hideLoader();

// Usar con fetch (RECOMENDADO)
const response = await fetchWithLoader('/api/endpoint', options);
```

---

## 📝 MÓDULOS ACTUALIZADOS

### ✅ Budget (Balance Mensual) - 100%
Todas las peticiones usan el loader:
- Cargar presupuesto inicial
- Guardar configuración
- Calcular balance
- Agregar gasto fijo
- Eliminar gasto fijo

### ✅ Card Detail (Detalle Tarjeta) - Parcial
- Cargar datos de tarjeta ✅
- Cargar cuotas (pendiente)
- Guardar cuota (pendiente)
- Marcar como pagada (pendiente)

---

## 🔄 FLUJO DE TRABAJO

### Ejemplo: Guardar Configuración

```
1. Usuario hace clic en "Guardar Configuración"
   ↓
2. JavaScript llama: fetchWithLoader('/api/budget/123', {...})
   ↓
3. showLoader() se ejecuta automáticamente
   ↓
4. Loader aparece en pantalla
   ↓
5. Petición HTTP se envía al servidor
   ↓
6. Servidor procesa y responde
   ↓
7. hideLoader() se ejecuta automáticamente (en finally)
   ↓
8. Loader desaparece
   ↓
9. showToast('Configuración guardada') aparece
```

---

## 🎯 CASOS DE USO

### ✅ Cuándo aparece el loader:

- ✅ Al cargar datos iniciales de una página
- ✅ Al guardar cambios en el servidor
- ✅ Al eliminar registros
- ✅ Al actualizar información
- ✅ Al calcular balances complejos
- ✅ Cualquier operación que tarde >100ms

### ❌ Cuándo NO aparece:

- ❌ Al abrir/cerrar modales (operación local)
- ❌ Al renderizar listas (operación local)
- ❌ Al validar formularios (operación local)
- ❌ Al cambiar pestañas (operación local)

---

## 🐛 TROUBLESHOOTING

### Problema: El loader no aparece

**Posible causa:** No estás usando `fetchWithLoader`

**Solución:**
```javascript
// ❌ INCORRECTO
const res = await fetch('/api/endpoint');

// ✅ CORRECTO
const res = await fetchWithLoader('/api/endpoint');
```

### Problema: El loader no desaparece

**Posible causa:** Error en la petición que no se manejó

**Solución:** El `finally` en `fetchWithLoader` siempre oculta el loader, incluso con errores. Verifica la consola.

### Problema: El loader parpadea muy rápido

**Respuesta:** Eso es normal si el servidor responde muy rápido (conexión local). En producción será más visible.

**Opcional:** Agregar delay mínimo:
```javascript
async function fetchWithLoader(url, options = {}) {
    showLoader();
    const minDelay = new Promise(resolve => setTimeout(resolve, 300));
    try {
        const [response] = await Promise.all([fetch(url, options), minDelay]);
        return response;
    } finally {
        hideLoader();
    }
}
```

---

## 📊 ESTADÍSTICAS DE IMPLEMENTACIÓN

| Aspecto | Estado |
|---------|--------|
| **Loader creado** | ✅ Sí |
| **CSS agregado** | ✅ Sí |
| **Funciones JS** | ✅ 3 funciones |
| **Budget.html** | ✅ 100% |
| **Card_detail.html** | ⏳ 20% |
| **Otros templates** | ⏳ 0% |

---

## 🚀 PRÓXIMOS PASOS

Para completar la implementación:

1. **Actualizar card_detail.html:**
   - loadInstallments()
   - loadMonthlyPayment()
   - deleteInstallment()
   - payInstallment()
   - installment-form submit

2. **Actualizar loans.html:**
   - loadLoans()
   - deleteLoan()
   - payMonthlyPayment()
   - loan-form submit

3. **Actualizar cards.html:**
   - loadCards()
   - deleteCard()
   - card-form submit

4. **Y así con todos los templates...**

---

## 💡 TIPS DE USO

### Tip 1: Siempre usa fetchWithLoader
```javascript
// ✅ BIEN
const res = await fetchWithLoader('/api/data');

// ❌ MAL
const res = await fetch('/api/data');
```

### Tip 2: No te preocupes por ocultar
```javascript
// ✅ BIEN - Se oculta automáticamente
const res = await fetchWithLoader('/api/data');

// ❌ MAL - No necesitas esto
const res = await fetchWithLoader('/api/data');
hideLoader(); // Innecesario
```

### Tip 3: Maneja errores normalmente
```javascript
// ✅ BIEN - El loader se oculta incluso con error
try {
    const res = await fetchWithLoader('/api/data');
    // ...
} catch (error) {
    showToast('Error', 'error');
}
```

---

## ✅ CHECKLIST DE VERIFICACIÓN

Marca cuando hayas verificado:

- [x] Loader se muestra al cargar Budget
- [x] Loader se muestra al guardar configuración
- [x] Loader se muestra al agregar gasto
- [x] Loader se muestra al eliminar gasto
- [x] Loader se muestra al calcular balance
- [x] Loader se muestra al cargar tarjeta
- [ ] Loader se muestra en todos los módulos

---

## 🎨 PERSONALIZACIÓN (Opcional)

### Cambiar color del spinner:
```css
.loader-spinner {
    border-top: 4px solid #10b981; /* Verde */
}
```

### Cambiar texto:
```html
<p class="text-gray-700 font-medium">Procesando...</p>
```

### Agregar logo:
```html
<img src="/static/logo.png" class="w-12 h-12 mb-2">
<div class="loader-spinner mb-4"></div>
```

---

## 📚 DOCUMENTACIÓN RELACIONADA

- **LOADER_IMPLEMENTADO.md** - Documentación técnica
- **RESUMEN_FINAL_COMPLETO.md** - Resumen del proyecto

---

**Creado:** 3 de Diciembre de 2024  
**Estado:** ✅ Implementado y funcional  
**Próximo paso:** Actualizar todos los templates

