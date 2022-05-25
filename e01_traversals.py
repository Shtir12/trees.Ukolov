from tree_node import TreeNode
from tree_visualizer import TreeVisualizer

class RecursiveTraversal:
    @staticmethod
    def preorder(tree_node):
        if not tree_node:
            return []
        return [tree_node.data] + RecursiveTraversal.preorder(tree_node.left) + RecursiveTraversal.preorder(tree_node.right)
    @staticmethod
    def inorder(tree_node):
        if not tree_node:
            return []
        return RecursiveTraversal.inorder(tree_node.left) + [tree_node.data] + RecursiveTraversal.inorder(tree_node.right)
    @staticmethod
    def postorder(tree_node):
        if not tree_node:
            return []
        return RecursiveTraversal.postorder(tree_node.left) + RecursiveTraversal.postorder(tree_node.right) + [tree_node.data]


class IterativeTraversal:
    @staticmethod
    def preorder(tree_node):
        myStack = []
        result = []
        x = tree_node
        while x or myStack : 
            if x:
                myStack.append(x)
                result.append(x.data)
                x = x.left
            else:
                x = myStack.pop()
                x = x.right
        return  result

    @staticmethod
    def inorder(tree_node):
        myStack = []
        result = []
        x = tree_node
        while x or myStack : 
            if x:
                myStack.append(x)
                x = x.left
            else:
                x = myStack.pop()
                result.append(x.data)
                x = x.right
        return  result

    @staticmethod
    def postorder(tree_node):
        myStack = []
        result = []
        x = tree_node
        while x or myStack : 
            if x:
                myStack.append(x)
                result.append(x.data)
                x = x.right
            else:
                x = myStack.pop()
                x = x.left
        return  result[::-1]

    @staticmethod
    def bfs(tree_node):
        if not tree_node:
            return []
        queue = [tree_node]
        result = []
        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
            result.append(cur_node.data)
        return result


expected_preorder = [
    [],
    [1],
    [1, 2, 3],
    [1, 2, 4, 5, 3, 6],
    [8, 5, 1, 7, 10, 12],
    [25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]
]

expected_inorder = [
    [],
    [1],
    [1, 3, 2],
    [4, 2, 5, 1, 6, 3],
    [1, 5, 7, 8, 10, 12],
    [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
]

expected_postorder = [
    [],
    [1],
    [3, 2, 1],
    [4, 5, 2, 6, 3, 1],
    [1, 7, 5, 12, 10, 8],
    [4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25]
]

expected_bfs = [
    [],
    [1],
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6],
    [8, 5, 10, 1, 7, 12],
    [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
]


test_trees = [
    None,
    TreeNode(1),
    TreeNode(1, right=TreeNode(2, left=TreeNode(3))),
    TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6))),
    TreeNode(8, left=TreeNode(5, left=TreeNode(1), right=TreeNode(7)), right=TreeNode(10, right=TreeNode(12))),
    TreeNode(25, left=TreeNode(15, left=TreeNode(10, left=TreeNode(4), right=TreeNode(12)), right=TreeNode(22, left=TreeNode(18), right=TreeNode(24))),
    right=TreeNode(50, left=TreeNode(35, left=TreeNode(31), right=TreeNode(44)), right=TreeNode(70, left=TreeNode(66), right=TreeNode(90))))
]


if __name__ == '__main__':
    for tree in test_trees:
        TreeVisualizer.visualize(tree)

    print('PREORDER:')
    for tree, expected in zip(test_trees, expected_preorder):
        actual = RecursiveTraversal.preorder(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)

    print('INORDER:')
    for tree, expected in zip(test_trees, expected_inorder):
        actual = RecursiveTraversal.inorder(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)

    print('POSTORDER_:')
    for tree, expected in zip(test_trees, expected_postorder):
        actual = RecursiveTraversal.postorder(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)

    print('PREORDER_I:')
    for tree, expected in zip(test_trees, expected_preorder):
        actual = IterativeTraversal.preorder(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)

    print('INORDER_I:')
    for tree, expected in zip(test_trees, expected_inorder):
        actual = IterativeTraversal.inorder(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)

    print('POSTORDER_I:')
    for tree, expected in zip(test_trees, expected_postorder):
        actual = IterativeTraversal.postorder(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)

    print('BFS_I:')
    for tree, expected in zip(test_trees, expected_bfs):
        actual = IterativeTraversal.bfs(tree)
        assert actual == expected, f'expected {expected}, got {actual}'
        print(actual)
