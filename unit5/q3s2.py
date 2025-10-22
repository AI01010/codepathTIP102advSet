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

# loop thru sorted list to find duplicates
# when find duplicate 
def delete_dupes(head):
    if not head:
        return head
    
    while head and head.next and head.next.next and head.value == head.next.value:
        head = head.next.next

    current = head
    prev = None
    while current.next:            

        prev = current
        current = current.next

        while current.next and current.next.value == current.value:
            current = current.next
            prev.next = current.next

        # if not prev:
        #     head = current.next    
     
        
    return head
    

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

head2 = Node(1, Node( 1, Node(2, Node(3, Node(3, Node(4, Node(5)))))))

# Linked List: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head2))


# //we needed a dummy at the top, then dummy.next would always be the correct head
