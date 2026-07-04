# Task and Project Management System Using a Binary Search Tree (BST)

This project consists of a **Python desktop application** developed with **Tkinter** for the graphical user interface and a **Binary Search Tree (BST)** as the main data structure for storing and organizing tasks and projects.

The goal is to allow users to manage pending activities through **insertion**, **search**, and **deletion** operations, taking advantage of the efficiency that a BST provides compared to linear data structures such as lists or arrays.

---

# Data Structure: Binary Search Tree (BST)

The core of the system is composed of two main classes.

## `Node` Class

Represents the basic unit of the tree.

Each node stores the following information:

- Unique ID (tree key)
- Item type (Task or Project)
- Name
- Due date
- Tags
- Reference to the left child
- Reference to the right child

---

## `Tree` Class

Contains the implementation of all fundamental BST operations.

### Insertion (`insert`)

Adds a new node while preserving the Binary Search Tree property.

- Smaller IDs are placed on the left.
- Larger IDs are placed on the right.
- If the ID already exists, the user is notified and the information is not overwritten.

---

### Search (`search`)

Traverses the tree recursively, using the ordering of IDs to eliminate half of the remaining possibilities at each step.

**Average Time Complexity**

```text
O(log n)
```

---

### Deletion (`delete`)

Implements the three classic BST deletion cases.

#### Case 1

Node with no children.

```text
The node is removed directly.
```

#### Case 2

Node with one child.

```text
The node is replaced by its child.
```

#### Case 3

Node with two children.

```text
The node is replaced by its inorder successor
(the smallest value in the right subtree).
```

---

### Inorder Traversal (`inorder_traversal`)

Returns all elements sorted in ascending order by their ID.

This traversal is used to display the information in an organized manner within the graphical interface.

---

# Graphical User Interface

The application is divided into two main sections.

## Left Panel (Form)

Contains the input fields:

- ID
- Type
- Name
- Due Date
- Tags

It also includes the following buttons:

- Add
- Search
- Delete
- Clear

The controls are generated dynamically using a configuration list, reducing code duplication.

---

## Right Panel (Results Table)

Uses Tkinter's **Treeview** widget to display all registered tasks and projects.

Features:

- Automatically displays data in sorted order.
- Refreshes after every operation.
- Retrieves information through the BST inorder traversal.

---

# Validation and Error Handling

The system includes several validations to ensure data integrity.

- The ID must be an integer.
- The Name field is required.
- The system verifies that the ID exists before deletion.
- Duplicate IDs are not allowed.
- Errors are displayed through dialog boxes.

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert | O(log n) |
| Search | O(log n) |
| Delete | O(log n) |
| Inorder Traversal | O(n) |

---

# Why Use a BST?

A Binary Search Tree was chosen because it provides greater efficiency than a simple list for search, insertion, and deletion operations, especially as the number of stored items increases.

Additionally, since the data remains sorted by ID, the system can generate an ordered list naturally without requiring additional sorting algorithms.

---

# Technologies Used

- Python
- Tkinter
- Binary Search Tree (BST)
- Treeview (ttk)

---

# Conclusion

This project combines fundamental **data structure** concepts with **Python GUI development**, demonstrating how a **Binary Search Tree (BST)** can be applied to a practical task and project management system. Thanks to this data structure, the main operations are performed efficiently while keeping the information automatically organized.
