from tree_node import TreeNode
from e02_bst import BST

class AVLTreeNode(TreeNode):
    def __init__(self,data=0,bf=0,left=None,right=None, parent=None, height=1):
        TreeNode.__init__(self,data,left,right)
        self.bf = bf
        self.parent = parent
        self.height = height
        #print(data, "-", height)

class AVLTree(BST):      
    #def insert_node(self, data, current_node=0):
        #Normal BST insert
        #BST.insert_node(self, data, current_node=0)
    
    def __init__(self):
        super().__init__()

    def insert_list(self, data_list):
        for data in data_list:
            self.insert_node(data)

    def insert_node(self, data):
        self.root = self._vsavka(self.root, data)

    def _vsavka(self, root: AVLTreeNode, data) -> AVLTreeNode:
        if not root:
            return AVLTreeNode(data, bf=0)
        if data < root.data:
            left_sub_root = self._vsavka(root.left, data)
            root.left = left_sub_root
            left_sub_root.parent = root
        elif data > root.data:
            right_sub_root = self._vsavka(root.right, data)
            root.right = right_sub_root
            right_sub_root.parent = root
        else:
            return root
        root.height = max(self.poluchit_visotu(root.left), self.poluchit_visotu(root.right)) + 1
        root.bf = self.poluchit_visotu(root.left) - self.poluchit_visotu(root.right)
        return self.rebalance(root)

    def rebalance(self, root: AVLTreeNode) -> AVLTreeNode:
        if root.bf == 2:
            if root.left.bf < 0:  # L-R
                root.left = self.vertel_na_levo(root.left)
                return self.vertel_na_pravo(root)
            else:  # L-L
                return self.vertel_na_pravo(root)
        elif root.bf == -2:
            if root.right.bf > 0:  # R-L
                root.right = self.vertel_na_pravo(root.right)
                return self.vertel_na_levo(root)
            else:  # R-R
                return self.vertel_na_levo(root)
        else:
            return root

    def vertel_na_pravo(self, root: AVLTreeNode) -> AVLTreeNode:
        pivot = root.left
        tmp = pivot.right
        pivot.right = root
        pivot.parent = root.parent
        root.parent = pivot
        root.left = tmp
        if tmp:
            tmp.parent = root
        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot
        root.height = max(self.poluchit_visotu(root.left), self.poluchit_visotu(root.right)) + 1
        root.bf = self.poluchit_visotu(root.left) - self.poluchit_visotu(root.right)
        pivot.height = max(self.poluchit_visotu(pivot.left), self.poluchit_visotu(pivot.right)) + 1
        pivot.bf = self.poluchit_visotu(pivot.left) - self.poluchit_visotu(pivot.right)
        return pivot

    def vertel_na_levo(self, root: AVLTreeNode) -> AVLTreeNode:
        pivot = root.right
        tmp = pivot.left
        pivot.left = root
        pivot.parent = root.parent
        root.parent = pivot
        root.right = tmp
        if tmp:
            tmp.parent = root
        if pivot.parent:
            if pivot.parent.left == root:
                pivot.parent.left = pivot
            else:
                pivot.parent.right = pivot
        root.height = max(self.poluchit_visotu(root.left), self.poluchit_visotu(root.right)) + 1
        root.bf = self.poluchit_visotu(root.left) - self.poluchit_visotu(root.right)
        pivot.height = max(self.poluchit_visotu(pivot.left), self.poluchit_visotu(pivot.right)) + 1
        pivot.bf = self.poluchit_visotu(pivot.left) - self.poluchit_visotu(pivot.right)
        return pivot

    def poluchit_visotu(self, root: AVLTreeNode) -> int:
        if not root:
            return 0
        else:
            return root.height
