# 📂 Organizador de Archivos

**Script en Python que ordena automáticamente archivos en distintas carpetas según su extensión y fecha de modificación.**

---
## Tecnologías usadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
---

## 🚀 Funcionamiento
Una pequeña interfaz gráfica en la que puedes seleccionar la ruta de la carpeta dónde están los archivos que se quieren ordenar y escoger como quieres hacer la organización, si por tipo de archivo o su fecha de modificación.

<p align="center">
  <img src="/docs/images/Por_tipo.png" alt="Ventana del programa">
</p>


### Botón para deshacer acción
En caso de ser necesario se pueden deshacer los cambios de la última acción.

<p align="center">
  <img src="/docs/images/Deshacer.gif" alt="Demo animado">
</p>


### Organizar archivos por tipo 
Se crean carpetas en función de los tipos de archivos existentes, y se mueven los mismos a la que le corresponde, los tipos de archivos que no están contemplados simplemente se mueven a una carpeta llamada “Otros”.

<p align="center">
  <img src="/docs/images/Por_tipo_de_archivo.gif" alt="Demo animado">
</p>

### Organizar archivos por fecha
Cuándo se usa esta opción hay tres comportamientos posibles dependiendo de las fechas encontradas en los archivos.

#### Diferentes años
Si existen archivos distribuidos en diferentes años se crearan carpetas para cada año y dentro de estas, subcarpetas por cada mes.

<p align="center">
  <img src="/docs/images/Por_fecha_years.gif" alt="Demo animado">
</p>


#### Diferentes meses
Si se encuentran archivos de diferentes meses pero todos ellos de un mismo año se crean carpetas para cada mes.

<p align="center">
  <img src="/docs/images/Por_fecha_meses.gif" alt="Demo animado">
</p>

#### Diferentes días
Si se encuentran únicamente archivos pertenecientes a un mismo mes se crearan carpetas por cada día de dicho mes.

<p align="center">
  <img src="/docs/images/Por_dias.gif" alt="Demo animado">
</p>

## 📁 Tipos de archivos contemplados


| Tipo de archivo | Extensiones consideradas |
|:----------:|:----------------------|
| 🖼️ **Imágenes** | `.png`, `.jpg`, `.jpeg`, `.webp` |
| 📄 **Documentos Word** | `.docx`, `.doc`, `.odt` |
| 📑 **Archivos de texto** | `.txt` |
| 📊 **Hojas de cálculo** | `.xlsx`, `.ods` |
| 📕 **PDF** | `.pdf` |
| 🗺️ **KML** | `.kml` |
| 📋 **CSV** | `.csv` |
| 🎬 **Videos** | `.mp4`, `.mkv` |
| 📦 **Comprimidos** | `.zip`, `.rar`, `.7z` |
| 🗃️ **Otros** | Los archivos con extensiones no contempladas se moverán a una carpeta llamada **`Otros`**. |

## Continuo trabajando en mejoras, se aprecian los comentarios y sugerencias.
