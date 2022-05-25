
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.data}{f', l = {str(self.left)}' if self.left else ''}{f', r = {str(self.right)}' if self.right else ''})"

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        if self.data != other.data:
            return False
        if self.data == other.data:
            return self.left == other.left and self.right == other.right
            
