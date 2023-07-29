# Data-Structure-with-python

**Description**:

**Sortings:**
This repository contains Python implementations of three popular sorting algorithms: bubble sort, insertion sort, and selection sort. Sorting algorithms are essential in computer science and can be crucial for improving the efficiency of various applications.

**Bubble Sort:** In Bubble Sort algorithm, in every iteration we compare the elements of arr[0] with arr[1], arr[1] with arr[2] and so on. If the first number is greater than the second number we interchange. There are n-1 iterations.

**Insertion Sort:** First we assume that arr[0] is already sorted. Thus we have two parts- Sorted and unsorted part. In this algo, in every iterations, from unsorted part we take one elements one by one and insert it into the sorted part in its proper place. There are n-1 iterations.

**Selection Sort:** In this algorithm, in every iteration we search the smallest element from arr[0],arr[1],...arr[n-1] respectively and interchange it with arr[0],arr[1],...arr[n-1] respectively. There are n-1 iterations.

**Usage**
To use the sorting algorithms, follow these steps:

Create an instance of the sort class.
The constructor of the class prompts you to enter the size of the array and its elements.
Call the sorting methods as needed:
**bubble_sort()** to perform Bubble Sort.
**selection_sort_asc()** to perform Selection Sort in ascending order.
**selection_sort_desc()** to perform Selection Sort in descending order.
**insertion_sort()** to perform Insertion Sort.

**Example Usage:**
ob = sort()
# Enter the size of the array: 5
# Enter an item: 34
# Enter an item: 12
# Enter an item: 56
# Enter an item: 7
# Enter an item: 92
# Before Sorting:
# [34, 12, 56, 7, 92]

ob.bubble_sort()
# After Bubble Sort:
# [7, 12, 34, 56, 92]

ob.selection_sort_asc()
# After Selection Sort in ascending order:
# [7, 12, 34, 56, 92]

ob.selection_sort_desc()
# After Selection Sort in descending order:
# [92, 56, 34, 12, 7]

ob.insertion_sort()
# After Insertion Sort:
# [7, 12, 34, 56, 92]

**Searchings:**
This repository contains various searching algorithms. These searching techniques like Linear Search, Binary Search are used to find elements.

**Linear Search:** This method searches for an element in a list by checking each element one by one until the target element is found.

**Usage**
To use the Linear Search program, follow these steps:

-Run the program.
-Enter the list of items when prompted.
-Enter the search item.
-The program will display the list of items and the search item.
-The program will perform a linear search and output the position of the search item if found or display "Search item is invalid" if the item is not present in the list.

**Binary Search:** Binary search is an efficient algorithm for finding a target element in a sorted list by repeatedly dividing the search space in half. The condition for this search is that the elements are must be in sorted order.

**Usage**
To use the Binary Search program, follow these steps:

-Run the program.
-Enter the size of the array.
-Enter the array elements in ascending order.
-Enter the search item.
-The program will display the array elements and the search item.
-The program will perform a binary search and output the position of the search item if found or display "Search item is invalid" if the item is not present in the array.


**Stack:**
A stack is a linear data structure in which an item is inserted or deleted from one end called TOP of the stack. It follows **FILo** or **LIFO** rules.
Operations on stack are PUSH, POP, Display,etc.

**Class Initialization**
The Operation class is initialized with the following attributes:

**size:** The size of the stack, entered by the user during class initialization.
**top:** A variable that keeps track of the top element of the stack.
**stack:** The list that serves as the stack data structure.

**Methods**

**empty:** Checks if the stack is empty and returns True if it is.

**PUSH:** The "push" operation refers to adding an element to the top of the stack. It increases the stack size by one and places the new element at the top, becoming the new top element.

**POP:** The "pop" operation is used to remove the top element from the stack. It decreases the stack size by one and returns the removed element. The next element below the removed one becomes the new top element.

**peek():** Returns the top element of the stack without removing it. If the stack is empty, it prints "Stack is empty."

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

**Usage**
To use the BST data structure, follow these steps:

-Create a new instance of the BST class.
-Call the createbst(lst) method with a list of integers to create the BST.
-Perform various operations using the available methods like preorder(), inorder(), postorder(), search(item), height(), and delete(t).

val = [100, 50, 90, 130, 110, 150, 120, 30, 20, 45, 130, 140, 115, 105]
ob = BST()
ob.createbst(val)

print("Preorder traversal:", end=" ")
ob.preorder(ob.root)

print("\nInorder traversal:", end=" ")
ob.inorder(ob.root)

print("\nPostorder traversal:", end=" ")
ob.postorder(ob.root)

res = ob.height(ob.root)
print("\nHeight of the tree:", res)

item = int(input("\nEnter the search item:"))
r = ob.search(item)
print("Parent node of the search item is:", r)

item_to_delete = int(input("Enter the item to delete:"))
ob.delete(item_to_delete)

print("\nInorder traversal after deletion:", end=" ")
ob.inorder(ob.root)


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


**QUICK SORT ALGORITHM**
This repository contains a Python implementation of the Quick Sort algorithm, which is one of the widely used sorting algorithms. Quick sort alogorithm uses the idea of divide and conquer. It finds the element called pivot which divides the array into two halves/partitions in such a way that the elements in left half are smaller than or equal to the pivot and the elements in right half are greater than the pivot. 

**Quick Sort Function**
The quicksort function is defined to sort an array a within a specified range. The function takes three parameters:

def quicksort(a, lb, ub):
    if lb < ub:
        piv = quick(a, lb, ub)
        quicksort(a, lb, piv - 1)
        quicksort(a, piv + 1, ub)

**a:** The list to be sorted.
**lb**: The lower bound of the range to be sorted.
**ub:** The upper bound of the range to be sorted.

**Quick Partition Function**
The quick function is used to partition the array into two parts based on a pivot element. The elements less than the pivot are moved to its left, and elements greater than the pivot are moved to its right. The function takes three parameters:

**a:** The list to be sorted.
**lb:** The lower bound of the range to be sorted.
**ub**: The upper bound of the range to be sorted.
def quick(a, lb, ub):
    pivot = lb
    start = lb
    end = ub
    while True:
        # Compare pivot with end (left search)
        while a[pivot] <= a[end] and start <= end:
            end -= 1
        if start > end:
            return pivot  # Pivot in its proper place
        if a[pivot] > a[end]:
            a[pivot], a[end] = a[end], a[pivot]
            pivot = end
            end -= 1

        # Compare pivot with start (right search)
        while a[pivot] >= a[start] and start <= end:
            start += 1
        if start > end:
            return pivot  # Pivot in its proper place
        if a[pivot] < a[start]:
            a[pivot], a[start] = a[start], a[pivot]
            pivot = start
            start += 1

**Usage**
To use the Quick Sort algorithm, simply call the quicksort function and pass the list of elements to be sorted:

l = input("Enter list of elements:").split()
lst = [int(i) for i in l]
quicksort(lst, 0, len(lst) - 1)
print("Sorted List:", lst)


**Heap Sort Algorithm Implementation**

This repository contains an implementation of the Heap Sort algorithm in Python for both max heap and min heap. The Heap Sort algorithm is a comparison-based sorting algorithm that efficiently sorts an array by building a heap data structure and then repeatedly extracting the maximum (for max heap) or minimum (for min heap) element from the heap and placing it at the end of the sorted array.

**Max Heap Sort**
To perform the Heap Sort for the max heap, we have implemented the following functions:

**build_max_heap(arr):** This function builds the max heap data structure from the input array arr. It is used to create the initial max heap from the given array elements.
**heapsort_for_max_heap(a):** This function performs the heap sort on the input array `a`. It first builds the max heap using the build_max_heap() function and then sorts the array in ascending order by repeatedly swapping the root node (maximum element) with the last element and maintaining the heap property using the heapify_for_max_heap() function.
**heapify_for_max_heap(a, i, size):** This function is used to maintain the max heap property during the heap sort. It takes an array a, an index i, and the size of the heap size as inputs and ensures that the subtree rooted at index i satisfies the max heap property.

**Min Heap Sort**
In addition to the max heap, we also provide functions to perform the Heap Sort for the min heap:

**build_min_heap(arr):** This function builds the min heap data structure from the input array `arr`. It is used to create the initial min heap from the given array elements.
**heapsort_for_min_heap(a):** This function performs the heap sort on the input array `a` for the min heap. It first builds the min heap using the build_min_heap() function and then sorts the array in descending order by repeatedly swapping the root node (minimum element) with the last element and maintaining the heap property using the heapify_for_min_heap() function.
**heapify_for_min_heap(a, i, size):** This function is used to maintain the min heap property during the heap sort for the min heap. It takes an array `a`, an index `i`, and the size of the heap `size` as inputs and ensures that the subtree rooted at index `i` satisfies the min heap property.


This README file provides an overview of the repository, explains the purpose of the graph class, and provides instructions on how to use it.
