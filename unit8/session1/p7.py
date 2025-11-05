class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if not root:
        return 0

    # print(root.val)
    if root.val > threshold:
        # print("^^^")
        return 1 + count_old_growth(root.right, threshold) + count_old_growth(root.left, threshold)
    
    return count_old_growth(root.right, threshold) + count_old_growth(root.left, threshold)
     



# """
#      100
#      /  \
#     /    \
#   1200  1500
#   /     /  \
# 20    700  2600
# """

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))