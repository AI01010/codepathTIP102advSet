from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# take in 2d array and turn it into binary tree via 1,0 is left child or not

def build_cookie_tree(descriptions):
    cheese = {}
    root = None

    for desc in descriptions:
        parent = desc[0]
        child = desc[1]
        is_left = desc[2]
    
        if parent in cheese:
            parent = cheese[parent]
        else:
            parent = TreeNode(parent)
            cheese[parent.val] = parent

        if not root:
            root = parent

        if child in cheese:
            if child == root.val:
                root = parent
            child = cheese[child]
        else:
            child = TreeNode(child)
            cheese[child.val] = child

        if is_left == 1:
            parent.left = child
        else:
            parent.right = child
    
    return root


# Example Usage:

descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

descriptions3 = [
    ["Peanut Butter", "Sugar", 1],
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
print_tree(build_cookie_tree(descriptions3))
