# Visualización de Monto Faltante en Cuotas Sin Intereses

## Cambio Implementado

Se agregó una nueva columna en la vista de detalle de tarjetas que muestra el **monto faltante por pagar** en cada compra a cuotas sin intereses, con un diseño optimizado y compacto para móviles.

## Ubicación

**Archivo modificado:** `templates/card_detail.html`

## Detalles de la Implementación

### Información Mostrada

En cada tarjeta de compra a cuotas, ahora se muestran 4 campos:

1. **Total**: El costo total de la compra
2. **Falta**: Monto pendiente por pagar (Pago Mensual × Cuotas Restantes)
3. **Mensual**: Cuota mensual a pagar
4. **Cuotas**: Número de cuotas pendientes del total (formato: X/Y)

### Cálculo

```javascript
const monthlyPayment = inst.monthly_payment || 0;
const remaining = inst.remaining_months || 0;
const amountRemaining = monthlyPayment * remaining;
```

### Diseño Responsive y Compacto

#### Mobile (< 768px)
- **Grid**: 2 columnas para los 4 campos
- **Padding**: 3 unidades (p-3)
- **Títulos**: Texto abreviado ("Total", "Falta", "Mensual", "Cuotas")
- **Valores**: text-sm (texto pequeño)
- **Botones**: Solo icono + para agregar, texto "Agregar" oculto
- **Título sección**: "Cuotas MSI" (versión corta)
- **Cajas de valores**: Fondo blanco con padding de 2 unidades para mejor legibilidad

#### Desktop (≥ 768px)
- **Grid**: 4 columnas para mostrar todos los campos en una fila
- **Padding**: 4 unidades (p-4)
- **Títulos**: Texto completo
- **Valores**: text-base (texto normal)
- **Botones**: Icono + texto completo
- **Título sección**: "Compras en Cuotas / MSI"

### Optimizaciones Aplicadas

1. **Reducción de espaciado**:
   - Padding: p-3 en móvil, p-4 en desktop
   - Gaps: gap-2 en móvil, gap-3 en desktop
   - Margin bottom: mb-2 en elementos internos

2. **Tipografía ajustada**:
   - Títulos: text-base en móvil, text-lg en desktop
   - Valores: text-sm en móvil, text-base en desktop
   - Cuotas: Formato compacto "6/12" en lugar de "6 de 12"

3. **Botones optimizados**:
   - Botón "Marcar cuota pagada": Ancho completo en móvil
   - Iconos de editar/eliminar: Padding reducido (p-1)
   - Espaciado entre iconos: space-x-1 en móvil

4. **Cajas de información**:
   - Fondo blanco individual para cada métrica
   - Bordes redondeados para mejor separación visual
   - Padding interno optimizado (p-2)

5. **Barra de progreso**:
   - Altura reducida: h-1.5 (más compacta)
   - Texto simplificado: "6 pagadas" en lugar de "Progreso: 6 cuotas pagadas"

### Colores

- **Total**: Texto gris/blanco (neutral)
- **Falta**: Naranja si está activo (#f97316), gris si está completado
- **Mensual**: Verde si está activo (#16a34a), gris si está completado
- **Cuotas**: Azul si está activo (#2563eb), gris si está completado

## Beneficios

1. **Visibilidad clara**: El usuario puede ver de inmediato cuánto dinero le falta pagar en cada compra
2. **Mejor planificación**: Facilita la toma de decisiones sobre pagos anticipados
3. **Cálculo automático**: Se actualiza automáticamente conforme se van pagando cuotas
4. **Diseño intuitivo**: El color naranja destaca el monto pendiente, facilitando su identificación
5. **Optimizado para móvil**: Vista compacta que permite ver más información sin scroll excesivo
6. **Mejor legibilidad**: Cajas individuales con fondo blanco separan visualmente cada métrica

## Ejemplo Visual Mobile

```
┌──────────────────────────────────────────┐
│ Laptop HP                      ✏️  🗑️   │
│ 15/12/2025                              │
│                                         │
│ ┌──────────┬──────────┐                │
│ │Total     │Falta     │                │
│ │S/ 3,600  │S/ 1,800  │                │
│ └──────────┴──────────┘                │
│ ┌──────────┬──────────┐                │
│ │Mensual   │Cuotas    │                │
│ │S/ 300    │6/12      │                │
│ └──────────┴──────────┘                │
│                                         │
│ 6 pagadas              50%             │
│ ██████████░░░░░░░░░░                   │
│                                         │
│ [✓ Marcar cuota pagada]                │
└──────────────────────────────────────────┘
```

## Notas

- El monto faltante se calcula multiplicando el pago mensual por las cuotas restantes
- Cuando una compra está completamente pagada (remaining = 0), muestra S/ 0.00 en gris
- El cálculo es preciso y se basa en los datos almacenados en Firebase
- Todas las optimizaciones mantienen la funcionalidad completa en dispositivos móviles
- El diseño usa clases responsive de Tailwind CSS (md:) para adaptarse automáticamente


