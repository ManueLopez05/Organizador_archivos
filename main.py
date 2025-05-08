import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


#Almacenamos los nombres de las carpetas en una diccionario
path = None
file_extentions = {
    ".pdf":"PDFs",
    ".docx":"Documentos",
    ".doc":"Documentos",
    ".odt":"Documentos",
    ".txt":"Documentos_txt",
    ".png":"Imagenes",
    ".jpg":"Imagenes",
    ".jpeg": "Imagenes",
    ".webp": "Imagenes",
    ".xlsx":"Excel",
    ".ods":"Excel",
    ".mp4":"Videos",
    ".avi":"Videos",
    ".mkv":"Videos",
    ".zip":"Comprimidos",
    ".rar":"Comprimidos",
    ".7z": "Comprimidos",
    ".kml": "Archivos_kml",
    "otros": "Otros"  #Para todos los archivos no contemplados
}

#--------------------------------------------Funciones para los botónes----------------------------------------------
#Obtener ruta de carpeta
def get_path():
    global path
    path = filedialog.askdirectory(title="Selecciona la ruta de la carpeta")
    path_entry.configure(text=path)


def move_files():
    for folder_name in set(file_extentions.values()):
        folder_path = os.path.join(path,folder_name)
        if not os.path.exists(folder_path):os.makedirs(folder_path)

    for file in os.listdir(path):
        file_path = os.path.join(path,file)
        if os.path.isfile(file_path):
            name, file_ext = os.path.splitext(file)
            file_ext = file_ext.lower()
            if file_ext in file_extentions:
                shutil.move(file_path, os.path.join(path,file_extentions[file_ext],file))
            else:
                shutil.move(file_path,os.path.join(path,file_extentions["otros"],file))
    
    messagebox.showinfo("Info", "Se organizaron los archivos")


#-----------------------------------------------Aplicación Gráfica-----------------------------------------------------
#Iniciamos las Tkinter y configuramos la ventana principal
root = Tk()
root.title("Organizador de Archivos")
root.resizable(0,0)
#Body
#Para seleccionar la ruta
path_label = Label(root, text="Ruta:")
path_label.grid(row=1, column=0,padx=10,pady=25)

path_entry = Label(root, text="...........")
path_entry.grid(row=1,column=1,padx=10,pady=25)

path_button = Button(root, text="...", command=get_path)
path_button.grid(row=1,column=2,padx=10,pady=25)

#Botón que organiza los archivos
organization_button = Button(root, text="Organizar",command=move_files)
organization_button.grid(row=2,column=1,padx=10,pady=25)

root.mainloop()