import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from file_organizer import move_files_2_folders


class App: 

    def __init__(self,root,file_extentions_dictionary):

        """
        Inicializa los parámetros principales de la interfaz gráfica.

        Arguments:
            root {tkinter.Tk} -- Ventana raíz de Tkinter

            file_extentions_dictionary {dict} -- Contiene extenciones de archivos (key) asociados a un tipo de archivo/carpeta (value).

        """

        self.file_extentions_dictionary = file_extentions_dictionary
        self.root = root
        self.root.title("Organizador de Archivos")
        self.root.minsize(width=400, height=200)
        self.root.grid_anchor("center")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self._create_widgets()
    
    def _create_widgets(self):
        
        """
        Crea los Labels y Botones en la interfaz gráfica

        """

        self.path_label = ttk.Label(self.root, text="Ruta:", font=(14))
        self.path_label.grid(row=0, column=1,padx=10,pady=10)

        # Entry del cuál se obtendrá la ruta de la carpeta
        self.path_entry = ttk.Entry(self.root, width=30,font=(6))
        self.path_entry.grid(row=1,column=1,padx=10,pady=10)

        #Boton para obetener el path mediante la función get_path()
        self.get_path_button = ttk.Button(self.root, text="...", command=self._get_path)
        self.get_path_button.grid(row=2,column=1,padx=10,pady=10)

        #Boton para organizar los archivos mediante la función move_files()
        organizer_button = ttk.Button(self.root, text="Organizar",command=self._move_files)
        organizer_button.grid(row=3,column=1,padx=10,pady=25)

    def _get_path(self):
        """

        Mediante filedialog obtiene la ruta del directorio que contiene los archivos para ordenar y la guarda en el atributo self.path,
        en caso de no hacer una selección de directorio muestra una advertencia en pantalla.

        Notes:

            self.path almacena la ruta obtenida pero lo que realmente se usa para hacer el ordenamiento es el contenido de self.path_entry, es por ello 
            que se carga el contenido de self.path al Entry.

        """
        self.path = filedialog.askdirectory(title="Selecciona la ruta de la carpeta")
        #self.path_entry.configure(text=self.path)

        if not self.path:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún directorio.")
        else:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0,self.path)
    

    def _move_files(self):
        """
        Ejecuta la función move_file_2_folders() del módulo file_organizer. Con esto se seleccionan que carpetas crear,
        se crean las carpetas y se mueven los archivos a la que le corresponde.
        
        Raises:
            AttributeError  
                Esto ocurre cuando se intenta ejecutar este atributo sin antes haber ejecutado el método _geth_path(),
                pue es ahí dónde se define el atributo self.path, por lo que de no hacerlo este no existirá en el programa. 

            FileNotFoundError
                Ocurre cuando se intenta manipular un archivo que no se encuentra, es provocado si al definir self.path se pasa una ruta que no existe 
                o ninguna ruta (str vacío).
            
            TypeError
                Cuando se ejecuta el método _get_path() y lo primero que se hace es cancelar, en vez de obtener un string la instrucción
                filedialog.askdirectory() devuelve una tupla. (Nota. No estoy seguro de por qué, tengo que investigar esto)

        
        Notes:
            Todas las excepciones ocurren dentro de la función move_files_2_folders(), que a su vez provienen de la funciones auxiliares
            de las que esta hace uso (Revisar el módulo file_organizer). ¿Sería mejor tratar la excepciones directamente en esas funciones? No se, debo investigarlo



        """
        try:
            move_files_2_folders(self.path_entry.get().strip(),self.file_extentions_dictionary)
        except AttributeError:
            messagebox.showwarning("Advertencia", "Primero seleccione un directorio")
        except FileNotFoundError:
            messagebox.showwarning("Advertencia", "Seleccione un directorio válido")
        except TypeError:
            messagebox.showwarning("Advertencia", "Seleccione un directorio válido")


def run_app(file_extentions_dictionary):
    """
    Ejecuta la interfaz gráfica usando Tkinter.

    Arguments:
        file_extentions_dictionary {diccionario} -- Contiene extenciones de archivos (key) asociados a un tipo de archivo/carpeta (value).

    """
    root = tk.Tk()
    app = App(root,file_extentions_dictionary)
    #print(type(root))
    root.mainloop()