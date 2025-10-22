#s1 q6 adv
# u - write catch_fish to retrun the fish the user would expect to catch next. remove that fish from the linked list
# p - 


class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head == None:
        print("Aw! Better luck next time!")
        return None
    
    temp = head
    if head.next != None:
        head = head.next
    else:
        head = None

    print("I caught a " + temp.fish_name +"!")
    return head


#7
# u - print the chance/probability to nearest 100th of catching a target/inouted fish from a creatin given linked list
# p - loop thru the list, add up the freq of the target fish and count the total fishes in the list at the same time
#       divide freq/total
# i
def fish_chances(head, fish_name):
    freq = 0
    total = 0

    while head.next != None:
        total += 1
        if head.fish_name == fish_name:
            freq += 1
        head = head.next

    if total == 0:
        return 0
    
    if head.fish_name == fish_name:
        freq += 1
    total += 1

    return round(freq/total, 2)



#6
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))

#7
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))
print(fish_chances(fish_list, "Rainbow Trout"))
