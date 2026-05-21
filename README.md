# PROGRAMA-PYTHON-
Solución al Problema 3 (Auditoría de Inventario) para la Evaluación Final POA del curso Fundamentos de Programación - UNAD 2026. Estudiante: CARLOS GUILLERMO DIAZ BARROS.
# Evaluación Final POA - Fase 5: Fundamentos de Programación

Este repositorio contiene la solución informática estructurada para el **Problema 3: Auditoría de Inventario**, correspondiente a la evaluación final del curso de Fundamentos de Programación de la Universidad Nacional Abierta y a Distancia (UNAD).

##  Descripción del Problema Seleccionado
**Problema 3:** Se requiere una herramienta para auditar el inventario y decidir qué artículos necesitan ser reabastecidos. La información se gestiona a través de una matriz con el formato: `[Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]`.

### Lógica de Negocio Aplicada:
* Si el **Stock Actual** es menor al **Stock Mínimo Requerido**, la cantidad exacta a pedir es la diferencia (`Mínimo Requerido - Stock Actual`).
* Si el **Stock Actual** es suficiente (mayor o igual al mínimo), la cantidad a pedir es estrictamente cero (`0`).

---

##  Estructura del Proyecto
El desarrollo se realizó bajo el **paradigma de programación estructurada y modular** utilizando **Python**, cumpliendo con los siguientes requerimientos core:
* **Matriz de datos:** Inicialización de un arreglo bidimensional con 5 registros de prueba.
* **Modularidad (RAC 3):** Creación de la función independiente `calcular_cantidad_a_pedir()` para procesar la lógica de negocio de manera aislada.
* **Estructuras de repetición:** Recorrido dinámico de las filas de la matriz mediante un ciclo `for`.

---

##  Cómo Ejecutar el Programa
1. Asegúrate de tener instalado **Python 3** en tu equipo.
2. Clona o descarga este repositorio.
3. Ejecuta el archivo principal desde tu terminal o consola de comandos:
   ```bash
   python solucion_problema3.py
