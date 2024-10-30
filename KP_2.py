#Given the roots of two binary trees root and subRoot,
#return true if there is a subtree of root with the same structure and node values os subRoot and false otherwise
#A subtree of a binary tree is a tree that consists of a node in tree
#and all of this node's descendants.
#The tree could also be considered as a subtree of itself.
#Example: root  = [3,4,5,1,2]; subRoot = [4,1,2]; output: true

#Definition for a binary tree node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#class Solution(object):
#    def isSubrtee(self, root, subRoot):


def isSubtree(root, subRoot):
    def isMatch(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val and
                isMatch(node1.left, node2.left) and
                isMatch(node1.right, node2.right))

    if not root:
        return False
    if isMatch(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

# узлы
#root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
#subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

root = TreeNode(7, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(4))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

print(isSubtree(root, subRoot))


