# counting treasures 
# in a dictionary with location : # of treausres
# assume all postive integers, all locations have a #
# empty case will return 0
# O(n) time & O(1) space complexity

def total_treasures(treasure_map):
    # total = 0

    # for val in treasure_map.values():
    #     total += val

    return sum(treasure_map.values())


treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 