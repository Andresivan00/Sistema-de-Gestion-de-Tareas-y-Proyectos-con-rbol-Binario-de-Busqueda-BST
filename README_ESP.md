# Sistema-de-Gestion-de-Tareas-y-Proyectos-con-Arbol-Binario-de-Busqueda-BST

Este proyecto consiste en una aplicación de escritorio desarrollada en **Python**, utilizando la librería **Tkinter** para la interfaz gráfica y un **Árbol Binario de Búsqueda (BST)** como estructura de datos principal para almacenar y organizar tareas y proyectos.

El objetivo es permitir al usuario administrar actividades pendientes mediante operaciones de **inserción**, **búsqueda** y **eliminación**, aprovechando la eficiencia que ofrece un BST frente a estructuras lineales como listas o arreglos.

---

# Estructura de Datos: Árbol Binario de Búsqueda (BST)

El núcleo del sistema está compuesto por dos clases principales.

## Clase `Nodo`

Representa la unidad básica del árbol.

Cada nodo almacena la siguiente información:

- ID único (clave del árbol)
- Tipo de elemento (Tarea o Proyecto)
- Nombre
- Fecha de vencimiento
- Etiquetas
- Referencia al hijo izquierdo
- Referencia al hijo derecho

---

## Clase `Arbol`

Contiene la implementación de todas las operaciones fundamentales del BST.

### Inserción (`insertar`)

Agrega un nuevo nodo respetando la propiedad del árbol binario de búsqueda.

- IDs menores se ubican a la izquierda.
- IDs mayores se ubican a la derecha.
- Si el ID ya existe, se notifica al usuario y no se sobrescribe la información.

---

### Búsqueda (`buscar`)

Recorre el árbol de forma recursiva utilizando el orden de los IDs para descartar la mitad de las posibilidades en cada paso.

**Complejidad promedio**

```text
O(log n)
```

---

### Eliminación (`eliminar`)

Implementa los tres casos clásicos de eliminación en un BST.

#### Caso 1

Nodo sin hijos.

```text
Se elimina directamente.
```

#### Caso 2

Nodo con un solo hijo.

```text
Se reemplaza por su hijo.
```

#### Caso 3

Nodo con dos hijos.

```text
Se reemplaza por el sucesor inorden
(valor mínimo del subárbol derecho).
```

---

### Recorrido Inorden (`listar_inorden`)

Permite obtener todos los elementos ordenados ascendentemente según su ID.

Este recorrido es utilizado para mostrar la información organizada dentro de la interfaz gráfica.

---

# Interfaz Gráfica

La aplicación está dividida en dos secciones principales.

## Panel Izquierdo (Formulario)

Contiene los campos de entrada:

- ID
- Tipo
- Nombre
- Fecha de vencimiento
- Etiquetas

También incluye los botones:

- Agregar
- Buscar
- Eliminar
- Limpiar

Los controles se generan dinámicamente mediante una lista de configuración, evitando la repetición de código.

---

## Panel Derecho (Tabla de Resultados)

Utiliza el componente **Treeview** de Tkinter para mostrar todas las tareas y proyectos registrados.

Características:

- Muestra los datos ordenados automáticamente.
- Se actualiza después de cada operación.
- Obtiene la información mediante el recorrido inorden del árbol.

---

# Validaciones y Manejo de Errores

El sistema implementa validaciones para garantizar la integridad de los datos.

- El ID debe ser un número entero.
- El nombre es un campo obligatorio.
- Antes de eliminar se verifica que el ID exista.
- No se permiten IDs duplicados.
- Los errores se notifican mediante cuadros de diálogo.

---

# Complejidad de las Operaciones

| Operación | Complejidad |
|-----------|------------|
| Insertar | O(log n) |
| Buscar | O(log n) |
| Eliminar | O(log n) |
| Recorrido Inorden | O(n) |

---

# Justificación del Uso de un BST

Se eligió un Árbol Binario de Búsqueda porque ofrece una mayor eficiencia que una lista simple para las operaciones de búsqueda, inserción y eliminación, especialmente cuando el número de elementos aumenta.

Además, al mantener los datos ordenados por ID, permite obtener un listado ordenado de forma natural sin necesidad de aplicar algoritmos adicionales de ordenamiento.

---

# Tecnologías Utilizadas

- Python
- Tkinter
- Árbol Binario de Búsqueda (BST)
- Treeview (ttk)

---

# Conclusión

Este proyecto integra conceptos fundamentales de estructuras de datos con el desarrollo de interfaces gráficas en Python, demostrando cómo un Árbol Binario de Búsqueda puede aplicarse a un caso práctico de gestión de tareas y proyectos. Gracias a esta estructura, las operaciones principales se realizan de manera eficiente y la información permanece organizada automáticamente.
