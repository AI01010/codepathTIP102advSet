#u - spread cure to all camps/nodes in network, each edge is weighted w (time to travese) from node u to node v
# find min time for all nodes to receive cure form node k

#p: 

def spread_cure(n, times, k):

    pass

# Example Usage:

times_1 = [(2, 1, 1), (2, 3, 1), (3, 4, 1)]
times_2 = [(1, 2, 1), (2, 3, 2), (1, 3, 4)]
times_3 = [(1, 2, 1)]

print(spread_cure(1, times_1, 2))
print(spread_cure(3, times_2, 1))
print(spread_cure(2, times_3, 2))