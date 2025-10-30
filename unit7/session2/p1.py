#find part in list and return bool true or false

#binary search

def check_stock(inventory, part_id):
    left, right = 0, len(inventory) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if inventory[mid] == part_id:
            return True
        elif inventory[mid] < part_id:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))  

