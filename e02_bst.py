from tree_node import TreeNode
#from tree_visualizer import TreeVisualizer
from e01_traversals import RecursiveTraversal

class BST:
    def __init__(self):
        self.root = None


    def __eq__(self, other):
        if not isinstance(other, BST):
            return False
        return self.root == other.root


    def insert_node(self, data, current_node=0):
        insert_node = TreeNode(data)
        if self.root is None:
            self.root = insert_node
            return
        current_node = self.root
        while True:
            if current_node.data < insert_node.data:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = insert_node
                    break
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = insert_node
                    break
        return self.root


    def insert_list(self, data_list):
        for data in data_list:
            self.insert_node(data)


    def find_node(self, data, current_node=0):
        temp = self.root
        if temp is None:
            return None
        while temp:
            if temp.data < data:
                temp = temp.right
            elif temp.data > data:
                temp = temp.left
            else:
                return temp


    def delete_node(self, node_to_delete, current_node=0):
        key = node_to_delete.data
        curr = self.root
        prev = None
        while(curr != None and curr.data != key):
            prev = curr
            if curr.data < key:
                curr = curr.right
            else:
                curr = curr.left
        if curr == None:
            return self.root
        if curr.left == None or\
            curr.right == None:
            newCurr = None
            if curr.left == None:
                newCurr = curr.right
            else:
                newCurr = curr.left
            if prev == None:
                return newCurr
            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr
            curr = None
        else:
            p = None
            temp = None
            temp = curr.right
            while(temp.left != None):
                p = temp
                temp = temp.left
            if p != None:
                p.left = temp.right
            else:
                curr.right = temp.right
            curr.data = temp.data
            temp = None
        return self.root

  #  def visualize(self):
    #    TreeVisualizer.visualize(self.root)


    def traverse(self):
        return RecursiveTraversal.inorder(self.root)
