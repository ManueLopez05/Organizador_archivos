import gui

#Diccionario con las extenciones de archivo(key)  y carpeta que le corresponde (value)
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
#print(type(file_extentions))
if __name__ == "__main__":
    gui.run_app(file_extentions)