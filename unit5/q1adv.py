#10-14
# session1
# q1adv.py

#U: when an item is added validate the input
# valid items "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".
#P: creat a list of valid items, check if the input is in list and only validate if so 
#I: 

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name):
        list = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]

        if item_name in list:
            self.furniture.append(item_name)
        
        pass

        




apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species) 
print(apollo.catchphrase)
print(apollo.furniture)


alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)




