import tkinter as tk
from tkinter import messagebox, ttk

# ── Nodo: unidad básica del árbol (una tarea o proyecto) ──
class Nodo:
    def __init__(self, id, tipo, nombre, vencimiento, etiquetas):
        # Datos de la tarea (no afectan la posición del nodo en el árbol)
        self.id          = id           # clave del BST, define su posición
        self.tipo        = tipo         # "tarea" o "proyecto"
        self.nombre      = nombre
        self.vencimiento = vencimiento
        self.etiquetas   = etiquetas

        # Punteros a los hijos (None porque el nodo nace sin hijos)
        self.izquierdo = None   # subárbol con IDs menores
        self.derecho   = None   # subárbol con IDs mayores


# ── Árbol: contiene la raíz y las operaciones principales (CRUD) ──
class Arbol:
    def __init__(self):
        self.raiz = None   # árbol vacío al inicio

    # Método público: punto de entrada usado por la GUI
    def insertar(self, id, tipo, nombre, vencimiento, etiquetas):
        self.raiz = self._insertar_rec(self.raiz, id, tipo, nombre, vencimiento, etiquetas)

    # Baja recursivamente hasta encontrar el lugar correcto según la regla del BST
    def _insertar_rec(self, nodo, id, tipo, nombre, vencimiento, etiquetas):
        # Caso base: hueco vacío encontrado, aquí se crea el nuevo nodo
        if nodo is None:
            return Nodo(id, tipo, nombre, vencimiento, etiquetas)

        if id < nodo.id:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, id, tipo, nombre, vencimiento, etiquetas)
        elif id > nodo.id:
            nodo.derecho = self._insertar_rec(nodo.derecho, id, tipo, nombre, vencimiento, etiquetas)
        else:
            # ID repetido: se avisa en vez de sobreescribir en silencio
            messagebox.showwarning("Advertencia", f"El ID {id} ya existe.")

        return nodo  # cierra la recursión reconectando cada nivel

    # Búsqueda binaria: en cada paso descarta media rama del árbol
    def buscar(self, id):
        return self._buscar_rec(self.raiz, id)

    def _buscar_rec(self, nodo, id):
        if nodo is None:
            return None            # no encontrado
        if id == nodo.id:
            return nodo             # encontrado
        elif id < nodo.id:
            return self._buscar_rec(nodo.izquierdo, id)
        else:
            return self._buscar_rec(nodo.derecho, id)

    # Elimina un nodo por ID; primero valida que exista
    def eliminar(self, id):
        if self._buscar_rec(self.raiz, id) is None:
            messagebox.showerror("Error", f"El ID {id} no existe.")
            return
        self.raiz = self._eliminar_rec(self.raiz, id)

    def _eliminar_rec(self, nodo, id):
        if nodo is None:
            return None

        # Navega hacia el nodo a eliminar
        if id < nodo.id:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, id)
        elif id > nodo.id:
            nodo.derecho = self._eliminar_rec(nodo.derecho, id)
        else:
            # Nodo encontrado: hay 3 casos posibles según sus hijos

            # Caso 1: sin hijo izquierdo (o ninguno) -> se reemplaza por el derecho
            if nodo.izquierdo is None:
                return nodo.derecho
            # Caso 2: sin hijo derecho -> se reemplaza por el izquierdo
            if nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: dos hijos -> se copia el sucesor inorden (el mínimo
            # del subárbol derecho) y luego se elimina ese sucesor
            sucesor = self._minimo_rec(nodo.derecho)
            nodo.id, nodo.tipo, nodo.nombre = sucesor.id, sucesor.tipo, sucesor.nombre
            nodo.vencimiento, nodo.etiquetas = sucesor.vencimiento, sucesor.etiquetas
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.id)

        return nodo

    # El mínimo de un subárbol siempre está en el extremo izquierdo
    def _minimo_rec(self, nodo):
        if nodo.izquierdo is None:
            return nodo
        return self._minimo_rec(nodo.izquierdo)

    # Recorrido inorden (izq -> raíz -> der): da los nodos ordenados por ID
    def listar_inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is None:
            return
        self._inorden_rec(nodo.izquierdo, resultado)
        resultado.append(nodo)
        self._inorden_rec(nodo.derecho, resultado)


# ── Interfaz gráfica (separada de la lógica del árbol) ──
class App:
    def __init__(self, root):
        self.arbol = Arbol()          # instancia propia del árbol
        self.root  = root
        self.root.title("Gestión de Tareas y Proyectos")
        self.root.state("zoomed")
        self.root.configure(bg="#c0392b")
        self._construir_interfaz()

    def _construir_interfaz(self):
        # ── Panel izquierdo: formulario de entrada ──
        panel_izq = tk.Frame(self.root, bg="#ffffff", width=320)
        panel_izq.pack(side="left", fill="y", padx=10, pady=10)
        panel_izq.pack_propagate(False)   # evita que el frame se encoja

        tk.Label(panel_izq, text="Gestión de Tareas", font=("Helvetica", 14, "bold"),
                 bg="#ffffff", fg="#c0392b").pack(pady=15)

        # Campos generados dinámicamente para no repetir código 5 veces
        campos = [
            ("ID (número):",             "id"),
            ("Tipo (tarea/proyecto):",   "tipo"),
            ("Nombre:",                  "nombre"),
            ("Vencimiento (dd/mm/aaaa):","vencimiento"),
            ("Etiquetas:",               "etiquetas"),
        ]

        # Diccionario para acceder a cada Entry por su nombre clave
        self.entradas = {}
        for label, key in campos:
            tk.Label(panel_izq, text=label, bg="#ffffff", fg="#555555",
                     font=("Helvetica", 9)).pack(anchor="w", padx=15, pady=(8, 0))
            entrada = tk.Entry(panel_izq, bg="#f0f0f0", fg="#222222",
                               insertbackground="#c0392b", relief="flat",
                               font=("Helvetica", 10))
            entrada.pack(fill="x", padx=15, ipady=5)
            self.entradas[key] = entrada

        frame_botones = tk.Frame(panel_izq, bg="#ffffff")
        frame_botones.pack(fill="x", padx=15, pady=15)

        # Botones generados dinámicamente: (texto, color, función asociada)
        botones = [
            ("Agregar",  "#c0392b", self._agregar),
            ("Buscar",   "#b8960c", self._buscar),
            ("Eliminar", "#888888", self._eliminar),
            ("Limpiar",  "#d5d5d5", self._limpiar_formulario),
        ]
        for texto, color, comando in botones:
            tk.Button(frame_botones, text=texto, bg=color, fg="#ffffff",
                      font=("Helvetica", 10, "bold"), relief="flat",
                      cursor="hand2", command=comando).pack(fill="x", pady=3, ipady=6)

        # ── Panel derecho: tabla de resultados ──
        panel_der = tk.Frame(self.root, bg="#f5f5f5")
        panel_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        tk.Label(panel_der, text="Tareas pendientes",
                 font=("Helvetica", 12, "bold"), bg="#f5f5f5", fg="#c0392b").pack(pady=10)

        cols = ("ID", "Tipo", "Nombre", "Vencimiento", "Etiquetas")
        self.tabla = ttk.Treeview(panel_der, columns=cols, show="headings", height=20)

        # Tema "clam" necesario para poder colorear los encabezados
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview", background="#ffffff", foreground="#222222",
                         fieldbackground="#ffffff", font=("Helvetica", 9))
        estilo.configure("Treeview.Heading", background="#c0392b",
                         foreground="#ffffff", font=("Helvetica", 9, "bold"))

        anchos = [50, 80, 200, 120, 150]
        for col, ancho in zip(cols, anchos):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor="center", stretch=True)

        # Scrollbar conectada a la tabla en ambos sentidos
        scroll = ttk.Scrollbar(panel_der, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    # Redibuja la tabla completa a partir del recorrido inorden del árbol.
    # Se llama después de cada operación para mantener la vista sincronizada.
    def _actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for nodo in self.arbol.listar_inorden():
            self.tabla.insert("", "end", values=(
                nodo.id, nodo.tipo, nodo.nombre, nodo.vencimiento, nodo.etiquetas
            ))

    def _agregar(self):
        # Valida que el ID sea un número entero antes de tocar el árbol
        try:
            id = int(self.entradas["id"].get())
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero.")
            return

        tipo        = self.entradas["tipo"].get().strip()
        nombre      = self.entradas["nombre"].get().strip()
        vencimiento = self.entradas["vencimiento"].get().strip()
        etiquetas   = self.entradas["etiquetas"].get().strip()

        # El nombre es obligatorio
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio.")
            return

        self.arbol.insertar(id, tipo, nombre, vencimiento, etiquetas)
        self._actualizar_tabla()
        self._limpiar_formulario()

    def _buscar(self):
        try:
            id = int(self.entradas["id"].get())
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero.")
            return

        resultado = self.arbol.buscar(id)
        if resultado:
            # Muestra solo el nodo encontrado, vaciando el resto de la tabla
            for fila in self.tabla.get_children():
                self.tabla.delete(fila)
            self.tabla.insert("", "end", values=(
                resultado.id, resultado.tipo, resultado.nombre,
                resultado.vencimiento, resultado.etiquetas
            ))
        else:
            messagebox.showinfo("Búsqueda", f"No se encontró ningún elemento con ID {id}.")

    def _eliminar(self):
        try:
            id = int(self.entradas["id"].get())
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero.")
            return

        # arbol.eliminar() ya valida si el ID existe y avisa si no
        self.arbol.eliminar(id)
        self._actualizar_tabla()
        self._limpiar_formulario()

    def _limpiar_formulario(self):
        # Borra todos los campos de texto y refresca la tabla
        for entrada in self.entradas.values():
            entrada.delete(0, tk.END)
        self._actualizar_tabla()


# Punto de entrada: solo se ejecuta si el archivo corre directamente
if __name__ == "__main__":
    root = tk.Tk()
    app  = App(root)
    root.mainloop()