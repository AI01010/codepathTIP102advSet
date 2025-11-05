class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

#U: post order
#p: left right then parent for all nodes to get post order list returned
# start from left most check left n right child, if exist add to lst otherwise add node and recurse up (add values)

def sum_inventory(inventory):
    if not inventory:
        return 0

    # if root.left:
    return sum_inventory(inventory.left) + sum_inventory(inventory.right) + inventory.val 
    


# Example Usage:
"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))


#time O(n),  space O(n)

