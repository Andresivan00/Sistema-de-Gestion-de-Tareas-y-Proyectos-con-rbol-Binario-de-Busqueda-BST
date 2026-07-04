# Sistema-de-Gestion-de-Tareas-y-Proyectos-con-Arbol-Binario-de-Busqueda-BST

Este proyecto consiste en una aplicación de escritorio desarrollada en Python, utilizando la librería Tkinter para la interfaz gráfica y un Árbol Binario de Búsqueda (BST) como estructura de datos principal para almacenar y organizar tareas y proyectos. El objetivo es permitir al usuario administrar actividades pendientes (tareas o proyectos) mediante operaciones de inserción, búsqueda y eliminación, aprovechando la eficiencia que ofrece un árbol binario frente a estructuras lineales como listas o arreglos.
Estructura de Datos: Árbol Binario de Búsqueda
El núcleo del sistema está compuesto por dos clases principales:
Clase Nodo
Representa la unidad básica del árbol. Cada nodo almacena la información de una tarea o proyecto: un ID único (que funciona como clave del árbol), el tipo de elemento (tarea o proyecto), el nombre, la fecha de vencimiento y las etiquetas asociadas. Además, mantiene dos referencias (izquierdo y derecho) que apuntan a sus posibles subárboles.
Clase Arbol
Contiene la lógica de las operaciones fundamentales sobre el BST:

Inserción (insertar): agrega un nuevo nodo respetando la propiedad del árbol binario de búsqueda (los IDs menores se ubican a la izquierda y los mayores a la derecha). Si el ID ya existe, se notifica al usuario en lugar de sobrescribir la información.
Búsqueda (buscar): recorre el árbol de forma recursiva, descartando en cada paso la mitad de las posibilidades gracias al orden de los IDs, lo que permite una búsqueda eficiente con complejidad promedio de O(log n).
Eliminación (eliminar): contempla los tres casos clásicos de eliminación en un BST: nodo sin hijos o con un solo hijo (se reemplaza directamente), y nodo con dos hijos (se sustituye por su sucesor inorden, es decir, el valor mínimo del subárbol derecho).
Recorrido inorden (listar_inorden): permite obtener todos los elementos ordenados ascendentemente según su ID, lo cual es clave para mostrar la información de manera organizada en la interfaz.

Interfaz Gráfica
La aplicación cuenta con una interfaz dividida en dos secciones:

Panel izquierdo (formulario): contiene los campos de entrada (ID, tipo, nombre, vencimiento y etiquetas) y los botones de acción: Agregar, Buscar, Eliminar y Limpiar. Estos campos se generan de forma dinámica mediante una lista de configuración, evitando la repetición de código.
Panel derecho (tabla de resultados): utiliza un Treeview de Tkinter para mostrar todas las tareas y proyectos registrados, ordenados automáticamente gracias al recorrido inorden del árbol. Cada vez que se realiza una operación (agregar, eliminar), la tabla se actualiza para reflejar el estado actual del árbol.

Validaciones y Manejo de Errores
El sistema incluye validaciones básicas para garantizar la integridad de los datos:

El ID debe ser un número entero; de lo contrario, se muestra un mensaje de error.
El nombre es un campo obligatorio para poder agregar un elemento.
Antes de eliminar, se verifica que el ID exista en el árbol.
Se evita la duplicación de IDs, notificando al usuario mediante una ventana de advertencia.

Justificación del Uso de un BST
Se eligió un Árbol Binario de Búsqueda porque permite realizar operaciones de búsqueda, inserción y eliminación de forma más eficiente que una lista simple, especialmente a medida que crece el número de tareas. Al mantener los elementos ordenados por ID, también resulta natural obtener un listado ordenado sin necesidad de aplicar algoritmos de ordenamiento adicionales.
Conclusión
Este proyecto integra conceptos fundamentales de estructuras de datos (árboles binarios de búsqueda) con el desarrollo de interfaces gráficas en Python, demostrando cómo una estructura de datos eficiente puede aplicarse a un caso práctico y cotidiano como lo es la gestión de tareas y proyectos.
