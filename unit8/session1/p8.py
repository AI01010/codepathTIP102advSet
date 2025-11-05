class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# check if two trees are identical
# p: check if both nodes are none, if one is none return false, if both not none check values, if not equal return false
# recurse left n right

def is_identical(root1, root2):

    if not root1 and not root2:
        return True
    if not root1 or not root2 or root1.val != root2.val:
        return False

    return is_identical(root1.right, root2.right) and is_identical(root1.left, root2.left)


# Example Usage:

# """
#       1                1
#      / \              / \
#     2   3            2   3  
# """
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

# """
#       1                1
#      /                  \
#     2                    2  
# """

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))