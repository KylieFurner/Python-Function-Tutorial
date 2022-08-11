# Trees
[Link Back To Welcome Page](welcome.md)

## Introduction
Trees are similar to linked lists but with one main difference. Trees can
connect to multiple nodes. There are also several diifferent kinds of trees:
Binary Trees, Binary Search Trees, and Balanced Binary Search Trees.

## Binary Trees
A Binary Tree is a tree that only links to two nodes. The picture below will
show the **Root** which is the very first node. The bottom nodes that connect to
no other nodes are called **Leaves** 
Nodes that have other nodes connecting to them are **Parent** nodes and the nodes
connected to the parent nodes are **Child** nodes
All the nodes coming off a parent node form a **Subtree** 

![Binary Tree](https://byui-cse.github.io/cse212-course/lesson09/binary_tree.jpeg)

## Binary Search Trees (BST)
A BST is a tree that sorts its data. When new data is added to the tree the value
of the data is compared to the parent node. If the new data is a smaller value 
than the parent node it is placed to the left but if it is greater it will be 
placed to the right. If the data is equal to the value of the parent node it can be 
placed to the right or the left. 
The benefit of a BST is that it is more efficient than the other data structures 
such as linked lists or dynamic arrays. Both lists and arrays have an O(n) performance
and BST's have more of an O(logn) performance, but the BST will only have an O(logn)
performance if the tree remains balanced. If the tree is unbalanced it will look more
like a linked list and will go back to an O(n) performance.

## Balanced Binary Search Trees
For a BST to be balanced it has to have all its subtrees be about the same height.
There are a couple of algorithims to detect if a tree is balanced or unbalanced
one of the most common ones being the AVL (Adelson-Velskii and Landis).
If the AVL finds that there is a difference of more than 2 between subtrees it will
rotate some nodes to correct that difference.


## Python Code

BST Operation | Description | Performance 
------------- | ----------- | -----------
insert(value) | inserts into the tree | O(logn)
remove(value) | removes from the tree | O(logn)
contains(value) | check if the value is in the tree | O(logn)
traverse_forward | visits objects smallest to largest | O(logn)
traverse_reverse | visits objects largest to smallest | O(logn)
height(node) | determines the height of the node | O(logn)
size() | returns the size of the BST | O(1)
empty() | returns true if the root node is empty | O(1)


## Example Problem
Below is an example problem. This example uses 2 classes to first create and 
initialize a tree. The problem then shows how to insert data into a tree and has
a test to the problem beneath it.
```
class BST:
    class Node:
        """
        Each node of the BST will have data and links to the left and right sub-tree. 
        """
        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially the links are unknown so they are set to None.
            """      
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST is empty, then set the root equal to the new 
        node. Otherwise, use _insert to recursively find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root


    def _insert(self, data, node):
        """
        This function will look for a place to insert a node with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking. Call _insert recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking. Call _insert recursively on the right sub-tree.
                self._insert(data, node.right)

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
#After implementing 'no duplicates' rule,
#this next insert will have no effect on the tree.
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
print(x)  # 1, 3, 4, 5, 6, 7, 10
```        

## Problem To Solve
Solve the contains function. A test and the final solution is provided. This function
will need the previous functions from the example to run properly.
```
    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function supports the ability to use 
        the 'in' keyword:
        if 5 in my_bst:
            ("5 is in the bst")
        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains 'data'. The current sub-tree 
        being search is represented by 'node'.  This function is intended to be called 
        the first time by the __contains__ function.
        """
        pass

print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False
```

## Solution
[Solution](solution3.py)