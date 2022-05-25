# trees
Trees exercises for TP course

1. Traversals `e01_traversals.py`

    You have to implement:
    * Recursive traversals
        * preorder (NLR)
        * inorder (LNR)
        * postorder (LRN)
    * Iterative traversals
        * preorder (NLR)
        * inorder (LNR)
        * postorder (LRN)
        * breadth-first (level order) traversal


2. Binary Search Tree (BST) `e02_bst.py`

    Implement:
    * single node insertion
    * insertion of multiple nodes from list
    * node search
    * node deletion

3. AVL Tree `e03_avl_tree.py`

    Implement:
    * AVLTreeNode class
    * AVLTree class with:
    * single node insertion
    * required methods for insertion

    Ensure correct inheritance of `insert_list` method from BST.

## How-to
1. Clone repo
2. `cd` to repo
3. Create and activate virtual environment
    ```bash
    python3 -m venv env
    source ./env/bin/activate
    ```
4. Install requirements
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

> Graphviz package required on your system for tree visualization!
> https://www.graphviz.org/download/
