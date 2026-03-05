import os
import shutil
from datetime import datetime



def organize_files_by_type(path,file_extentions_dictionary):

    """
    Mueve todos los archivos a sus carpetas correspondientes.

    Arguments:
        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

        file_extention_dictionary {dict} -- contiene extenciones de archivos (key) asociados a un tipo de archivo/carpeta (value).

    Raises:

    
    See Also:
        _check_files_in_folderpath() [En este módulo] -- Revisa que tipos de archivos existen en el directorio.

        _create_folders() [En este módulo] -- Crea las carpetas a dónde se moverán los archivos.

        _browse_files() [En este módulo] -- Genera una lista con los archivos en el directorio.
    
    Retunrs:
        {list} -- Contiene las rutas finales de todos los archivos movidos.
        {set} -- Contiene todas las rutas de los directorios padre creados.
        
    """
    #Se genera el set de nombres de carpetas
    folders_set = _check_files_in_folderpath(path, file_extentions_dictionary)
    #Se crean las carpetas con el set obtenido
    _create_folders(path, folders_set)
    #Se genera las listas de, rutas, extenciones y nombres de los archivos en el directorio
    file_path_list, file_list, file_extensions_list = _browse_files(path)

    # Lista para guardar las rutas de destino de todos los archivos movidos
    final_file_path_list = []

    # Set para guardar la ruta de todos los directorios creados
    final_dir_path_set = set()

    for file_extension, item_path, item in zip(file_extensions_list,file_path_list,file_list):
        #Se comprueba si está dentro del diccionario para moverse a la carpeta que corresponde
        if file_extension in file_extentions_dictionary:
            directory = os.path.join(path,file_extentions_dictionary[file_extension])
            shutil.move(item_path,directory)
            print(f"\nSe movió el archivo {item_path} a {directory}")

            #Guardamos las rutas de destino
            final_file_path_list.append(directory+"/"+item)
            final_dir_path_set.add(directory)

        #Si no se encuentra en el diccionario, se mueve a la carpeta otros
        else:
            directory = os.path.join(path,file_extentions_dictionary["Otros"])
            shutil.move(item_path, directory)
            print(f"\nSe movió el archivo {item_path} a {directory}")

            #Guardamos las rutas de destino
            final_file_path_list.append(directory+"/"+item)
            final_dir_path_set.add(directory)

    # Para depuración
    # print("Lista de rutas destino")
    # print(final_file_path_list)
    # print("Set de directorios creados")
    # print(final_dir_path_set)

    return final_file_path_list, final_dir_path_set



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

    See Also:
        _browse_files() [En este módulo] -- Genera una lista con los archivos en el directorio.
    """
    
    folders_set = set()

    file_path_list, file_list, file_extensions_list = _browse_files(path)

    for file_extension in file_extensions_list: 
            #Comprobamos si la extención de archivo se encuentra en el diccionario
            if file_extension in file_extentions_dictionary: #and not file_extentions_dictionary[file_extention] in folders_set:
                #Se añade el nombre de la carpeta al set si existe el tipo de archivo correspondiente
                folders_set.add(file_extentions_dictionary[file_extension])

            #Se añade el nombre de la carpeta Otros si se encuentran extenciones no contempladas en el diccionario
            elif not file_extension in file_extentions_dictionary: #and not file_extentions_dictionary["Otros"] in folders_set:
                folders_set.add("Otros")
    #------------------------------------------Para depuración----------------------------------------------------------
    # print("------------------------------------En función _check_files_in_folderpath()------------------------")
    # print(f"Tamaño de set de carpetas: {len(folders_set)}")

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



def _browse_files(path):
    """
    Hace una lista de todos los archivos que encuentra en el directorio.

    Arguments:
        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

    Returns:
        {list} -- Contiene el nombre de todos lo archivos encontrados en el directorio.
        {list} -- Contiene las extenciones de archivo de los items encontrados en el directorio.
        {list} -- Contiene los nombres de archivo de los items encontrados en el directorio.
    Raises:
    
    """
    file_path_list = []
    file_extensions_list = []
    file_list = []


    for item in os.listdir(path):
        item_path = os.path.join(path,item)

        if os.path.isfile(item_path):
            file_list.append(item)
            file_path_list.append(item_path)
            

            name, file_extension = os.path.splitext(item_path)
            file_extension = file_extension.lower()
            file_extensions_list.append(file_extension)

            print("\n",item_path)
            print("\n",item)
            print("\n",file_extension)

    # Para depuración
    # print("----------------------En función _browse_files()----------------------------------")
    # print(f"Tamaño de lista ruta de archivos: {len(file_path_list)}\nTamaño de lista nombres: {len(file_list)}\nTamaño de lista extenciones: {len(file_extensions_list)}")

    return file_path_list, file_list, file_extensions_list



def organize_files_by_date(path):
    """
    Función que organiza los archivos según su fecha de modificación.

    Arguments:
        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

    Retunrs:
        {list} -- Contiene las rutas finales de todos los archivos movidos.
        {set} -- Contiene todas las rutas de los directorios padre creados.
    """

    file_path_list, file_list, file_extensions_list = _browse_files(path)

    months_years = _check_date(file_path_list)

    # Lista para guardar las rutas de destino de todos los archivos movidos
    final_file_path_list = []

    # Set para guardar la ruta de todos los directorios creados
    final_dir_path_set = set()

    for file_path, file in zip(file_path_list,file_list):
        # Se obtien la fecha de modificación
        modified_time = os.path.getmtime(file_path)

        # Convertimos modified_time a un tipo de dato datatime
        date = datetime.fromtimestamp(modified_time)

        month = date.strftime("%B")
        day = date.day

        # Se crea el nombre del directorio con el mes y día
        if months_years == "varios meses y anios":
            year = date.year
            directory = os.path.join(path,str(year),month)
            final_dir_path_set.add(os.path.dirname(directory))
            
        elif months_years == "varios meses":
            directory = os.path.join(path,month)
            final_dir_path_set.add(directory)
        elif months_years == "basico":
            directory = os.path.join(path,f"{month} - {day}")
            final_dir_path_set.add(directory)

        # Se crcrea el nombre del directorio con mes y subcarpetas con día
        #directory = os.path.join(path, f"{month}/{day}")

        # Se crea el directorio

        os.makedirs(directory,exist_ok=True)

        # Se mueve el archivo
        shutil.move(file_path, directory)

        #Guardamos las rutas de destino
        final_file_path_list.append(directory+"/"+file)
        

        


        # Para depuración
        print("-------------------------------------En función organize_files_by_date()----------------------------------")
        print(f"Se movió '{file_path}' a '{directory}'")
    
    print("Lista de rutas destino")
    print(final_file_path_list)
    print("Set de directorios creados")
    print(final_dir_path_set)

    return final_file_path_list, final_dir_path_set



def _check_date(file_path_list):
    """
    Revisa las fechas de todos los archivos para saber si solo abercan un mes, varios meses o varios años.

    Arguments:
        file_path_list {list} -- Una lista con las rutas de todos los archivos en el directorio.

    Return:
        {str} -- Regresa un string que indica si hay o no varios años y varios meses.
    """

    years = set()
    months = set()

    for file_path in file_path_list:

        # Se obtien la fecha de modificación
        modified_time = os.path.getmtime(file_path)

        # Convertimos modified_time a un tipo de dato datatime
        date = datetime.fromtimestamp(modified_time)

        month = date.strftime("%B")
        year = date.year

        years.add(year)
        months.add(month)
    
    if len(months) > 1:
        if len(years) > 1:
            return "varios meses y anios"
        return "varios meses"
    else:
        return "basico"
    


def undo_action(path, final_file_path_list, final_dir_path_set):
    """
    Deshace todas las acciones hechas, regresa todos los archivos a el directorio original y elimina los directorios creados

    Parameters:
        path {str} -- Contiene la ruta del directorio dónde se encuentran los archivos a ordenar.

        final_file_path_list {list} -- Contiene las rutas finales de todos los archivos movidos.

        final_dir_path_set {set} -- Contiene todas las rutas de los directorios padre creados.
    """

    for file_paht in final_file_path_list:
        shutil.move(file_paht,path)
    
    for dir_path in final_dir_path_set:
        shutil.rmtree(dir_path)

