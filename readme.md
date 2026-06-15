\# 🌍 Sistema de Gestión de Datos de Países en Python



Trabajo Práctico Integrador (TPI) para la materia \*\*Programación 1\*\*.

\*\*Institución:\*\* Universidad Tecnológica Nacional (UTN) - Tecnicatura Universitaria en Programación a Distancia.



\## 👥 Equipo de Desarrollo

\* Alejandro Nicolás Abrigo

\* Sofia Anahí Rosales



\## 📝 Descripción del Proyecto

Este proyecto es una aplicación de consola desarrollada en Python 3 que permite gestionar un dataset de países. El sistema carga los datos desde un archivo `.csv` a una arquitectura basada en listas de diccionarios, permitiendo una manipulación eficiente en memoria y asegurando la persistencia de los cambios físicos en el archivo de origen.



\## ⚙️ Funcionalidades Principales (Estructura)

1\. \*\*ABM (Alta, Baja y Modificación):\*\* Agregar nuevos países validando que no existan duplicados y actualizar valores de población o superficie.

2\. \*\*Búsqueda y Filtros:\*\* Búsqueda por coincidencia parcial de nombre y filtros dinámicos por continente, rango de población o rango de superficie.

3\. \*\*Ordenamiento Dinámico:\*\* Reorganización del dataset mediante funciones `lambda` para ordenar por población, superficie, nombre o densidad poblacional.

4\. \*\*Motor Estadístico:\*\* Cálculo de promedios globales, detección de máximos/mínimos poblacionales y de superficie, y agrupación/conteo por continentes.

5\. \*\*Persistencia:\*\* Guardado automático en `paises.csv` utilizando el módulo `csv.DictWriter`.



\## 🚀 Instrucciones de Ejecución

Para correr el programa en un entorno local:



1\. Clonar el repositorio en tu máquina local:

&#x20;  `git clone \[URL\_DEL\_REPOSITORIO]`

2\. Asegurarse de tener instalado Python 3.x.

3\. Verificar que el archivo `paises.csv` se encuentre en la misma carpeta raíz que el script principal.

4\. Ejecutar el archivo principal desde la terminal:

&#x20;  `python main.py`



\## 📚 Librerías Utilizadas

El proyecto fue desarrollado utilizando exclusivamente bibliotecas de la \*\*librería estándar de Python\*\*, evitando dependencias de terceros:

\* `csv`: Para la lectura (`DictReader`) y escritura (`DictWriter`) del dataset persistente.

\* `pathlib`: Para la validación segura de la existencia del archivo físico antes de su lectura.



\## 🔗 Enlaces Relevantes

\* \*\*Documentación Técnica (PDF):\*\* \[[Link al PDF subido en el repo](https://github.com/tiamant/gestion-datos-paises/blob/main/Universidad%20Tecnol%C3%B3gica%20Nacional.pdf)]

\* \*\*Video Demostración:\*\* \[Link a YouTube - (https://youtu.be/OHl6K2mJC3w)]

