class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

#U: post order
#p: left right then parent for all nodes to get post order list returned
# start from left most check left n right child, if exist add to lst otherwise add node and recurse up

def survey_tree(root):
    if not root:
        return []

    # if root.left:
    return survey_tree(root.left) + survey_tree(root.right) + [root.val] 
    
    # if root.right:
    # return survey_tree(root.right) + [root.val]

    # return [root.val]



# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))


#time O(n),  space O(n)

