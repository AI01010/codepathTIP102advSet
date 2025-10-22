#print out cycle sublist in linked list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle(protein):
    slow = fast = protein
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected, now list the nodes in the cycle
            cycle_nodes = []
            current = slow
            while True:
                cycle_nodes.append(current.value)
                current = current.next
                if current == slow:
                    break
            return cycle_nodes
    return []  # No cycle detected



# Create a protein linked list with a cycle for testing
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next

print(cycle(protein_head))