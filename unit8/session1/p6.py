class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

#U - retunr all  leaf nodes
#P: travese all nodes, if leaf (no children) add to returned []

def get_most_specific(taxonomy):
    if not taxonomy:
        return []

    if not taxonomy.right and not taxonomy.left:
        return [taxonomy.val]
    
    return get_most_specific(taxonomy.left) + get_most_specific(taxonomy.right)
    


# Example Usage:

# """
#            Plantae
#           /       \
#          /         \
#         /           \ 
# Non-flowering     Flowering
#    /      \       /        \
# Mosses   Ferns Gymnosperms Angiosperms
#                              /     \
#                         Monocots  Dicots
# """

plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))