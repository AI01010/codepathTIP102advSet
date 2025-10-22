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

# delete skip m nodes then delete n nodes
def edit_dna_sequence(dna_strand, m, n):

    current = dna_strand
    
    while current:
        # Skip m nodes
        for _ in range(m-1):
            if current:
                current = current.next

        # Delete n nodes
        for _ in range(n):
            if current:
                current = current.next

    return dna_strand



dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))