
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

#recursively combo 2 lists
def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a and not sandwich_b:
        return None
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    
    return Node(sandwich_a.value, merge_orders(sandwich_b, sandwich_a.next))


# Example Usage:

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))