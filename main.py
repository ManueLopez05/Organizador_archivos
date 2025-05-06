import os
import shutil
from tkinter import Tk, filedialog


#Iniciamos las Tkinter
main_window = Tk()
main_window.withdraw()

#Ruta de la carpeta dónde se encuentran los archivos a ordenar

path = filedialog.askdirectory(title="Selecciona la ruta de la carpeta")

#Crear carpetas dónde se van a almacenar los archivos
#Una por cada categória que se quiera

#Almacenamos los nombres de las carpetas en una lista

file_extentions = {
    ".pdf":"PDFs",
    ".docx":"Documentos",
    ".doc":"Documentos",
    ".odt":"Documentos",
    ".txt":"Documentos_txt",
    ".png":"Imagenes",
    ".jpg":"Imagenes",
    ".xlsx":"Excel",
    ".ods":"Excel",
    "otros": "Otros"  #Para todos los archivos no contemplados
}

#Se crean los directorios

for folder_name in set(file_extentions.values()):
    folder_path = os.path.join(path,folder_name)
    if not os.path.exists(folder_path):os.makedirs(folder_path)

#Ahora movemos los archivos a las carpetas creadas

for file in os.listdir(path):
    file_path = os.path.join(path,file)
    if os.path.isfile(file_path):
        name, file_ext = os.path.splitext(file)
        file_ext = file_ext.lower()
        if file_ext in file_extentions:
            shutil.move(file_path, os.path.join(path,file_extentions[file_ext],file))
        else:
            shutil.move(file_path,os.path.join(path,file_extentions["otros"],file))