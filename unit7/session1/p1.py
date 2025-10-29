# U: count layers of a sandwich by nested lists, where each nested list is a layer inside the sandwich,  recursively
# P: base case 1 element if not keep adding to total num of layers int

def count_layers(sandwich):

    if len(sandwich) == 1:
        return 1

    return count_layers(sandwich[1]) + 1


# Example Usage:

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))

# O(n) time and O(1) space complexity