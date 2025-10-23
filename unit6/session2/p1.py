#queue from linked list
# follow FIFO with head an tail access

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None #head
        self.rear = None  #tail
    
    def is_empty(self):
        if not self.front:
            return True
        return False

    def enqueue(self, tval):
        next_song = Node(tval)

        if self.is_empty():
             self.front = next_song
             self.rear = self.front
        else:
            self.rear.next = next_song
            self.rear = self.rear.next
        
    
    def dequeue(self):
        if self.is_empty():
            return None

        curr_song = self.front.value

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            
        return curr_song
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front.value
    


    # Create a new Queue
q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 