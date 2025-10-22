#s1 q3 adv
# q3: of_personality_type
#U: create a list of all people with a given personality type, return in any order
#P: take the townies list, loop thru it to get all people that mathc witht eh given personality type
#   add them to a new result list and return


#q4 telephone
#u - can you pass a message thru a series of neighbors 1 by 1 to connect 2 villagers. attempt to go form starting to target villager.
#       can only have 1 neighbor so its like a lsit of pointers
#p - treat it like a linked list, check if link from start to target exist and retirn true or false



class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    
    # ... methods from previous problems
    def add_item(self, item_name):
        list = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in list:
            self.furniture.append(item_name)
        pass


def of_personality_type(townies, personality_type):
    result = []

    for person in townies:
        if person.personality == personality_type:
            result.append(person.name)
    return result

#4
def message_received(start_villager, target_villager):
    
    while start_villager.neighbor != None and start_villager.neighbor != target_villager:
        if start_villager.neighbor == target_villager:
            return True
        else:
            start_villager = start_villager.neighbor

    if start_villager.neighbor == target_villager:
            return True
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


#4
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))
