#Trabajo final POO
#GRUPO 2

import datetime
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
from tkinter import simpledialog
from tkcalendar import DateEntry
import sqlite3
import re
#versión final con modificaitones


class Participantes:
    # nombre de la base de datos  y ruta 
    path = r'.'
    db_name = path + r'/Participantes.db'
    actualiza = None
    def __init__(self, master=None):
        # Top Level - Ventana Principal
        self.win = tk.Tk() if master is None else tk.Toplevel()
        
             
        
        # Main widget
        self.mainwindow = self.win
        
        #Label Frame
        self.lblfrm_Datos = tk.LabelFrame(self.win, width= 600, height= 400, labelanchor= "n", 
                                          font= ("Helvetica", 13,"bold"))
        #Label Id
        self.lblId = ttk.Label(self.lblfrm_Datos)
        self.lblId.configure(anchor="e", font="TkTextFont", justify="left", text="Idenficación")
        self.lblId.configure(width="12")
        self.lblId.grid(column="0", padx="5", pady="15", row="0", sticky="w")
        
        #Entry Id
        self.entryId = ttk.Entry(self.lblfrm_Datos, validate="key", validatecommand=(self.win.register(self.valida_numeros2), "%P"))
        self.entryId.grid(column="1", row="0", sticky="w")

        
        
        #Label Nombre
        self.lblNombre = ttk.Label(self.lblfrm_Datos)
        self.lblNombre.configure(anchor="e", font="TkTextFont", justify="left", text="Nombre")
        self.lblNombre.configure(width="12")
        self.lblNombre.grid(column="0", padx="5", pady="15", row="1", sticky="w")
        
        #Entry Nombre
        self.entryNombre = ttk.Entry(self.lblfrm_Datos, validate="key", validatecommand=(self.win.register(self.valida_nombre), "%P"))
        self.entryNombre.grid(column="1", row="1", sticky="w")


        #Label Departamento
        self.lblDep =  ttk.Label(self.lblfrm_Datos)
        self.lblNombre.configure(width="12")
        self.lblNombre.grid(column="0", padx="5", pady="15", row="1", sticky="w")
        
        #Entry Nombre
        #self.entryNombre = tk.Entry(self.lblfrm_Datos)
        #self.entryNombre.configure(exportselection="true", justify="left",relief="groove", width="30")
        
        self.entryNombre = ttk.Entry(self.lblfrm_Datos, validate="key", validatecommand=(self.win.register(self.valida_nombre), "%P"))
        self.entryNombre.grid(column="1", row="1", sticky="w")


        #Label Departamento
        self.lblDep =  ttk.Label(self.lblfrm_Datos)
        self.lblDep.configure(anchor="e", font="TkTextFont", justify="left", text="Departamento")
        self.lblDep.configure(width="14")
        self.lblDep.grid(column="0", padx="5", pady="15", row="2")
        
        #Entry Departamento
        self.comboboxDep = ttk.Combobox(self.lblfrm_Datos,  state="readonly")
        conn = sqlite3.connect(self.db_name)  # Conectar a la base de datos
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT Nombre_Departamento FROM t_ciudades')
        departamentos = cursor.fetchall() 
        self.comboboxDep['values'] = [dep[0] for dep in departamentos] 
        conn.close()
        self.comboboxDep.configure(exportselection="true", justify="left", width="27")
        self.comboboxDep.grid(column="1", row="2", sticky="w")
        self.comboboxDep.bind("<<ComboboxSelected>>", self.carga_Ciudades)
        
        
        #Label Ciudad
        self.lblCiudad =  ttk.Label(self.lblfrm_Datos)
        self.lblCiudad.configure(anchor="e", font="TkTextFont", justify="left", text="Ciudad")
        self.lblCiudad.configure(width="12")
        self.lblCiudad.grid(column="0", padx="5", pady="15", row="3")
        
        #Entry Ciudad
        self.comboboxCiudad = ttk.Combobox(self.lblfrm_Datos,  state="readonly")
        self.comboboxCiudad.configure(exportselection="true", justify="left", width="27")
        self.comboboxCiudad.grid(column="1", row="3", sticky="w")
        
        #Label Direccion
        self.lblDireccion = ttk.Label(self.lblfrm_Datos)
        self.lblDireccion.configure(anchor="e", font="TkTextFont", justify="left", text="Dirección")
        self.lblDireccion.configure(width="12")
        self.lblDireccion.grid(column="0", padx="5", pady="15", row="4", sticky="w")
        
        #Entry Direccion
        self.entryDireccion = tk.Entry(self.lblfrm_Datos)
        self.entryDireccion.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryDireccion.grid(column="1", row="4", sticky="w")
        
        #Label Celular
        self.lblCelular = ttk.Label(self.lblfrm_Datos)
        self.lblCelular.configure(anchor="e", font="TkTextFont", justify="left", text="Celular")
        self.lblCelular.configure(width="12")
        self.lblCelular.grid(column="0", padx="5", pady="15", row="5", sticky="w")
        
        #Entry Celular
        self.entryCelular = ttk.Entry(self.lblfrm_Datos, validate="key", validatecommand=(self.win.register(self.valida_numeros1), "%P"))
     
        #self.entryCelular = tk.Entry(self.lblfrm_Datos)
        #self.entryCelular.configure(exportselection="false", justify="left",relief="groove", width="30")
        self.entryCelular.grid(column="1", row="5", sticky="w")

        #ttk.Label(self.lblfrm_Datos, text="Celular").grid(column=0, row=4, padx=5, pady=5, sticky="w")
           #self.entryCelular.grid(column=1, row=4, sticky="w")


        

        
        #Label Entidad
        self.lblEntidad = ttk.Label(self.lblfrm_Datos)
        self.lblEntidad.configure(anchor="e", font="TkTextFont", justify="left", text="Entidad")
        self.lblEntidad.configure(width="12")
        self.lblEntidad.grid(column="0", padx="5", pady="15", row="6", sticky="w")
        
        #Entry Entidad
        self.entryEntidad = tk.Entry(self.lblfrm_Datos)
        self.entryEntidad.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryEntidad.grid(column="1", row="6", sticky="w")


        #ttk.Label(self.lblfrm_Datos, text="Fecha").grid(column=0, row=5, padx=5, pady=5, sticky="w")
        

        
        #Label Fecha
        self.lblFecha = ttk.Label(self.lblfrm_Datos)
        self.lblFecha.configure(anchor="e", font="TkTextFont", justify="left", text="Fecha")
        self.lblFecha.configure(width="12")
        self.lblFecha.grid(column="0", padx="5", pady="15", row="7", sticky="w")
        
        #Entry Fecha
        #self.entryFecha = tk.Entry(self.lblfrm_Datos)
        self.entryFecha = DateEntry(self.lblfrm_Datos, date_pattern="dd/MM/yyyy")
        #self.entryFecha.configure(exportselection="true", justify="left",relief="groove", width="30")
        self.entryFecha.grid(column="1", row="7", sticky="w")
        self.entryFecha.bind("<Key>", self.valida_Fecha)          
    

        
        #Entry Fecha
        #self.entryFecha = DateEntry(self.lblfrm_Datos, date_pattern="dd/MM/yyyy")
        #self.entryFecha.grid(column=1, row=5, sticky="w")
        #self.entryFecha = tk.Entry(self.lblfrm_Datos)
        #self.entryFecha.configure(exportselection="true", justify="left",relief="groove", width="30")
        #self.entryFecha.grid(column="1", row="7", sticky="w")
        
        
          
        #Configuración del Labe Frame    
        self.lblfrm_Datos.configure(height="430", relief="groove", text=" Inscripción ", width="330")
        self.lblfrm_Datos.place(relx="0.01", rely="0.1", width="300", x="0", y="0")
        #self.lblfrm_Datos.grid_propagate(0)


        #Botón Grabar
        
        self.btnGrabar = ttk.Button(self.win, command=self.adiciona_Registro, width="8")
        self.btnGrabar.configure(state="normal", text="Grabar")
        self.btnGrabar.place(anchor="nw", relx=0.01, rely="0.7", x="2",  y="0")
        #self.btnGrabar.bind("<1>", self.adiciona_Registro, add="+")
        

        #Botón Editar
        self.btnEditar = ttk.Button(self.win)        
        self.btnEditar.configure(text="Editar", width="8")
        self.btnEditar.place(anchor="nw", rely="0.7", x="75", y="0")
        self.btnEditar.bind("<1>", self.edita_tablaTreeView, add="+")
        
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.win, command=self.eliminar_registro)
        self.btnEliminar.configure(text="Eliminar", width="8")
        self.btnEliminar.place(anchor="nw", rely="0.7", x="135", y="0")

        
      

        
        #Botón Consultar
        self.btnConsultar = ttk.Button(self.win)
        self.btnConsultar.configure(text="Consultar", width="8")
        self.btnConsultar.place(anchor="nw", rely="0.7", x="195", y="0")

        self.btnConsultar.bind("<1>", self.consultar_registro, add="+")

        #Botón Cancelar
        self.btnCancelar = ttk.Button(self.win)
        self.btnCancelar.configure(text="Cancelar", width="8",command = self.limpia_Campos)
        self.btnCancelar.place(anchor="nw", rely="0.7", x="255", y="0")

        
        #tablaTreeView
        self.style=ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0, bd=0, background='AliceBlue', font=('Calibri Light',10))
        self.style.configure("estilo.Treeview.Heading", background='Azure', font=('Calibri Light', 10,'bold')) 
        self.style.layout("estilo.Treeview", [('estilo.Treeview.treearea', {'sticky': 'nswe'})])

        self.treeDatos = ttk.Treeview(self.win, height = 10, style="estilo.Treeview")
        self.treeDatos.place(x=380, y=10, height=340, width = 600)

       # Etiquetas de las columnas
        self.treeDatos["columns"]=("Nombre","Departamento","Ciudad","Dirección","Celular","Entidad","Fecha")
        # Determina el espacio a mostrar que ocupa el código
        self.treeDatos.column('#0',         anchor="w", stretch="true", width=60)
        self.treeDatos.column('Nombre',         stretch="true",             width=80)
        self.treeDatos.column('Departamento',   stretch="true",             width=80)
        self.treeDatos.column('Ciudad',         stretch="true",             width=80)
        self.treeDatos.column('Dirección',      stretch="true",             width=70)
        self.treeDatos.column('Celular',        stretch="true",             width=70)
        self.treeDatos.column('Entidad',        stretch="true",             width=90)
        self.treeDatos.column('Fecha',          stretch="true",             width=50) 

       #Encabezados de las columnas de la pantalla
        self.treeDatos.heading('#0',             text = 'Id')
        self.treeDatos.heading('Nombre',         text = 'Nombre')
        self.treeDatos.heading('Departamento',   text = 'Departamento')
        self.treeDatos.heading('Ciudad',         text = 'Ciudad')
        self.treeDatos.heading('Dirección',      text = 'Dirección')
        self.treeDatos.heading('Celular',        text = 'Celular')
        self.treeDatos.heading('Entidad',        text = 'Entidad')
        self.treeDatos.heading('Fecha',          text = 'Fecha')

        #Scrollbar en el eje Y de treeDatos
        self.scrollbar=ttk.Scrollbar(self.win, orient='vertical', command=self.treeDatos.yview)
        self.treeDatos.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(x=1020, y=80, height=400)

        #Carga los datos en treeDatos
        self.lee_tablaTreeView()    
        self.treeDatos.place(anchor="nw", height="400", rely="0.115", width="700", x="320", y="2")
 
    def valida_numeros1(self, value):
        """Valida que solo se ingresen exactamente 10 dígitos numéricos"""
        return re.fullmatch(r"\d{0,10}", value) is not None

    def valida_numeros2(self, value):
        """Valida que solo se ingresen exactamente 15 dígitos numéricos"""
        return re.fullmatch(r"\d{0,15}", value) is not None
        
    def valida_nombre(self, value):
        """Valida que solo se ingresen letras, espacios y acentos"""
        return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]*", value) is not None
        
   
    def eliminar_registro(self):
        """Elimina el registro de la base de datos"""
        identificacion = self.entryId.get()

        if not identificacion:
            mssg.showerror("Error", "Ingrese un número de identificación")
            return

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM t_participantes WHERE Id = ?", (identificacion,))
        conn.commit()
        conn.close()
        mssg.showinfo("Éxito", "Registro eliminado correctamente")
        self.limpia_Campos()
        self.lee_tablaTreeView()




    def valida(self):
        '''Valida que el Id no esté vacio, devuelve True si ok'''
        return (len(self.entryId.get()) != 0 )   

    def run(self):
        self.mainwindow.mainloop()

    def valida_Identificacion(self, event=None):
        ''' Valida que la longitud no sea mayor a 15 caracteres'''
        if event.char:
            if len(self.entryId.get()) >= 15:
                mssg.showerror('Atención!!','.. ¡Máximo 15 caracteres! ..')
                self.entryId.delete(15,"end")
        else:
              self.entryId.delete(15,"end")

    def valida_Fecha(self, event=None):
        ''' Valida que la fecha ingresada sea correcta en formato dd/mm/yyyy '''
        fecha_texto = self.entryFecha.get()
        try:
            # Intentamos convertir la fecha
            fecha_obj = datetime.datetime.strptime(fecha_texto, "%d/%m/%Y")
            # Validamos si el mes y día son correctos
            dia, mes, año = fecha_obj.day, fecha_obj.month, fecha_obj.year
            if not (1 <= dia <= 31 and 1 <= mes <= 12):
                raise ValueError("Fecha incoherente: día o mes fuera de rango.")
            if mes == 2 and dia == 29:  # Verificamos si el año es bisiesto
                if not (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
                    raise ValueError("El año ingresado no es bisiesto.")
        except ValueError:
            if not (fecha_texto == fecha_obj):
                mssg.showerror("Fecha incorrecta", "Ingrese una fecha válida en formato dd/mm/yyyy.")
                self.entryFecha.delete(0, "end")

    def carga_Datos(self):
        ''' Carga los datos en los campos desde el treeView'''
        self.entryId.insert(0,self.treeDatos.item(self.treeDatos.selection())['text'])
        self.entryId.configure(state = 'readonly')
        self.entryNombre.insert(0,self.treeDatos.item(self.treeDatos.selection())['values'][0])
        self.comboboxDep.set(self.treeDatos.item(self.treeDatos.selection())['values'][1])
        self.comboboxCiudad.set(self.treeDatos.item(self.treeDatos.selection())['values'][2])

        self.entryDireccion.insert(0,self.treeDatos.item(self.treeDatos.selection())['values'][3])
        self.entryCelular.insert(0,self.treeDatos.item(self.treeDatos.selection())['values'][4])
        self.entryEntidad.insert(0,self.treeDatos.item(self.treeDatos.selection())['values'][5])
        self.entryFecha.insert(0,self.treeDatos.item(self.treeDatos.selection())['values'][6])
              
    def limpia_Campos(self):
    # Limpiar todos los campos de texto y el combobox. Restablecer el entry id
        self.entryId.delete(0, "end")
        self.entryNombre.delete(0, "end")
        self.entryDireccion.delete(0, "end")
        self.entryCelular.delete(0, "end")
        self.entryEntidad.delete(0, "end")
        self.entryFecha.delete(0, "end")
        self.comboboxDep.set('')
        self.comboboxCiudad.set('')
        self.entryId.configure(state='normal')
    
    def carga_Ciudades(self, event):
        selected_department = self.comboboxDep.get()
        #Si no hay un departameto seleccionado no muestra ninguna ciudad
        if not selected_department:
            self.comboboxCiudad['values'] = []
            return

        try:
            conn = sqlite3.connect(self.db_name)  # Conectar a la base de datos
            cursor = conn.cursor()
            cursor.execute('SELECT Nombre_Ciudad FROM t_ciudades WHERE Nombre_Departamento = ?', (selected_department,))
            ciudades = cursor.fetchall()

            if ciudades:  # Verificar si se encontraron ciudades
                self.comboboxCiudad['values'] = [ciu[0] for ciu in ciudades]
            else:
                self.comboboxCiudad['values'] = []

        # Limpiar el combobox de ciudades
            self.comboboxCiudad.set('')  
        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos: {e}")
        finally:
            conn.close()


    def run_Query(self, query, parametros = ()):
        ''' Función para ejecutar los Querys a la base de datos '''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def lee_tablaTreeView(self):
        ''' Carga los datos de la BD y Limpia la Tabla tablaTreeView '''
        tabla_TreeView = self.treeDatos.get_children()
        for linea in tabla_TreeView:
            self.treeDatos.delete(linea)
        # Seleccionando los datos de la BD
        query = 'SELECT * FROM t_participantes ORDER BY Id DESC'
        db_rows = self.run_Query(query)
        # Insertando los datos de la BD en la tabla de la pantalla
        for row in db_rows:
            self.treeDatos.insert('',0, text = row[0], values = [row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
        
    def adiciona_Registro(self, event=None):
        '''Adiciona un participante a la BD si la validación es True'''
        if self.actualiza:
            self.actualiza = None
            self.entryId.configure(state='readonly')
            query = 'UPDATE t_participantes SET Nombre = ?, Departamento = ?, Ciudad = ?, Direccion = ?, Celular = ?, Entidad = ?, Fecha = ? WHERE Id = ?'
            print("query", query)
            print("self.comboboxDep.get()", self.comboboxDep.get())
            print("self.comboboxCiudad.get()", self.comboboxCiudad.get())
            parametros = (self.entryNombre.get(), self.comboboxDep.get(), self.comboboxCiudad.get(), 
                        self.entryDireccion.get(), self.entryCelular.get(), self.entryEntidad.get(), 
                        self.entryFecha.get(), self.entryId.get())
            self.run_Query(query, parametros)
            mssg.showinfo('Ok', 'Registro actualizado con éxito')
        else:
            query = 'INSERT INTO t_participantes (Id, Nombre, Departamento, Ciudad, Direccion, Celular, Entidad, Fecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
            parametros = (self.entryId.get(), self.entryNombre.get(), self.comboboxDep.get(), 
                        self.comboboxCiudad.get(), self.entryDireccion.get(), self.entryCelular.get(), 
                        self.entryEntidad.get(), self.entryFecha.get())
            if self.valida():
                self.run_Query(query, parametros)
                self.limpia_Campos()
                mssg.showinfo('', f'Registro: {self.entryId.get()} .. agregado')
            else:
                mssg.showerror("¡ Atención !", "No puede dejar la identificación vacía")
        self.limpia_Campos()
        self.lee_tablaTreeView()

    def edita_tablaTreeView(self, event=None):
        try:
            # Carga los campos desde la tabla TreeView
            self.treeDatos.item(self.treeDatos.selection())['values']
            self.limpia_Campos()
            self.actualiza = True # Esta variable controla la actualización
            self.carga_Datos()
        except IndexError as error:
            self.actualiza = None
            mssg.showerror("¡ Atención !",'Por favor seleccione un ítem de la tabla')
            return

    def consultar_registro(self, event=None):
        '''Consulta un participante por ID y carga sus datos en los campos'''
        id_participante = self.entryId.get().strip()
    
        if not id_participante:
            mssg.showerror("Error", "Debe ingresar un ID para consultar.")
            return

        query = "SELECT * FROM t_participantes WHERE Id = ?"
        resultado = self.run_Query(query, (id_participante,))
        datos = resultado.fetchone()

        if datos:
            self.limpia_Campos()
            self.entryId.insert(0, datos[0])
            self.entryNombre.insert(0, datos[1])
            self.comboboxDep.set(datos[2])
            self.comboboxCiudad.set(datos[3])
            self.entryDireccion.insert(0, datos[4])
            self.entryCelular.insert(0, datos[5])
            self.entryEntidad.insert(0, datos[6])
            self.entryFecha.insert(0, datos[7])
            
        else:
            mssg.showerror("Error", "No se encontró ningún participante con ese ID.")

    
    def elimina_Registro(self, event=None):
     pass



#if _name_ == "_main_":
#    app = Participantes()
#    app.run()

if __name__ == "__main__":
    app = Participantes()
    app.run()
