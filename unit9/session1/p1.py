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


class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

#U is level order traversal of teh wedding dessert
#P start at root and go to next level go across all its child nodes 
# and keep track of what level we are on to add to final list

def listify_design(design):
    if not design:
        return []
    
    # print_tree(design)
    lst = []
    queue = deque() #root
    queue.append(design)
    lst.append([design.val])

    #search all child nodes in level BFS
    while queue:
        temp = queue.popleft()
        # print("pop")
        # print(temp.val)
        
        temp_lst = []
        if temp.left:
            # print("left")
            # print(temp.left.val)
            queue.append(temp.left)
            temp_lst.append(temp.left.val)

        
        if temp.right:
            # print("right")
            # print(temp.right.val)
            queue.append(temp.right)
            temp_lst.append(temp.right.val)

        if temp_lst:
            lst.append(temp_lst)

    return lst

# Example Usage:

# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
croquembouche = TreeNode("Vanilla", None,
                    TreeNode("Chocolate", None, TreeNode("Vanilla"), TreeNode("Matcha")), 
                    TreeNode("Strawberry", None)
                    )
print(listify_design(croquembouche))

# [['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]

# O(n) time complexity, O(n) space complexity