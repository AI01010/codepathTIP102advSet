class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root:
        return 0

    if root.val == '+':
        return calculate_yield(root.right) + calculate_yield(root.left)
    
    elif root.val == '-':
        return calculate_yield(root.left) - calculate_yield(root.right)
    
    elif root.val == '*':
        return calculate_yield(root.right) * calculate_yield(root.left)
    
    else:
        return root.val
    
  


# Example Usage:

# """
#       +
#      / \ 
#     /   \
#    -     *
#   / \   / \
#  4   2 10  2
# """

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
