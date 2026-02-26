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

Este programa realiza análisis de datos de las bases de datos de la ONU sobre intercambio de armas a nivel mundial, determinando los suministradores y receptores de armas más prominentes, y los países con los que hacen más transacciones de esta índole, los mayores tipos de armas intercambiados, además, realiza el cruce de la base de datos de armas con la base de datos del crecimiento del PIB de los países a lo largo del tiempo.

Adicionalmente, se cuenta con dos versiones del programa, una que muestra los resultados a través de la librería Streamlit y otro a través de una interfaz de usuario cuidadosamente diseñada.