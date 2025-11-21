#hello

#u- find all gear than I can craft based on  input, each gear has a component which needs supplies to make
# given supplies list can i craft the gears needed in my list. components my be supply or gear

#p: bool func per gear and add to buildable lst if can make it
#   if a gear is found in components replace with its component's supplies
#   then cehck if all supplies are available from supplies lst
#   if true (can craft) add to final lst
#   Return a list of all the gear you can craft. You can return the list in any order.


def craftable_gear(gear, components, supplies):
    craftable = []
    
    def is_gear_craftable(idx):
        for i, comp in enumerate(components[idx]):
            if comp in gear:
                is_gear_craftable(i)
            elif comp not in supplies:
                return False
        return True


    for i in range(len(gear)):
        add = True
        for comp in components[i]:
            if comp in gear:
                add = is_gear_craftable(gear.index(comp)) 
                if not add:
                    break
            elif comp not in supplies:
                add = False
                break
           
        if add:
            craftable.append(gear[i])
    
    return craftable


# Example Usage:

gear_1 = ["weapon"]
components_1 = [["metal", "wood"]]
supplies_1 = ["metal", "wood", "rope"]

gear_2 = ["weapon", "trap"]
components_2 = [["metal", "wood"], ["weapon", "wire"]]
supplies_2 = ["metal", "wood", "wire"]

gear_3 = ["weapon", "trap", "shelter"]
components_3 = [["metal", "wood"], ["weapon", "wire"], ["trap", "wood", "metal"]]
supplies_3 = ["metal", "wood", "wire"]

print(craftable_gear(gear_1, components_1, supplies_1))
print(craftable_gear(gear_2, components_2, supplies_2))
print(craftable_gear(gear_3, components_3, supplies_3))