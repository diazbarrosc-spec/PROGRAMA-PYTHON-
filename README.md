# PROGRAMA-PYTHON-
Solución al Problema 3 (Auditoría de Inventario) para la Evaluación Final POA del curso Fundamentos de Programación - UNAD 2026. Estudiante: CARLOS GUILLERMO DIAZ BARROS.
# Evaluación Final POA - Fase 5: Fundamentos de Programación

Este repositorio contiene la solución informática estructurada para el **Problema 3: Auditoría de Inventario**, correspondiente a la evaluación final del curso de Fundamentos de Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

## Descripción del Problema Seleccionado
**Problema 3:** Se requiere una herramienta para auditar el inventario y decidir qué artículos necesitan ser reabastecidos. La información se gestiona a través de una matriz con el formato: `[Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]`.

### Lógica de Negocio Aplicada:
* Si el **Stock Actual** es menor al **Stock Mínimo Requerido**, la cantidad exacta a pedir es la diferencia (`Mínimo Requerido - Stock Actual`).
* Si el **Stock Actual** es suficiente (mayor o igual al mínimo), la cantidad a pedir es estrictamente cero (`0`).

---

## Estructura del Proyecto
El desarrollo se realizó bajo el **paradigma de programación estructurada y modular** utilizando **Python**, cumpliendo con los siguientes requerimientos del algoritmo:
* **Matriz de datos (`inventario`):** Inicialización de un arreglo bidimensional con 5 registros de prueba que contienen el código, nombre, existencias actuales y topes mínimos.
* **Modularidad (`calcular_cantidad_a_pedir`):** Función independiente que procesa la lógica condicional del negocio para determinar las unidades faltantes.
* **Generación de Reporte (`generar_informe_inventario`):** Módulo encargado de iterar las filas del arreglo mediante un ciclo `for` e imprimir los resultados de manera limpia y formateada.

---

## Cómo Ejecutar el Programa
1. Asegúrate de tener instalado **Python 3** en tu equipo.
2. Descarga el archivo de este repositorio.
3. Ejecuta el programa principal desde tu terminal o consola de comandos:
   ```bash
   python solucion_problema3.py
