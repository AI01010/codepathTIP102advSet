#U - find teh center node of this graph given teh terminal/nodes bi-direction connections. 
# A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.
#P - objective is to find node with n-1 edges. 
# for each node store its # of edges in like a hashmap and then pick 1 with n-1 edges

def find_center(terminals):
    freqMap = {}

    #create hashmap
    for lst in terminals:
        for n in lst:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1

    for node, num_edges in freqMap.items():
        if num_edges == len(freqMap)-1:
            return node
    
    return None

    
#     pass
#  node:edge
#     1:1,  2:3  3:1 4:1
# 4 nodes
# 2:3  3 = 4-1

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))

# O(n) space n time 

