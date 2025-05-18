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
    ".csv":"Archivos_csv",
    ".mp4":"Videos",
    ".avi":"Videos",
    ".mkv":"Videos",
    ".zip":"Comprimidos",
    ".rar":"Comprimidos",
    ".7z": "Comprimidos",
    ".kml": "Archivos_kml",
    "Otros": "Otros"  #Para todos los archivos no contemplados
}

#--------------------------------------------Funciones para los botónes----------------------------------------------

def get_path():
    global path
    path = filedialog.askdirectory(title="Selecciona la ruta de la carpeta")
    path_entry.configure(text=path)


def move_files():
    if not path:
        messagebox.showwarning("Advertencia","Primero seleccione una carpeta")
        return
    try:
        for folder_name in set(check_if_files_exists()):
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
                    shutil.move(file_path,os.path.join(path,file_extentions["Otros"],file))
        
        messagebox.showinfo("Mensaje", "Se organizaron los archivos")
    except Exception as e:
        messagebox.showerror("Error",f"Error:\n{str(e)}")

#Se crean las carpetas únicamente para los archivos que se encuentran en el directorio
def check_if_files_exists():
    folders = list()
    for file in os.listdir(path):
        file_path = os.path.join(path,file)

        if os.path.isfile(file_path):
            name, file_ext = os.path.splitext(file)
            file_ext = file_ext.lower()
            #print(file_ext)

            if file_ext in file_extentions and not file_extentions[file_ext] in folders:
                folders.append(file_extentions[file_ext])
            elif not file_ext in file_extentions and not file_extentions["Otros"] in folders:
                folders.append("Otros")
    #print(folders)
    return folders
#-----------------------------------------------Aplicación Gráfica-----------------------------------------------------
#Iniciamos las Tkinter y configuramos la ventana principal
root = Tk()
root.title("Organizador de Archivos")
root.minsize(width=400, height=200)
root.grid_anchor("center")

#Body---------------------------------------------

#Para seleccionar la ruta
path_label = Label(root, text="Ruta:", font=(14))
path_label.grid(row=0, column=1,padx=10,pady=10)

path_entry = Label(root, text="...........",font=(6))
path_entry.grid(row=1,column=1,padx=10,pady=10)

path_button = Button(root, text="...", command=get_path)
path_button.grid(row=2,column=1,padx=10,pady=10)

#Botón que organiza los archivos
organization_button = Button(root, text="Organizar",command=move_files)
organization_button.grid(row=3,column=1,padx=10,pady=25)

root.mainloop()