# Análisis-intercambios-de-armas
Proyecto con el fin de analizar las bases de datos de la ONU sobre intercambios de armas a nivel mundial

## Requisitos previos

Para utilizar adecuadamente este programa debe instalar Python, a continuación se muestra en enlace de descarga.

https://www.python.org/downloads/

Luego de instalar la última versión de Python, debe instalar las librerías necesarias, esto se puede hacer en Windows siguiendo los pasos descritos a continuación.

- Presiona la tecla Win+R para abrir la ventana de ejecutar.
- En esta ventana escribe "cmd", sin comillas, y luego presiona Enter.
- En la ventana del símbolo del sistema pega lo siguiente:

```
pip install darkdetect
pip install pywinstyles
pip install pandas
pip install numpy
pip install matplotlib
pip install tkintermapview
pip install ttkbootstrap
pip install sv-ttk
```

## Resumen

Este proyecto analiza las bases de datos de la ONU sobre intercambios de armas a nivel mundial, combinadas con datos de PIB del Banco Mundial. Los análisis principales incluyen:

- **Proveedores y Receptores de Armas:** Identificación de los top 20 países proveedores y receptores de armas, basados en el número total de armas entregadas.
- **Análisis de Relaciones Clave:** Para el mayor proveedor global, se muestran sus top 5 receptores; para el mayor receptor, sus top 5 proveedores.
- **Tipos de Armas:** Clasificación de los top 20 tipos de armas más entregadas.
- **Relación con el PIB:**
   - Gráficos de evolución del PIB de países seleccionados.
   - Comparaciones entre PIB y distribución de armas (para proveedores) o recepción de armas (para receptores), desde 1960 hasta 2024, usando ejes duales para visualizar tendencias económicas y armamentísticas.
- **Datos Procesados:** Los datos se limpian y agrupan por países, años y tipos de armas, eliminando valores nulos y enfocándose en entregas/órdenes de armas.
El objetivo es comprender dinámicas globales del comercio de armas, actores clave y su vínculo con el crecimiento económico.

Capacidades del Proyecto
El proyecto cuenta con dos versiones para ejecutar los análisis, permitiendo flexibilidad en el acceso a los resultados.

### 1. Ejecución a través de Streamlit (Versión Web Interactiva)
- **Archivo Principal:** Version_Streamlit/Intercambio_de_armas.py.
- **Capacidades:**
  - Interfaz web accesible desde un navegador (ejecutable con streamlit run streamlit_app.py).
  - Gráficos interactivos generados con Matplotlib, mostrados directamente en la app.
  - Secciones dedicadas para cada análisis (proveedores, receptores, tipos de armas, etc.).
  - Selectores interactivos (selectboxes) para elegir países en gráficos relacionados con PIB (e.g., PIB de un país específico o comparación PIB vs. armas para proveedores/receptores).
  - Carga automática de datos desde carpetas Datos (armas) y PIB (económicos).
  - ncluye una introducción con información del proyecto y autores.
- **Ventajas:** Fácil de compartir, no requiere instalación adicional en el navegador, ideal para presentaciones o acceso remoto.
- **Requisitos:** Instalar Streamlit (pip install streamlit) y las dependencias (pandas, numpy, matplotlib).
### 2. Ejecución a través de Interfaz de Usuario (Versión de Escritorio)
Archivo Principal: main.py.
Capacidades:
Interfaz gráfica de escritorio usando Tkinter con ttkbootstrap para un diseño moderno y responsivo (incluye temas oscuros/claros y personalización de la barra de título en Windows).
Menú lateral deslizable con opciones para cada análisis (Inicio, Proveedores, Receptores, etc.).
Botones para mostrar gráficos en ventanas dedicadas; los gráficos se generan con Matplotlib y se integran en frames de la GUI.
Funcionalidad para seleccionar países en análisis de PIB vs. armas (usando comboboxes o inputs).
Ventana de inicio con descripción del proyecto, autores y resumen.
Opción para salir de la aplicación.
Ventajas: Experiencia nativa de escritorio, con navegación intuitiva y personalización visual; no requiere navegador.
Requisitos: Instalar librerías como ttkbootstrap, pandas, numpy, matplotlib, y dependencias adicionales (ver README.md para comandos de instalación).
Ambas versiones usan las mismas funciones de procesamiento de datos (data.py o function_lib.py), asegurando consistencia en los resultados. El proyecto es portable y puede ejecutarse en Windows (como se indica en el README), con datos en formato CSV.