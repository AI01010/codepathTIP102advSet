class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


#U: return a path doen the right (straight right) or just root of no right child
#P: go right from the root till end of right childern that are avaliable

def right_vine(root):
  lst = []
  if not root:
     return []
  
  if not root.right:
     return [root.val]
  
  curr = root
  while curr:
     lst.append(curr.val)
     curr = curr.right
  
  return lst


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

#time complextiy O(n), space O(n)

