#suffle list

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def shuffle_playlist(playlist):
    if not playlist or not playlist.next:
        return playlist

    # Split the playlist into two halves. slow is mid
    slow = fast = playlist
    prev = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:          # If they meet, there's a cycle
            return True

    # Reverse 2nd half
    curr = slow
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        slow = temp
    
    # Merge two halves
    first = playlist
    second = prev
    while second.next:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2
    return playlist




playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist2 = Node(('Respect', 'Aretha Franklin'),
                Node(('Superstition', 'Stevie Wonder'),
                    Node(('Wonderwall', 'Oasis'),
                        Node(('Like a Prayer', 'Madonna'),
                            Node(('Bohemian Rhapsody', 'Queen'))))))

print_linked_list(shuffle_playlist(playlist1))
print_linked_list(shuffle_playlist(playlist2))


# ex outputs:
# 1 -> 4 -> 2 -> 3
# ('Respect', 'Aretha Franklin') -> ('Bohemian Rhapsody', 'Queen') -> ('Superstition', 'Stevie Wonder') ->
# ('Like a Prayer', 'Madonna') -> ('Wonderwall', 'Oasis')
