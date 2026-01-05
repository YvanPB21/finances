# Botón "Pagar Todas las Cuotas" - Implementado ✅

## Resumen

Se agregó un botón de acción masiva que permite marcar una cuota como pagada en todas las compras activas a meses sin intereses con un solo clic.

## Ubicación

**Archivo modificado:** `templates/card_detail.html`

## Funcionalidad

### Botón "Pagar Todas"

- **Ubicación**: Header de la sección "Compras en Cuotas / MSI", junto al botón "Agregar"
- **Icono**: `fa-check-double` (doble check)
- **Color**: Verde (`bg-green-500`)
- **Texto**: 
  - Móvil pequeño: Solo icono
  - Mobile/tablet: Icono + "Pagar Todas"

### Comportamiento

1. **Visibilidad Inteligente**:
   - Solo se muestra cuando hay al menos una cuota activa (con remaining_months > 0)
   - Se oculta automáticamente cuando todas las cuotas están completadas
   - Se oculta si no hay ninguna compra registrada

2. **Confirmación**:
   - Solicita confirmación antes de ejecutar la acción
   - Muestra el número de compras que serán afectadas
   - Mensaje claro: "¿Marcar una cuota como pagada en X compra(s)?"

3. **Procesamiento**:
   - Marca una cuota como pagada en cada compra activa
   - Actualiza el campo `paid_months` incrementándolo en 1
   - Procesa todas las cuotas de forma secuencial
   - Muestra indicador de carga durante el proceso

4. **Feedback**:
   - Botón deshabilitado durante el procesamiento
   - Texto cambia a "Procesando..." con spinner animado
   - Toast de éxito mostrando cuántas cuotas se marcaron
   - Toast de advertencia si hubo errores parciales

5. **Actualización Automática**:
   - Recarga la lista de cuotas después de procesar
   - Actualiza el cálculo del pago mensual
   - Actualiza la visibilidad del botón

## Código Implementado

### HTML

```html
<button id="pay-all-installments-btn" 
        onclick="payAllInstallments()" 
        class="flex-1 md:flex-none bg-green-500 text-white px-3 md:px-4 py-2 rounded-lg hover:bg-green-600 transition text-sm md:text-base disabled:opacity-50 disabled:cursor-not-allowed" 
        style="display: none;">
    <i class="fas fa-check-double"></i>
    <span class="hidden sm:inline ml-2">Pagar Todas</span>
</button>
```

### JavaScript - Lógica de Visibilidad

```javascript
function renderInstallments() {
    // ...existing code...
    
    // Check if there are any active installments
    const hasActiveInstallments = installments.some(inst => (inst.remaining_months || 0) > 0);
    payAllBtn.style.display = hasActiveInstallments ? 'block' : 'none';
    
    // ...existing code...
}
```

### JavaScript - Función Principal

```javascript
async function payAllInstallments() {
    // 1. Filtrar cuotas activas
    const activeInstallments = installments.filter(inst => (inst.remaining_months || 0) > 0);
    
    // 2. Validar que hay cuotas activas
    if (activeInstallments.length === 0) {
        showToast('No hay cuotas activas para pagar', 'info');
        return;
    }

    // 3. Confirmar acción
    const confirmation = confirm(`¿Marcar una cuota como pagada en ${activeInstallments.length} compra(s)?`);
    if (!confirmation) return;

    // 4. Deshabilitar botón y mostrar loading
    const payAllBtn = document.getElementById('pay-all-installments-btn');
    payAllBtn.disabled = true;
    payAllBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i><span class="hidden sm:inline ml-2">Procesando...</span>';

    // 5. Procesar cada cuota
    let successCount = 0;
    let errorCount = 0;

    for (const inst of activeInstallments) {
        try {
            const newPaidMonths = (inst.paid_months || 0) + 1;
            const res = await fetch(`/api/cards/${cardId}/installments/${inst.id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    description: inst.description,
                    total_amount: inst.total_amount,
                    total_months: inst.total_months,
                    paid_months: newPaidMonths,
                    purchase_date: inst.purchase_date
                })
            });

            if (res.ok) successCount++;
            else errorCount++;
        } catch (error) {
            errorCount++;
        }
    }

    // 6. Recargar datos
    await loadInstallments();
    await loadMonthlyPayment();

    // 7. Mostrar resultado
    if (errorCount === 0) {
        showToast(`✓ ${successCount} cuota(s) marcada(s) como pagada(s)`);
    } else {
        showToast(`${successCount} exitosas, ${errorCount} fallidas`, 'warning');
    }

    // 8. Restaurar botón
    payAllBtn.disabled = false;
    payAllBtn.innerHTML = '<i class="fas fa-check-double"></i><span class="hidden sm:inline ml-2">Pagar Todas</span>';
}
```

## Casos de Uso

### Escenario 1: Pago mensual regular
**Situación**: El usuario tiene 5 compras a MSI activas y quiere marcar el pago del mes actual.

**Flujo**:
1. Usuario hace clic en "Pagar Todas"
2. Confirma la acción
3. Sistema marca 1 cuota como pagada en cada una de las 5 compras
4. Se actualizan todas las barras de progreso
5. Se recalcula el pago mensual total

**Resultado**: 
- 5 cuotas marcadas como pagadas
- Pago mensual reducido (si algunas se completaron)
- Toast: "✓ 5 cuota(s) marcada(s) como pagada(s)"

### Escenario 2: Solo una cuota activa
**Situación**: Usuario tiene solo 1 compra pendiente.

**Flujo**:
1. Usuario hace clic en "Pagar Todas"
2. Confirma: "¿Marcar una cuota como pagada en 1 compra(s)?"
3. Sistema procesa y actualiza

**Resultado**: 
- 1 cuota marcada
- Si era la última, la compra se marca como completada y el botón desaparece

### Escenario 3: Todas las cuotas completadas
**Situación**: Todas las compras ya están pagadas.

**Flujo**:
1. Botón "Pagar Todas" no es visible

**Resultado**: 
- UI limpia, sin botones innecesarios

### Escenario 4: Error parcial
**Situación**: Fallo de red o error en alguna cuota durante el procesamiento.

**Flujo**:
1. Usuario hace clic en "Pagar Todas"
2. Sistema procesa 3 exitosamente, 1 falla
3. Toast: "3 exitosas, 1 fallidas"

**Resultado**: 
- Cuotas exitosas se actualizan
- Usuario puede reintentar para la fallida

## Diseño Responsive

### Mobile (< 640px)
```
┌────────────────────────────────────┐
│ Cuotas MSI                         │
│ ┌──────────┬──────────┐           │
│ │ [✓✓]     │ [+]      │           │
│ └──────────┴──────────┘           │
└────────────────────────────────────┘
```

### Mobile/Tablet (≥ 640px)
```
┌────────────────────────────────────┐
│ Cuotas MSI                         │
│ ┌────────────┬────────────┐       │
│ │ ✓✓ Pagar   │ + Agregar  │       │
│ │   Todas    │            │       │
│ └────────────┴────────────┘       │
└────────────────────────────────────┘
```

### Desktop (≥ 768px)
```
┌──────────────────────────────────────────────────┐
│ Compras en Cuotas / MSI                          │
│                      [✓✓ Pagar Todas] [+ Agregar]│
└──────────────────────────────────────────────────┘
```

## Beneficios

1. **Ahorro de tiempo**: Un solo clic para actualizar múltiples cuotas
2. **Menos errores**: Evita olvidar marcar alguna cuota
3. **Flujo natural**: Simula el pago mensual real de la tarjeta
4. **Feedback claro**: Usuario sabe exactamente qué se procesó
5. **Seguridad**: Requiere confirmación antes de ejecutar
6. **Robusto**: Maneja errores parciales y muestra el resultado detallado

## Mejoras Futuras Sugeridas

1. **Selector individual**: Checkbox para elegir qué cuotas pagar
2. **Pagar múltiples meses**: Opción para marcar 2 o más cuotas en cada compra
3. **Fecha de pago**: Registrar la fecha en que se marcó como pagada
4. **Historial**: Ver cuándo se pagaron las cuotas
5. **Deshacer**: Opción para revertir el último pago masivo
6. **Pago parcial**: Marcar solo las cuotas que vencen antes de cierta fecha

## Notas Técnicas

- **Procesamiento secuencial**: Las cuotas se procesan una por una (no en paralelo) para evitar problemas de concurrencia
- **Validación**: Se verifica que cada cuota tenga remaining_months > 0 antes de procesarla
- **Estado del botón**: Se usa `disabled` para prevenir clics múltiples durante el procesamiento
- **Recarga completa**: Se recargan tanto las cuotas como el resumen de pago mensual
- **Manejo de errores**: Cada cuota se procesa en un try-catch individual para que un error no detenga todo el proceso

## Testing

### Casos de prueba
- [x] Marcar cuotas con 1 compra activa
- [x] Marcar cuotas con múltiples compras activas
- [x] Verificar que el botón desaparece cuando no hay cuotas activas
- [x] Verificar confirmación antes de procesar
- [x] Verificar estado de loading durante procesamiento
- [x] Verificar actualización de datos después de procesar
- [x] Verificar manejo de errores
- [x] Verificar diseño responsive (mobile/desktop)
- [x] Verificar que funciona con dark mode

## Conclusión

El botón "Pagar Todas" mejora significativamente la experiencia de usuario al permitir actualizar múltiples cuotas con un solo clic, simulando el flujo natural de pago mensual de una tarjeta de crédito.

