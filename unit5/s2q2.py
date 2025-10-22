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

#return max value
#edge case: list empty
#time complexity: O(N) - N- num of nodes
#space complexity: O(1) - always only create 2 variables
def find_max(head):
    if not head:
        return None
    max_value = float('-inf')
    curr = head
    while curr:
        max_value = max(curr.value, max_value)
        curr = curr.next
    return max_value


