# p2: recursive version returning a boolean

def check_stock(inventory, part_id):
    if not inventory:
        return False
    mid = len(inventory) // 2
    if inventory[mid] == part_id:
        return True
    elif inventory[mid] < part_id:
        return check_stock(inventory[mid + 1:], part_id)
    else:
        return check_stock(inventory[:mid], part_id)

print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))