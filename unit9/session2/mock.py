# Problem #2 (Same Tree)
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# u: check the trees p and q have the same structure and values in each node

# p: do tree traversl in parallel like inorder and as i go check if the structure for each respected pair of nodes form p and q
#    are equal:   if they have the same children structure and value in other words check all the nodes val and pointers left and right

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

    def build_tree(values):
        if not values:
            return None

        def get_key_value(item):
            if isinstance(item, tuple):
                return item[0], item[1]
            else:
                return None, item

        key, value = get_key_value(values[0])
        root = TreeNode(value, key)
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if index < len(values) and values[index] is not None:
                left_key, left_value = get_key_value(values[index])
                node.left = TreeNode(left_value, left_key)
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                right_key, right_value = get_key_value(values[index])
                node.right = TreeNode(right_value, right_key)
                queue.append(node.right)
            index += 1

        return root

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



def same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    #check each node if val is same
    if p.val != q.val:
        return False
    
    #check left subtree
    if p.left:
        if not q.left:
            return False
        same_tree(p.left, q.left)

    #check right subtree
    if p.right:
        if not q.right:
            return False
        same_tree(p.right, q.right)
        
    return True



root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))
print(same_tree(root, root))  # True
root2 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5), TreeNode(7)))
print(same_tree(root, root2))  # False