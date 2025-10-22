class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    if not head:
        print("Empty List")
        return
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


#u: take head of the linked list protein and an integer k, and returns an array of k segments
#p: find len of protein linked list, store size of each seg as m or m-1, 
#   see what combination of m and m-1 len seg = total len
#    m = total/k 
#    n = total%k
#       if total % k == 0
            # add 1 element to each segment n times
#   mkae those seg in a 2d arr and return it

def split_protein_chain(protein, k):
    segArrList = []

    curr = protein
    totalLen = 0
    while curr:
        totalLen += 1
        curr = curr.next

    m = int(totalLen/k)
    n = int(totalLen%k)


    # 37/5 = 7
    # 37%5 = 2

    segArrSizes = [m]*k

    if n != 0:
        for i in range(n):
            segArrSizes[i] +=1
    
    curr2 = protein
    #loop thru k sizes
    for size in segArrSizes:
        if size == 0:
            segArrList.append(None)
            continue
        
        segArr = [0] * size
        for i in range(size):
            segArr[i] = curr2.value  
            curr2 = curr2.next
        segArrList.append(segArr)

    return segArrList



protein1 = Node('Ala', Node('Gly', Node('Leu', Node('Val', Node('Pro', Node('Ser', Node('Thr', Node('Cys'))))))))
protein2 = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))

parts = split_protein_chain(protein1, 3)
print(parts)
# for part in parts:
#     print_linked_list(part)

parts = split_protein_chain(protein2, 5)
print(parts)
# for part in parts:
#     print_linked_list(part)