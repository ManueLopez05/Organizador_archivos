import os
import shutil

def move_files_2_folders(path,file_extentions_dictionary):

    """
    Mueve todos los archivos a sus carpetas correspondientes.

    Arguments:
        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

        file_extention_dictionary {dict} -- contiene extenciones de archivos (key) asociados a un tipo de archivo/carpeta (value).

    Raises:

    
    See Also:
        _check_files_in_folderpath() [En este módulo] -- Revisa que tipos de archivos existen en el directorio.

        _create_folders() [En este módulo] -- Crea las carpetas a dónde se moverán los archivos.
    
        
    """
    #Se genera el set de nombres de carpetas
    folders_set = _check_files_in_folderpath(path, file_extentions_dictionary)
    #Se crean las carpetas con el set obtenido
    _create_folders(path, folders_set)

    for item in os.listdir(path):

        item_path = os.path.join(path,item)

        if os.path.isfile(item_path):
            #Se obtiene la extención del archivo
            name, file_extention = os.path.splitext(item)
            file_extention = file_extention.lower()

            #Se comprueba si está dentro del diccionario para moverse a la carpeta que corresponde
            if file_extention in file_extentions_dictionary:
                shutil.move(item_path, os.path.join(path,file_extentions_dictionary[file_extention],item))

            #Si no se encuentra en el diccionario, se mueve a la carpeta otros
            else:
                shutil.move(item_path,os.path.join(path,file_extentions_dictionary["Otros"],item))




def _check_files_in_folderpath(path, file_extentions_dictionary):

    """

    Compara los archivos que están en el directorio proporcionado con los considerados en el diccionario para generar un set 
    con los nombres de las carpetas que se deben crear y evitar crear carpetas que no se usen.

    Arguments:

        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

        file_extention_dictionary {dict} -- Contiene extenciones de archivos (key) asociados a un tipo de archivo/carpeta (value).
    
    Raises:


    Returns:
        {set} -- Contiene los nombres de las carpetas que se deben crear.
    
    Notes:
        Las  condiciones extra comentadas en las sentencias condicionales if y elif anidadas son para asegurarse de no añadir el mismo nombre
        de carpeta mas de una vez, sin embargo, un conjunto (set) elimina de manera automatica los valores repetidos
        dentro de el. Se dejaron como comentarios en caso de ser necesarias.

    """
    
    folders_set = set()

    for item in os.listdir(path):
        item_path = os.path.join(path,item)

        if os.path.isfile(item_path):
            #Se obtiene la extención del archivo
            name, file_extention = os.path.splitext(item)
            file_extention = file_extention.lower()
            
            #Comprobamos si la extención de archivo se encuentra en el diccionario
            if file_extention in file_extentions_dictionary: #and not file_extentions_dictionary[file_extention] in folders_set:
                #Se añade el nombre de la carpeta al set si existe el tipo de archivo correspondiente
                folders_set.add(file_extentions_dictionary[file_extention])

            #Se añade el nombre de la carpeta Otros si se encuentran extenciones no contempladas en el diccionario
            elif not file_extention in file_extentions_dictionary: #and not file_extentions_dictionary["Otros"] in folders_set:
                folders_set.add("Otros")

    return folders_set



def _create_folders(path, folders_set):  
    
    """

    Crea las carpetas necesarias para mover los archivos en el directorio proporcionado.

    Arguments:

        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

        folders_set {set} -- Contiene los nombres de las carpetas a crear.

    Raises:


    """
    #Se recorre el set con los nombres de las carpetas
    for folder_name in folders_set:
        
        folder_path = os.path.join(path,folder_name)
        #Se crea la carpeta solo si esta no existe
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)