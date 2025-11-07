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



def remove_plant(collection, name):
    if not collection:
        return None
    
    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name) 
    else:
        # Node with only one child or no child
        if not collection.left:
            return collection.right
        elif not collection.right:
            return collection.left
        
        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = collection.right
        while temp.left:
            temp = temp.left
        
        # Copy the inorder successor's content to this node
        collection.val = temp.val
        
        # Delete the inorder successor
        collection.right = remove_plant(collection.right, temp.val)

    return collection



# Example Usage:

# """
#               Money Tree
#              /         \
#            Hoya        Pilea
#               \        /   \
#              Ivy    Orchid  ZZ Plant
# """

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))