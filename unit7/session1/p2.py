# U: reversing a list recursively of strings separated by spaces.
# P: convert string to a list then reverse it


def reverse_orders(orders):
    lst = orders.split(" ")
    
    if len(lst) == 1:
        return orders
    
    return lst[len(lst)-1] + " " + reverse_orders(" ".join(lst[:-1]))
 

# Example Usage:

print(reverse_orders("Bagel Sandwich Coffee Bagel Sandwich Coffee Bagel Sandwich Coffee"))

# O(n^2) time & O(n^2) space complexity