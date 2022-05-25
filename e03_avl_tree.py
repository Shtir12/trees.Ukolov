from tree_node import TreeNode
from e02_bst import BST

class AVLTreeNode(TreeNode):
    def __init__(self,data=0,left=None,right=None): #,height=0):
        TreeNode.__init__(self,data,left,right)
        #self.height = height

class AVLTree(BST):
    def __init__(self):
        BST.__init__(self)
        self.height = -1  
        self.balance = 0; 
                
    def height(self):
        if self.root: 
            return self.root.height 
        else: 
            return 0  
    
    def insert_node(self, data, current_node=0):
        BST.insert_node(self, data, current_node=0)
        
    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.root.left.balance < 0:  
                    self.root.left.lrotate()
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.root.right.balance > 0:  
                    self.root.right.rrotate()
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        A = self.root 
        B = self.root.left.root 
        T = B.right.root 
        
        self.root = B 
        B.right.root = A 
        A.left.root = T 

    
    def lrotate(self): 
        A = self.root 
        B = self.root.right.root 
        T = B.left.root 
        
        self.root = B 
        B.left.root = A 
        A.right.root = T 
        
            
    def update_heights(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.left != None: 
                    self.root.left.update_heights()
                if self.root.right != None:
                    self.root.right.update_heights()
            
            self.height = max(self.root.left.height,
                              self.root.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.left != None: 
                    self.root.left.update_balances()
                if self.root.right != None:
                    self.root.right.update_balances()

            self.balance = self.root.left.height - self.root.right.height 
        else: 
            self.balance = 0 
