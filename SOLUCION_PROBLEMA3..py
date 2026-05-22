# =====================================================================
# Fase 5 - Evaluación Final POA
# Problema 3: Auditoría de Inventario
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) para determinar la cantidad exacta a pedir.
    Lógica de negocio:
    - Si Stock Actual < Stock Mínimo -> Pide la diferencia.
    - Si Stock Actual >= Stock Mínimo -> Pide cero (0).
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def generar_informe_inventario(matriz_inventario):
    """
    Procesa la matriz de inventario e imprime el informe final requerido.
    """
    print("\n" + "="*50)
    print("        INFORME FINAL DE PEDIDOS - REABASTECIMIENTO")
    print("="*50)
    print(f"{'ARTÍCULO':<25} | {'CANTIDAD A PEDIR':<15}")
    print("-"*50)
    
    # Recorrido de la matriz fila por fila
    for fila in matriz_inventario:
        codigo = fila[0]
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]
        
        # Llamado al módulo/función de lógica de negocio
        cantidad_pedido = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Salida requerida: Nombre del artículo y cantidad exacta
        print(f"{nombre:<25} | {cantidad_pedido:<15}")
        
    print("="*50 + "\n")

# --- BLOQUE PRINCIPAL (Datos Iniciales) ---
if __name__ == "__main__":
    # Matriz inicial con 5 artículos como solicita el requerimiento
    # Formato: [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
    inventario = [
        ["ART001", "Teclado Mecánico RGB", 12, 15],  # Necesita (15 - 12 = 3)
        ["ART002", "Mouse Inalámbrico",     25, 20],  # Suficiente (0)
        ["ART003", "Monitor Gamer 24'",      3,  8],  # Necesita (8 - 3 = 5)
        ["ART004", "Auriculares Bluetooth",  30, 30],  # Al límite, suficiente (0)
        ["ART005", "Memoria USB 64GB",        5, 25]   # Crítico, necesita (25 - 5 = 20)
    ]
    
    # Ejecución del programa
    generar_informe_inventario(inventario)