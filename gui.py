import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from file_organizer import organize_files_by_type, organize_files_by_date, undo_action


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
        self.root.minsize(width=400, height=300)
        self.root.grid_anchor("center")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        #Variable para control del tipo de ordenamiento
        self.modo_ordenamiento = tk.StringVar(value="por_tipo")
        #Se generan los widgets
        self._create_widgets()
        #Variable que contiene la ruta del directorio
        self.path = ""
        #Variable que indica que si los archivos ya se organizaron
        self.organized_files = False

    
    def _create_widgets(self):
        
        """
        Crea los Labels y Botones en la interfaz gráfica

        """
        

        self.path_label = ttk.Label(self.root, text="Ruta:", font=(14))
        self.path_label.grid(row=0, column=1,padx=10,pady=10)
        #Frame para contener el entry y el botón para obtener la ruta
        frame_entry = ttk.Frame(self.root)
        frame_entry.grid(row=1,column=1,padx=10,pady=10)

        # Entry del cuál se obtendrá la ruta de la carpeta
        self.path_entry = ttk.Entry(frame_entry, width=30,font=(6))
        self.path_entry.pack(side="left")

        #Botón para obetener el path mediante la función get_path()
        self.get_path_button = ttk.Button(frame_entry, text="...", command=self._get_path)
        self.get_path_button.pack(side="left")
        self.get_path_button.configure(width=2)

        # RadioButtons para selecccionar el tipo de ordenamiento
        frame_radiobuttons = ttk.Frame(self.root)
        frame_radiobuttons.grid(row=2,column=1,padx=10,pady=25)

        ttk.Radiobutton(
            frame_radiobuttons,
            text="Organizar por tipo",
            variable=self.modo_ordenamiento,
            value="por_tipo"
            ).pack(side="left",padx=10)
        
        ttk.Radiobutton(
            frame_radiobuttons,
            text="Organizar por fecha",
            variable=self.modo_ordenamiento,
            value="por_fecha"
            ).pack(side="left",padx=10)
        
        #Boton para organizar los archivos mediante la función move_files()
        organizer_button = ttk.Button(self.root, text="Organizar",command=self._move_files)
        organizer_button.grid(row=3,column=1,padx=10,pady=10)

        #Botón para deshacer la acción
        self.undo_button = ttk.Button(self.root, text="Deshacer", command=self._undo_action) 
        self.undo_button.grid(row=4,column=1,padx=10,pady=10)

        
    def _get_path(self):
        """

        Mediante filedialog obtiene la ruta del directorio que contiene los archivos para ordenar y la guarda en el atributo self.path,
        en caso de no hacer una selección de directorio muestra una advertencia en pantalla.

        Notes:

            self.path almacena la ruta obtenida pero lo que realmente se usa para hacer el ordenamiento es el contenido de self.path_entry, es por ello 
            que se carga el contenido de self.path al Entry.

        """
        temp_path = filedialog.askdirectory(title="Selecciona la ruta de la carpeta")
        #self.path_entry.configure(text=self.path)
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0,temp_path)
    

    def _move_files(self):
        """
        Ejecuta la función move_file_2_folders() del módulo file_organizer. Con esto se seleccionan que carpetas crear,
        se crean las carpetas y se mueven los archivos a la que le corresponde.
        
        Raises: 

            FileNotFoundError
                Ocurre cuando se intenta manipular un archivo que no se encuentra, es provocado si la ruta que se obtiene con
                self.path_entry.get().strip() no existe.

        Notes:
            Todas las excepciones ocurren dentro de la función move_files_2_folders(), que a su vez provienen de la funciones auxiliares
            de las que esta hace uso (Revisar el módulo file_organizer). ¿Sería mejor tratar la excepciones directamente en esas funciones? No se, debo investigarlo


        """
        self.path = self.path_entry.get().strip()
        if self.path:
            try:
                modo = self.modo_ordenamiento.get()
                if modo == "por_tipo":
                    self.final_file_path_list, self.final_dir_path_set = organize_files_by_type(self.path,self.file_extentions_dictionary)
                    
                elif modo == "por_fecha":
                    self.final_file_path_list, self.final_dir_path_set = organize_files_by_date(self.path)
            except FileNotFoundError:
                messagebox.showwarning("Advertencia", "El directorio seleccionado no existe.")
            else:
                self.organized_files = True
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún directorio.")
        


    def _undo_action(self):
        if self.organized_files:
            undo_action(self.path, self.final_file_path_list, self.final_dir_path_set)
            self.organized_files = False
            #Para depuración 
            print("Se desorganizaron los archivos")

def run_app(file_extentions_dictionary):
    """
    Ejecuta la interfaz gráfica usando Tkinter.

    Arguments:
        file_extentions_dictionary {dict} -- Contiene extenciones de archivos (key) asociados a un tipo de archivo/carpeta (value).

    """
    root = tk.Tk()
    app = App(root,file_extentions_dictionary)
    #print(type(root))
    root.mainloop()