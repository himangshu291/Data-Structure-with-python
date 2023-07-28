# Data-Structure-with-python

**Description**:

**Sortings:**
This repository contains Python implementations of three popular sorting algorithms: bubble sort, insertion sort, and selection sort. Sorting algorithms are essential in computer science and can be crucial for improving the efficiency of various applications.

**Bubble Sort:** In Bubble Sort algorithm, in every iteration we compare the elements of arr[0] with arr[1], arr[1] with arr[2] and so on. If the first number is greater than the second number we interchange. There are n-1 iterations.

**Insertion Sort:** First we assume that arr[0] is already sorted. Thus we have two parts- Sorted and unsorted part. In this algo, in every iterations, from unsorted part we take one elements one by one and insert it into the sorted part in its proper place. There are n-1 iterations.

**Selection Sort:** In this algorithm, in every iteration we search the smallest element from arr[0],arr[1],...arr[n-1] respectively and interchange it with arr[0],arr[1],...arr[n-1] respectively. There are n-1 iterations.

**Searchings:**
This repository contains various searching algorithms. These searching techniques like Linear Search, Binary Search are used to find elements.

**Linear Search:** This method searches for an element in a list by checking each element one by one until the target element is found.

**Binary Search:** Binary search is an efficient algorithm for finding a target element in a sorted list by repeatedly dividing the search space in half. The condition for this search is that the elements are must be in sorted order.

**Stack:**
A stack is a linear data structure in which an item is inserted or deleted from one end called TOP of the stack. It follows **FILo** or **LIFO** rules.
Operations on stack are PUSH, POP, Display,etc.

**PUSH:** The "push" operation refers to adding an element to the top of the stack. It increases the stack size by one and places the new element at the top, becoming the new top element.

**POP:** The "pop" operation is used to remove the top element from the stack. It decreases the stack size by one and returns the removed element. The next element below the removed one becomes the new top element.

**Display:** The "display" operation displays the elements of the stack in the order they would be popped out, starting from the top element to the bottom.

**Expression or Notation:**
Combinations of operators and operands are called Expression or notation. 

**Infix Notation:** Infix notation is the most common way of writing expressions where operators are placed between the operands. For example, a+b, b+c.
**Prefix Notation/Polish Notation:** Prefix notation is a way of writing expressions where operators are placed before their operands. For example, +ab.
**Postfix Notation/Reverse Polish Notation:** Postfix notation is a way of writing expressions where operators are placed after their operands.For example, ab+.

**Queue:**
A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It is an ordered collection of elements where the element that is added first is the one that gets removed first. The basic operations supported by a queue are enqueuing (adding an element to the rear end) and dequeuing (removing an element from the front end).

**Types of Queues:**

**Linear Queue:** The most common type of queue is the linear queue, where elements are stored in a linear fashion, and the front and rear pointers move in a single direction. It has two ends: the front end from where elements are dequeued or removed, and the rear end where elements are enqueued or inserted.
**Circular Queue:** A circular queue is a variation of the linear queue in which the rear end is connected to the front end, forming a circular structure. This eliminates the need to shift elements when the rear reaches the end of the queue, allowing efficient utilization of memory.

**Linked List:**
A linked list is a linear data structure in which a node is divided into two or three parts- 
  **info-** it contains the information or value.
  **link/next-** it contains the address of next node.
  **prev-** it contains the address of previous node.
  Here are small definitions of linked lists with different types:

1. **Singly Linked List:**
   - A singly linked list is a type of linked list where each node points only to the next node in the list.
   - It consists of nodes, and each node has data and a single reference to the next node.
   - The last node in a singly linked list points to NULL, indicating the end of the list.

2. **Doubly Linked List:**
   - A doubly linked list is a type of linked list where each node points to both the next node and the previous node in the list.
   - It consists of nodes, and each node has data and two references: one to the next node and one to the previous node.
   - The first node's previous pointer and the last node's next pointer point to NULL.

3. **Circular Linked List:**
   - A circular linked list is a type of linked list where the last node points back to the first node, forming a circular structure.
   - It can be a singly circular linked list or a doubly circular linked list.
   - Circular linked lists can be useful in scenarios where elements need to be continuously traversed.


**BST or Binary Search Tree:**
BST is a binary tree(T), T is either empty or all the nodes of left subtree are less than the root node and all the nodes of right subtree are greater than equal to the root node. Left subtree and right subtree are again BST.

Here are the main **operations** on a Binary Search Tree:

**Insertion:** To add a new element to the BST while preserving the binary search property. The insertion process involves comparing the value to be inserted with the values of nodes in the tree and recursively traversing down the tree until the appropriate position is found to place the new node.

**Search:** To find whether a specific element exists in the BST. The search operation involves comparing the target value with the values of nodes in the tree and recursively traversing left or right based on whether the target value is smaller or larger than the current node's value, respectively, until the target value is found or the search reaches a leaf node.

**Deletion:** To remove a specified element from the BST while maintaining the binary search property. Deleting a node from a BST can be a bit more complex than insertion and search. There are three main cases to consider when deleting a node:

**Node with no children (leaf node):** In this case, the node can be simply removed from the tree.
**Node with one child:** In this case, the node is replaced by its child, and the child is connected to the parent of the deleted node.
**Node with two children:** In this case, the node is replaced by its in-order successor or its in-order predecessor. Then, the original node is deleted from its new position.

**Successor and Predecessor:** To find the in-order successor (the next node in ascending order) and in-order predecessor (the previous node in ascending order) of a given node in the BST.

**In-order Traversal:** In In-order traversal algorithm, we recursively traverse the left subtree of the root node then after backtracking we visit the root node then we traverse the right sub trre of root node.(Left Root Right).

**Pre-order Traversal:** In Pre-order traversal algorithm, we recursively visit the root node then we traverse the left subtree of the root node and after backtracking we traverse the right sub trre of root node.(Root Left Right).

**Post-order Traversal:** In Post-order traversal algorithm, we recursively traverse the left subtree of the root node then we traverse the right sub trre of root node then after backtracking we visit the root node .(Left Right Root).

**Find Minimum and Maximum:** To find the minimum (smallest) and maximum (largest) elements in the BST. The minimum value can be found by traversing to the leftmost node, and the maximum value can be found by traversing to the rightmost node.


**Graph Representation:**
The graph is represented using an adjacency matrix, which is a two-dimensional array. The adjacency matrix stores the connections between nodes. For an undirected graph, the edges between nodes are bidirectional. For a directed graph, the edges have a direction from one node to another.

**Usage:**
Create a graph by initializing an instance of the graph class, providing the number of rows and columns for the adjacency matrix.

Use the **matrix()** method to create the adjacency matrix with all elements initialized to 0.

Use the **adj_for_undirec()** method to add edges for an undirected graph. It prompts the user to enter the number of edges and then the source and destination nodes for each edge.

Use the **adj_for_direc()** method to add edges for a directed graph. It prompts the user to enter the number of edges and then the source and destination nodes for each edge.

Use the **undirec_degree()** method to calculate and display the degree of each node in an undirected graph.

Use the **direc_degree()** method to calculate and display the indegree of each node in a directed graph.

Use the **display()** method to print the adjacency matrix.

This README file provides an overview of the repository, explains the purpose of the graph class, and provides instructions on how to use it.
