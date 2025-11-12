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


def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    
    zigzagBool = False

    lst = []
    queue = deque() #root
    queue.append(cupcakes)
    lst.append(cupcakes.val)

    #search all child nodes in level BFS
    while queue:
        temp = queue.popleft()
        
        temp_lst = []
        if temp.left:
            queue.append(temp.left)
            temp_lst.append(temp.left.val)

        
        if temp.right:
            queue.append(temp.right)
            temp_lst.append(temp.right.val)

        if temp_lst:
            if zigzagBool:
                for item in temp_lst:
                    lst.append(item)
            else:
                for item in temp_lst[::-1]:
                    lst.append(item)


    return lst



# Example Usage:

# """
#             Chocolate
#            /         \
#         Vanilla       Lemon
#        /              /    \
#     Strawberry   Hazelnut   Red Velvet   
# """

# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))

# Example Output:
# ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']